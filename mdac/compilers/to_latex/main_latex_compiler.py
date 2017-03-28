import re

from typing import List

from mdac.compilers.common_compilers.constants_compiler import \
    const_compile
from mdac.compilers.to_latex.block_compiler import \
    BlockCompiler
from mdac.compilers.to_latex.refrence_compiler import \
    compile_ref
from mdac.helpers.constants import MDAC_BLOCK_REGEX
from mdac.helpers.general_function import unescape_block
from mdac.registers.common_register import CommonRegister
from mdac.registers.latex_register import LatexRegister


def __invoke_compile__(compiler: BlockCompiler) -> str:
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
        embedded_res = main_compile(compile_res)
        # compile ref
        compile_ref_res = compile_ref(embedded_res)
        # compile constants
        compile_cons_res = const_compile(compile_ref_res)
        # unescape the block
        final_res = unescape_block(compile_cons_res)
    else:
        final_res = compile_res

    return final_res


def __parse_yaml_block__(match_obj: tuple) -> BlockCompiler:
    """
    parse a yaml block
    :param match_obj: a mdac yaml block
    :return: a block compiler that is loaded with data
    """
    compiler = BlockCompiler()
    compiler.parse_match_ob(match_obj)

    return compiler


def __compile_simple_block__(simple_block: str) -> str:
    """
    this function compiles all the simple block
    including compile refs and then unescape
    :param simple_block: the text of one simple block
    :return the compiled text
    """

    # compile the reference
    ref_compile_res = compile_ref(simple_block)
    # compile the constants
    const_compile_res = const_compile(ref_compile_res)
    # unescape the block
    unescape_compile_res = unescape_block(const_compile_res)

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


def main_compile(mdac_content: str) -> str:
    """
    this is the main compile process, this method will be triggered to compile
    embedded block
    including:
    - compile yaml block
    - compile reference
    - compile constants
    - unescape all the blocks
    basically everything you need to do that depends on which kind of block
    you are in
    :param mdac_content: the document after pre-compile
    :return the compiled document
    """
    split_res = re.split(pattern=MDAC_BLOCK_REGEX, string=mdac_content)
    len_res = len(split_res)

    # simple blocks
    help_len = int(len_res / 5) + 1
    simple_blocks = [split_res[5 * i] for i in range(help_len)]
    match_objs = [tuple(split_res[5 * i - 4: 5 * i]) for i in
                  range(1, help_len)]

    # parse all yaml block (this step will also register everything)
    yaml_block_compilers = (
        __parse_yaml_block__(match_obj) for match_obj in match_objs
    )

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


def post_compile(mdac_content: str) -> str:
    """
    everything you need to do after compile blocks
    currently contain:
    - add latex theorem declaration
    - add header
    :param mdac_content: the document after main_compile
    :return the final document
    """
    theorem_header = LatexRegister.get_theorem_header()
    yaml_header = CommonRegister.get_yaml_header()

    return yaml_header + theorem_header + mdac_content


def compile_to_pandoc_for_latex(pre_compile_res: str) -> str:
    """
    this function compiles the mdac (markdown for academia) to pandoc documents
    that is capable of converting to latex
    :param pre_compile_res: the pre compile result
    :return: a pandoc document
    """

    main_compiled = main_compile(pre_compile_res)
    final_document = post_compile(main_compiled)

    return final_document
