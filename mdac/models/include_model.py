from mdac.models.base_model import BaseModel


class IncludeModel(BaseModel):
    def __init__(self):
        """
        this is the class for include block model
        """
        super().__init__()
        self.__use_raw_data__ = False
        self.file = ""

    def __construct__(self, file: str):
        """
        this function fills the value into the model
        :param file: the name of the file to include
        """
        self.file = file

    @staticmethod
    def get_content_data_name() -> str:
        """
        this function tells you the 'file' parameter is in the content block
        see base_model for more information on content_block
        :return: the content block implicitly specify the file parameter
        """
        return 'file'
