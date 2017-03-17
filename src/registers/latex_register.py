from typing import Set


class LatexRegister:
    __theorem_types__ = set()

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
    def register_theorem_type(cls, new_theorem_type: str):
        """
        add a new theorem type to the register
        :param new_theorem_type: the new theorem type
        """
        cls.__theorem_types__.add(new_theorem_type)
