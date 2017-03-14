from src.models.base_model import BaseModel


class TableModel(BaseModel):
    def __init__(self, label: str, caption: str, top_header: bool = True,
                 content: str = '', file: str = ''):
        """
        This class defines a model for the table class
        :param label: the label for the table, used for cross ref
        :param caption: the caption of the table
        :param top_header: a boolean to indicate does this table have header
        :param content: the actual table, in pandoc markdown format
        :param file: the csv file that contains the table,
                        cannot use with content parameter
        """
        super().__init__()
        self.label = label
        self.caption = caption
        self.top_header = top_header
        self.content = content
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
        :return: the content is the first positional parameter
        """
        return ['content']
