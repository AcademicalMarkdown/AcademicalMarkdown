import re

from src.helpers.constants import ORIG_CONST_REGEX_FORMAT
from src.registers.common_register import CommonRegister


def const_compile(document: str) -> str:
    """
    this function compiles all the constants inside documents
    :param document: the document that need to be compiled
    :return the compiled document
    """

    constant_tuples = CommonRegister.get_constants_set()

    for const_tuple in constant_tuples:
        # find the reference pattern and the string to replace it with
        reference_pattern = ORIG_CONST_REGEX_FORMAT.format(
            label=const_tuple[0])

        # use lambda to escape characters in const_tuple[1]
        # like \1 or \
        def replace_func(_): return const_tuple[1]

        # replace everything in that document
        document = re.sub(pattern=reference_pattern,
                          repl=replace_func, string=document)

    return document
