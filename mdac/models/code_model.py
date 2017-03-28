from mdac.models.base_model import BaseModel


class CodeModel(BaseModel):
    def __init__(self):
        """
        this class defines the model for code block
        """
        super().__init__()
        self.__use_raw_data__ = True
        self.label = ""
        self.syntax = ""
        self.caption = ""
        self.file = ""
        self.content = ""

    def __construct__(self, content: str, syntax: str = '', caption: str = '',
                      file: str = "", label: str = ""):
        """
        this function puts value into the class
        :param label: the label of the code for cross ref
        :param syntax: the language of the code this is written in
        :param caption: the caption for this code block
        :param file: the file containing the code
        :param content: the actual code, cannot be used with file
        """
        self.label = label
        self.syntax = syntax
        self.caption = caption
        self.file = file
        self.content = content

    @staticmethod
    def get_content_data_name() -> str:
        """
        this function tells you the 'content' parameter is in the content block
        see base_model for more information on content_block
        :return: the content block implicitly specify the content parameter
        """
        return 'content'
