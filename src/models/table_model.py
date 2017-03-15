from src.models.base_model import BaseModel


class TableModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.file = ''
        self.content = ""
        self.top_header = True
        self.caption = ""
        self.label = ''

    def __construct__(self, caption: str, top_header: bool = True,
                      content: str = '', file: str = '', label: str = ''):
        """
        This method fill the class in with data
        :param label: the label for the table, used for cross ref
        :param caption: the caption of the table
        :param top_header: a boolean to indicate does this table have header
        :param content: the actual table, in pandoc markdown format
        :param file: the csv file that contains the table,
                        cannot use with content parameter
        """
        self.file = file
        self.content = content
        self.top_header = top_header
        self.caption = caption
        self.label = label

    @staticmethod
    def get_positional() -> list:
        """
        this function returns the parameters that support positional parameter
        :return: the content is the first positional parameter
        """
        return ['content']
