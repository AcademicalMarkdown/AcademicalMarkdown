import re

import yaml

from markdown_for_academia.helpers.constants import UNESCAPED_REGEX_SUB_LIST, \
    YAML_PARSE_ERROR_FORMAT


def unescape_block(block_str: str) -> str:
    """
    this function takes a block of text and unescape it
    :param block_str: the original block string
    :return: the unescaped block text
    """
    # unescape all the escapes
    for escape in UNESCAPED_REGEX_SUB_LIST:
        block_str = re.sub(escape[0], escape[1], block_str)

    return block_str


def load_yaml(yaml_str: str) -> dict:
    """
    this function loads a yaml str and return a dict
    :param yaml_str: the yaml string to load
    :return: the yaml dict
    """
    try:
        return yaml.safe_load(yaml_str)
    except yaml.YAMLError as e:
        raise yaml.YAMLError(YAML_PARSE_ERROR_FORMAT.format(
            yaml_block=yaml_str,
            error_message=str(e)
        ))
