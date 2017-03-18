from typing import Set, Dict, Tuple


class CommonRegister:  # a static class with all the common registers
    __label_set__ = set()  # this is all the labels
    __constants_set__ = set()  # this is all the constants
    __output_configs__ = set()  # this is the output setting on the header

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

    @classmethod
    def get_constants_set(cls) -> Set[Tuple[str, str]]:
        """
        get the constants set
        :return: the constants set
        """
        return cls.__constants_set__

    @classmethod
    def register_constants(cls, new_constants: Set[Tuple[str, str]]):
        """
        this is the method to add constants into
        the original constants in the registry
        :param new_constants: a set of new constants that need to be added
        """
        # "|" is the join operator, kind of like '+' for set
        cls.__constants_set__ |= new_constants

    @classmethod
    def get_output_configs(cls) -> Set[Dict[str, str]]:
        """
        get the output configs
        :return: the private __output_configs__
        """
        return cls.__output_configs__

    @classmethod
    def register_output_configs(cls, output_config: Set[Dict[str, str]]):
        """
        add some new output configs to existing ones
        :param output_config: a set of new output configs
        """
        # "|" is the join operator, kind of like '+' for set
        cls.__output_configs__ |= output_config
