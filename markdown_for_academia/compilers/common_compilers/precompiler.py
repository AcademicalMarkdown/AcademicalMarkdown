import re

from markdown_for_academia.compilers.common_compilers.header_compiler import \
    HeaderCompiler
from markdown_for_academia.helpers.constants import YAML_HEADER_REGEX


def pre_compile(mdac_content: str) -> str:
    """
    this is precompile process, this is done before compiling blocks
    currently contain:
    - remove and register header
    :param mdac_content: the input markdown content
    :return the document after it is pre compiled (header compiled)
    """
    match = re.match(YAML_HEADER_REGEX, mdac_content)

    # if there is a yaml header
    if match:
        yaml_header = match.group(1)  # get the match group one
        compiler = HeaderCompiler()  # initialize the header compiler
        compiler.load_header(yaml_header)  # load the header
        # remove yaml header content
        res_content = re.sub(pattern=YAML_HEADER_REGEX, repl='',
                             string=mdac_content)
    # if there is no yaml header
    else:
        res_content = mdac_content

    return res_content
