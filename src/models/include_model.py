from src.models.base_model import BaseModel


class IncludeModel(BaseModel):
    def __init__(self, file: str):
        """
        this is the class for include block model
        :param file: the name of the file to include
        """
        super().__init__()
        self.file = file

    def load_dict(self, input_dict: dict):
        """
        load a dict to the class
        :param input_dict: the input dictionary
        """
        self.__init__(**input_dict)

    @staticmethod
    def get_positional() -> list:
        """
        this function returns the parameters that support positional parameter
        :return: no parameter support positional
        """
        return []
