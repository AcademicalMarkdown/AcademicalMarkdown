from typing import List

from src.registers.common_register import CommonRegister


class LatexRegister(CommonRegister):
    def __int__(self):
        """
        this is the all the global variable used in latex compiling
        """
        self.__theorem_types__ = []

    @property
    def theorem_type(self) -> List[str]:
        """
        this gets the list of theorem type that has been registered
        if you want to change the theorem type, use `register_theorem_type`

        Theorem type grammar is in latex, usually has 'Lemma', 'Definition' etc
        :return: a list of theorem_type (each is a string)
        """
        return self.__theorem_types__

    def register_theorem_type(self, new_theorem_type: str):
        """
        add a new theorem type to the register
        :param new_theorem_type: the new theorem type
        """
        self.__theorem_types__.append(new_theorem_type)
