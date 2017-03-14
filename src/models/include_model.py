from src.models.base_model import BaseModel


class IncludeModel(BaseModel):
    def __init__(self):
        """
        this is the class for include block model
        """
        super().__init__()
        self.file = ""

    def __construct__(self, file: str):
        """
        this function fills the value into the model
        :param file: the name of the file to include
        """
        self.file = file

    def load_dict(self, input_dict: dict):
        """
        load a dict to the class
        :param input_dict: the input dictionary
        """
        self.__construct__(**input_dict)

    @staticmethod
    def get_positional() -> list:
        """
        this function returns the parameters that support positional parameter
        :return: no parameter support positional
        """
        return []
