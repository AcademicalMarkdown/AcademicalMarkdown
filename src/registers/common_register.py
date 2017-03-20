from typing import Set, Dict, Tuple, Iterable

import yaml
from frozendict import frozendict

from src.helpers.constants import RESET_YAML_HEADER_ERROR


class CommonRegister:  # a static class with all the common registers
    __label_set__ = set()  # this is all the labels
    __constants_set__ = set()  # this is all the constants
    __output_configs__ = set()  # this is the output setting on the header
    __header_dict__ = {}

    @classmethod
    def __clear__(cls):
        """
        this method clears the CommonRegister
        this method is mainly used in testing,
        highly unrecommended to use in code
        """
        cls.__label_set__ = set()
        cls.__constants_set__ = set()
        cls.__output_configs__ = set()
        cls.__header_dict__ = {}

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
    def register_constants(cls, new_constants: Iterable[Tuple[str, str]]):
        """
        this is the method to add constants into
        the original constants in the registry
        :param new_constants: a set of new constants that need to be added
        """
        # "|" is the join operator, kind of like '+' for set
        cls.__constants_set__ |= set(new_constants)

    @classmethod
    def get_output_configs(cls) -> Set[Dict[str, str]]:
        """
        get the output configs
        :return: the private __output_configs__
        """
        return cls.__output_configs__

    @classmethod
    def register_output_configs(cls, output_configs: Iterable[Dict[str, str]]):
        """
        add some new output configs to existing ones
        :param output_configs: a set of new output configs
        """

        # freeze configs(dict) so that they can be in a set
        # (dict is mutable) therefore not hashable
        frozen_configs = [frozendict(config) for config in output_configs]

        # "|" is the join operator, kind of like '+' for set
        cls.__output_configs__ |= set(frozen_configs)

    @classmethod
    def register_yaml_header_dict(cls, header_dict: dict):
        """
        register a yaml header in the register.
        when one header is registered, you cannot register another
        :param header_dict: the loaded yaml header
        """
        if cls.__header_dict__:
            raise TypeError(RESET_YAML_HEADER_ERROR)
        else:
            cls.__header_dict__ = header_dict

    @classmethod
    def get_yaml_header(cls) -> str:
        """
        get a yaml string header
        :return: the yaml string (dumped from the registered header)
        """
        if not cls.__header_dict__:
            return ''
        else:
            return yaml.safe_dump(cls.__header_dict__,
                                  explicit_start=True,
                                  explicit_end=True)
