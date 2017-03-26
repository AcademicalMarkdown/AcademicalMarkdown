import re

import yaml
from typing import List, Union

from src.helpers.constants import UNESCAPED_REGEX_SUB_LIST, \
    YAML_PARSE_ERROR_FORMAT
from src.models.base_model import BaseModel


def positional_to_keyword_para(model: BaseModel,
                               paras: Union[dict, List]) -> dict:
    """
    this function converts positional parameter (a list of parameter)
    to keyword parameter (a dictionary of parameter)
    the positional parameter info can use get_positional method on model to get

    :param model: the type of the model, see the models folder
    :param paras: the parameters, either a list (positional) or a dict(keyword)
    :return: purely keyword parameter (dict)
    """

    # this is already a keyword para
    if isinstance(paras, dict):
        return paras

    # this is not a keyword para
    positional_para = model.get_content_data_name()

    res_paras = {}
    for index, para in enumerate(paras):
        if isinstance(para, dict):
            res_paras.update(para)
        else:
            res_paras.update({positional_para[index]: para})

    return res_paras


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
