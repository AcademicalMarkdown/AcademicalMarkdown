from typing import Set

from src.helpers.constants import THEOREM_HEADER_FORMAT_STR


class LatexRegister:
    __theorem_types__ = set()

    @classmethod
    def __clear__(cls):
        """
        this method clears the LatexRegister
        this method is mainly used for testing,
        highly unrecommended to use in your code
        """
        cls.__theorem_types__ = set()

    @classmethod
    def get_theorem_types(cls) -> Set[str]:
        """
        this gets the list of theorem type that has been registered
        if you want to change the theorem type, use `register_theorem_type`

        Theorem type grammar is in latex, usually has 'Lemma', 'Definition' etc
        :return: a list of theorem_type (each is a string)
        """
        return cls.__theorem_types__

    @classmethod
    def get_theorem_header(cls) -> str:
        """
        this method returns the string format of the theorem header
        you can directly plug the return into pandoc document
        :return: a string representing all the theorem header that is needed
        """
        # get all the theorem header for each theorem type
        # for example the theorem header for lemma type will be
        # "\newtheorem{lemma}{lemma}"
        theorem_header_list = [
            THEOREM_HEADER_FORMAT_STR.format(theorem_type=theo_type) for
            theo_type in cls.__theorem_types__
            ]

        # join each theorem header together with new lines
        return '\n'.join(theorem_header_list) + '\n\n'

    @classmethod
    def register_theorem_type(cls, new_theorem_type: str):
        """
        add a new theorem type to the register
        :param new_theorem_type: the new theorem type
        """
        cls.__theorem_types__.add(new_theorem_type)
