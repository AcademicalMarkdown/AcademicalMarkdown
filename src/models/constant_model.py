from src.models.base_model import BaseModel


class ConstantModel(BaseModel):
    def __init__(self):
        """
        this class defines the a model class for constant block
        """
        super().__init__()
        self.label = ''
        self.content = ''

    def __construct__(self, label: str, content: str):
        """
        this class defines the a model class for constant block
        :param label: the label of the constant to cross ref
        :param content: the content to replace
        """
        self.label = label
        self.content = content

    @staticmethod
    def get_positional() -> list:
        """
        this function returns the parameters that support positional parameter
        :return: no parameter support positional
        """
        return []
