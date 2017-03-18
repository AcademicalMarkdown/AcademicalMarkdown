from typing import Dict, List

from src.models.base_model import BaseModel
from src.registers.common_register import CommonRegister


class HeaderModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.constants = {}
        self.outputs = []

    def load_dict(self, input_dict: dict):
        try:
            constants = input_dict['constants']
            CommonRegister.register_constants(constants)
        except KeyError:
            pass

        try:
            outputs = input_dict['output']
            CommonRegister.register_output_configs(outputs)
        except KeyError:
            pass

    def __construct__(self, constants: Dict[str, str],
                      outputs: List[Dict[str, str]]):
        self.constants = constants
        self.outputs = outputs

    @staticmethod
    def get_positional() -> list:
        return []
