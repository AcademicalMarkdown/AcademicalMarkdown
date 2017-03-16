import re

from src.helpers.constants import ORIG_PAGE_REF_REGEX_FORMAT, \
    ORIG_REF_REGEX_FORMAT, \
    COMPILED_PAGE_REF_REGEX_FORMAT, COMPILED_REF_REGEX_FORMAT
from src.registers.common_register import global_common_register


def __gen_ref_sub_tuple__(label: str) -> (str, str):
    """
    generate a tuple for re.sub, the first is pattern the second is repl
    :param label: the registered label
    :return: a tuple for re.sub, change [@label] to \ref{label}
    """
    return (ORIG_REF_REGEX_FORMAT.format(label=label),
            COMPILED_REF_REGEX_FORMAT.format(label=label))


def __gen_pageref_sub_tuple__(label: str) -> (str, str):
    """
    generate a tuple for re.sub, the first is pattern the second is repl
    :param label: the registered label
    :return: a tuple for re.sub, change [p@label] to \pageref{label}
    """
    return (ORIG_PAGE_REF_REGEX_FORMAT.format(label=label),
            COMPILED_PAGE_REF_REGEX_FORMAT.format(label=label))


def compile_ref(document: str) -> str:
    """
    compile all the refs: [@label] and [p@label] in side of a document
    :param document: the whole corpus of the document
    :return: a new document with all the refs compiled
    """
    labels = global_common_register.label_list

    # build the replacement tuple
    for label in labels:
        ref_sub_tuple = __gen_ref_sub_tuple__(label)
        pageref_sub_tuple = __gen_pageref_sub_tuple__(label)
        document = re.sub(*ref_sub_tuple, string=document)
        document = re.sub(*pageref_sub_tuple, string=document)

    return document
