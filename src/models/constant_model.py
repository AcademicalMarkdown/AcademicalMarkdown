from src.models.base_model import BaseModel


class ConstantModel(BaseModel):
    def __init__(self):
        """
        this class defines the a model class for constant block
        """
        super().__init__()
        self.label = ''
        self.content = ''

    def construct(self, label: str, content: str):
        """
        this class defines the a model class for constant block
        :param label: the label of the constant to cross ref
        :param content: the content to replace
        """
        self.label = label
        self.content = content

    def load_dict(self, input_dict: dict):
        """
        load a dict to the class
        :param input_dict: the input dictionary
        """
        self.construct(**input_dict)

    @staticmethod
    def get_positional() -> list:
        """
        this function returns the parameters that support positional parameter
        :return: no parameter support positional
        """
        return []