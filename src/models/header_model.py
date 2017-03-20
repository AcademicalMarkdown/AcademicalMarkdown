from typing import Dict, List

from src.models.base_model import BaseModel
from src.registers.common_register import CommonRegister


class HeaderModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.constants = {}
        self.outputs = []
        self.__whole_header_dict__ = {}
        self.__use_raw_data__ = True

    def __load_constants__(self, header_dict: dict):
        self.constants = header_dict['constants']

        # convert the dict object into tuples
        constants_set = set(self.constants.items())

        # register the constants
        CommonRegister.register_constants(constants_set)

    def __load_output_config__(self, header_dict: dict):
        self.outputs = header_dict['output']
        CommonRegister.register_output_configs(self.outputs)

    def load_dict(self, input_dict: dict):
        self.__whole_header_dict__ = input_dict

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
        self.outputs = outputs

    @staticmethod
    def get_positional() -> list:
        return []
