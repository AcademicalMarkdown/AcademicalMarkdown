from typing import Dict, List

from src.models.base_model import BaseModel
from src.registers.common_register import CommonRegister


class HeaderModel(BaseModel):
    def __init__(self):
        """
        this class is the model for mdac meta data
        """
        super().__init__()
        # this represents constants in the header
        # whenever see a key, replace it with value
        self.constants = {}

        # this is all the output configs (command line para) in the header
        # this is a list of dicts
        self.output_configs = []

        # this is the loaded yaml header
        self.__header_dict__ = {}

        # do not compile embedded data, and escapes
        self.__use_raw_data__ = True

    def __load_constants__(self, header_dict: dict):
        """
        load the constant setting from the header_dict
        :param header_dict: the loaded yaml header
        """
        self.constants = header_dict['constants']

        # convert the dict object into tuples
        constants_set = set(self.constants.items())

        # register the constants
        CommonRegister.register_constants(constants_set)

    def __load_output_config__(self, header_dict: dict):
        """
        load the output configs from the header_dict
        :param header_dict: the loaded yaml header
        """
        self.output_configs = header_dict['output']
        CommonRegister.register_output_configs(self.output_configs)

    def load_dict(self, input_dict: dict):
        """
        load a input dict into the current object
        :param input_dict: the loaded yaml header
        """
        self.__header_dict__ = input_dict

        try:
            self.__load_constants__(header_dict=input_dict)
        except KeyError:
            pass

        try:
            self.__load_output_config__(header_dict=input_dict)
        except KeyError:
            pass

    def __construct__(self, constants: Dict[str, str],
                      outputs: List[Dict[str, str]]):
        self.constants = constants
        self.output_configs = outputs

    @staticmethod
    def get_positional() -> list:
        """
        all the positional parameters of this block
        :return: for this block there is no positional parameter
        """
        return []
