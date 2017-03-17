from typing import Set


class CommonRegister:  # a static class with all the common registers
    __label_set__ = set()  # this is all the labels

    @classmethod
    def get_label_set(cls) -> Set[str]:
        """
        this function is the property to get label list
        :return: all the label that have been registered
        """
        return cls.__label_set__

    @classmethod
    def register_new_label(cls, new_label: str):
        """
        registering a new label if it is not blank
        :param new_label: the str of the new label
        """
        if new_label:
            cls.__label_set__.add(new_label)
