from typing import List, Union

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
    positional_para = model.get_positional()

    res_paras = {}
    for index, para in enumerate(paras):
        if isinstance(para, dict):
            res_paras.update(para)
        else:
            res_paras.update({positional_para[index]: para})

    return res_paras
