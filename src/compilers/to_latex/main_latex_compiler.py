import re
from typing import Union, List

import yaml

from src.compilers.base_compiler import BaseCompiler
from src.compilers.to_latex.code_compiler_latex import CodeCompilerLatex
from src.compilers.to_latex.figure_compiler_latex import FigureCompilerLatex
from src.compilers.to_latex.include_compiler_latex import IncludeCompilerLatex
from src.compilers.to_latex.table_compiler_latex import TableCompilerLatex
from src.compilers.to_latex.theorem_compiler_latex import TheoremCompilerLatex
from src.helpers.constants import YAML_BLOCK_REGEX, \
    YAML_PARSE_ERROR_FORMAT, \
    COMPILER_LOAD_ERROR_FORMAT, \
    YAML_BLOCK_STRIP_REGEX, YAML_BLOCK_STRIP_REPLACE_REGEX
from src.helpers.general_function import positional_to_keyword_para

YAML_HEADER_TO_COMPILER_DICT = {
    'code': CodeCompilerLatex,
    'figure': FigureCompilerLatex,
    'include': IncludeCompilerLatex,
    'table': TableCompilerLatex,
    'theorem': TheoremCompilerLatex
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


def __compile_loaded_yaml__(compiler: BaseCompiler,
                            loaded_yaml: Union[dict, list]) -> str:
    """
    compile a loaded yaml, each loaded_yaml is a dict or a list that
    represent the parameter of a compiler
    :param compiler: the compiler used to compile
    :param loaded_yaml: a dict or a list that is the loaded from yaml block
    :return: compiled string for current block
            (the embedded block will also be compiled)
    """
    # convert the input to keyword parameter
    dict_input = positional_to_keyword_para(compiler, loaded_yaml)

    # load the dict into compiler
    compiler.load_dict(dict_input)

    # compile
    compile_result = compiler.compile()

    # compile embedded yaml block
    final_result = compile_to_pandoc_for_latex(compile_result)

    return final_result


def __compile_yaml_block__(yaml_block: str) -> str:
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
        block_dict = yaml.safe_load(yaml_block)
    except yaml.YAMLError as error:
        raise yaml.YAMLError(
            YAML_PARSE_ERROR_FORMAT.format(yaml_block=yaml_block,
                                           error_message=str(error))
        )

    # identify yaml header
    yaml_header = block_dict.keys()[0]

    # forgive me for not putting this in constant
    compiler = YAML_HEADER_TO_COMPILER_DICT[yaml_header.lower()]

    loaded_yaml = block_dict[yaml_header]
    try:
        compiled_str = __compile_loaded_yaml__(compiler=compiler,
                                               loaded_yaml=loaded_yaml)
    except TypeError as error:
        raise TypeError(COMPILER_LOAD_ERROR_FORMAT.format(
            yaml_block=yaml_block,
            error_message=str(error)
        )
        )

    return compiled_str


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


def compile_to_pandoc_for_latex(mdac_content: str) -> str:
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

    # compile yaml block
    compiled_yaml_blocks = [
        __compile_yaml_block__(yaml_block) for yaml_block in yaml_blocks
        ]

    # merge simple block with compiled yaml block
    document = __merge_blocks__(simple_blocks=simple_blocks,
                                yaml_blocks=compiled_yaml_blocks)

    return document
