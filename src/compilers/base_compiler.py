import yaml

from src.helpers.general_function import positional_to_keyword_para
from src.models.base_model import BaseModel


class BaseCompiler(BaseModel):
    def __construct__(self, **karg):
        """
        this is inherited from BaseModel, see models/base_model.py for more
        :param karg:
        """
        raise NotImplementedError

    @staticmethod
    def get_positional() -> list:
        """
        this is inherited from BaseModel, see models/base_model.py for more
        """
        raise NotImplementedError

    def load_yaml(self, input_yaml: str):
        """
        load the data in the yaml file into current model
        :param input_yaml:
        """
        # load the block parameter
        paras = yaml.safe_load(input_yaml)
        # convert the parameters to keyword parameters
        key_paras = positional_to_keyword_para(
            model=self, paras=paras
        )
        # load the keyword parameter
        self.load_dict(key_paras)

    def compile(self) -> str:
        raise NotImplementedError
