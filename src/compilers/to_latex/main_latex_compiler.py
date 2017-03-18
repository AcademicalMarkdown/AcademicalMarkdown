import re
from typing import Union, List

import yaml

from src.compilers.base_compiler import BaseCompiler
from src.compilers.to_latex.code_compiler_latex import CodeCompilerLatex
from src.compilers.to_latex.figure_compiler_latex import FigureCompilerLatex
from src.compilers.to_latex.include_compiler_latex import IncludeCompilerLatex
from src.compilers.to_latex.refrence_compiler import compile_ref
from src.compilers.to_latex.table_compiler_latex import TableCompilerLatex
from src.compilers.to_latex.theorem_compiler_latex import TheoremCompilerLatex
from src.helpers.constants import YAML_BLOCK_REGEX, \
    YAML_PARSE_ERROR_FORMAT, \
    COMPILER_LOAD_ERROR_FORMAT, \
    YAML_BLOCK_STRIP_REGEX, YAML_BLOCK_STRIP_REPLACE_REGEX
from src.helpers.general_function import positional_to_keyword_para, \
    unescape_block

# use lambda to get lazy result
YAML_HEADER_TO_COMPILER_DICT = {
    'code': lambda: CodeCompilerLatex(),
    'figure': lambda: FigureCompilerLatex(),
    'include': lambda: IncludeCompilerLatex(),
    'table': lambda: TableCompilerLatex(),
    'theorem': lambda: TheoremCompilerLatex()
}


def __strip_yaml_block__(yaml_block):
    """
    strip an mdac yaml block to a regular yaml block that can be loaded
    :param yaml_block: the mdac yaml block
    :return: a yaml string that can be loaded by PyYaml
    """
    return re.sub(pattern=YAML_BLOCK_STRIP_REGEX,
                  repl=YAML_BLOCK_STRIP_REPLACE_REGEX,
                  string=yaml_block)


def __parse_loaded_yaml__(compiler: BaseCompiler,
                          loaded_yaml: Union[dict, list]) -> BaseCompiler:
    """
    loaded each loaded_yaml into a compiler, and return that compiler
    :param compiler: the compiler used to compile
    :param loaded_yaml: a dict or a list that is the loaded from yaml block
    :return: a compiler object that is loaded with the loaded_yaml
    """
    # convert the input to keyword parameter
    dict_input = positional_to_keyword_para(compiler, loaded_yaml)

    # load the dict into compiler
    compiler.load_dict(dict_input)

    return compiler


def __invoke_compile__(compiler: BaseCompiler) -> str:
    """
    compile the compiler, the compiler is already loaded with data.
    if the compiler type requires raw_data (like code compiler),
    we will not unescape that block and will not compile embedded statements
    :param compiler: a compiler that is loaded with data
    :return: the final string that is compiled
    """
    compile_res = compiler.compile()

    if not compiler.use_raw_data:
        # compile embedded block
        embedded_res = compile_to_pandoc(compile_res)
        # compile ref
        compile_ref_res = compile_ref(embedded_res)
        # unescape the block
        final_res = unescape_block(compile_ref_res)
    else:
        final_res = compile_res

    return final_res


def __parse_yaml_block__(yaml_block: str) -> BaseCompiler:
    """
    compile a yaml block into pandoc
    :param yaml_block: a mdac yaml block
    :return: the compiled pandoc snippet for that block
    """
    # strip yaml
    yaml_block = __strip_yaml_block__(yaml_block)

    # try to load the yaml
    try:
        # remove the leading and ending '%'
        yaml_dict = yaml.safe_load(yaml_block)
    except yaml.YAMLError as error:
        raise yaml.YAMLError(
            YAML_PARSE_ERROR_FORMAT.format(yaml_block=yaml_block,
                                           error_message=str(error))
        )

    # identify yaml header
    yaml_header = tuple(yaml_dict.keys())[0]

    # find the compiler correspond to the header
    # because the YAML_HEADER_TO_COMPILER_DICT is str mapped to functions
    # therefore need the little "()" in the end to call the function
    # see the docs on the beginning of the file on YAML_HEADER_TO_COMPILER_DICT
    # for more info
    compiler = YAML_HEADER_TO_COMPILER_DICT[yaml_header.lower()]()

    # remove the header (get the content of header)
    # example: yaml block:
    # code:
    #     - testing code
    # we want to remove the code header, just use yaml_dict['code']
    loaded_yaml = yaml_dict[yaml_header]
    try:
        compiler = __parse_loaded_yaml__(compiler=compiler,
                                         loaded_yaml=loaded_yaml)
    except TypeError as error:
        raise TypeError(COMPILER_LOAD_ERROR_FORMAT.format(
            yaml_block=yaml_block,
            error_message=str(error)
        )
        )

    return compiler


def __compile_simple_block__(simple_block: str) -> str:
    """
    this function compiles all the simple block
    including compile refs and then unescape
    :param simple_block: the text of one simple block
    :return the compiled text
    """

    ref_compile_res = compile_ref(simple_block)
    unescape_compile_res = unescape_block(ref_compile_res)

    return unescape_compile_res


def __merge_blocks__(simple_blocks: List[str], yaml_blocks: List[str]) -> str:
    """
    merge simple block with compiled yaml block
    basic idea is zip the list together, and then flatten it
    example: [1, 3] merge with [2, 4]
    first zip: [(1,2), (3,4)]
    then flatten: [1, 2, 3, 4]
    :param simple_blocks: the blocks that don't need to be compiled
    :param yaml_blocks: the yaml blocks
    :return: a merged document
    """
    # take out the last simple block,
    # because there is one more simple block than yaml block
    last_simple_block = simple_blocks.pop()

    # zip them
    zipped_list = zip(simple_blocks, yaml_blocks)

    # flatten them
    flattened_list = [
        block for block_tuple in zipped_list for block in block_tuple]

    # concatenate
    return ''.join(flattened_list + [last_simple_block])


def compile_to_pandoc(mdac_content: str) -> str:
    """
    this function compiles the mdac (markdown for academia) to pandoc documents
    that is capable of converting to latex
    :param mdac_content: the content of the mdac file
    :return: a pandoc document
    """
    # find all the yaml block
    yaml_blocks = re.findall(pattern=YAML_BLOCK_REGEX, string=mdac_content)

    # a list of regular block
    simple_blocks = re.split(pattern=YAML_BLOCK_REGEX, string=mdac_content)

    # parse all yaml block (this step will also register everything)
    yaml_block_compilers = [
        __parse_yaml_block__(yaml_block) for yaml_block in yaml_blocks
        ]

    # compile all the yaml block
    yaml_block_compile_res = [
        __invoke_compile__(compiler) for compiler in yaml_block_compilers
        ]

    # compile all the simple block
    # this has to be later than parse yaml block, because we need to register
    # labels in order to compile ref
    compiled_simple_block = [
        __compile_simple_block__(simp_block) for simp_block in simple_blocks
        ]

    # merge simple block with compiled yaml block
    document = __merge_blocks__(simple_blocks=compiled_simple_block,
                                yaml_blocks=yaml_block_compile_res)

    return document