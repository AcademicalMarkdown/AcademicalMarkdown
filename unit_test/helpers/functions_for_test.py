import random

from typing import List


def remove_one_para(para_dict: dict, require_para_list: list) -> (dict, str):
    removed_para = random.choice(require_para_list)
    del para_dict[removed_para]
    return para_dict, removed_para


def add_one_para(para_dict: dict, extra_para_list: List[dict]) -> (dict, str):
    added_para = random.choice(extra_para_list)
    para_dict.update(added_para)
    return para_dict, list(added_para.keys())[0]


def list_eq_unorder(list_1: list, list_2: list) -> bool:
    for element in list_1:
        if element not in list_2:
            return False
    for element in list_2:
        if element not in list_1:
            return False
    return True
