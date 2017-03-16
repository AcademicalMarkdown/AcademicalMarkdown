from typing import Set


class __CommonRegister__:
    def __init__(self):
        """
        this class is essentially global variables.
        """
        self.__label_list__ = set()

    @property
    def label_list(self) -> Set[str]:
        """
        this function is the property to get label list
        :return: all the label that have been registered
        """
        return self.__label_list__

    def register_new_label(self, new_label: str):
        """
        registering a new label if it is not blank
        :param new_label: the str of the new label
        """
        if new_label:
            self.__label_list__.add(new_label)


global_common_register = __CommonRegister__()
