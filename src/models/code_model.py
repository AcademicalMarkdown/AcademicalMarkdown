from src.models.base_model import BaseModel


class CodeModel(BaseModel):
    def __init__(self):
        """
        this class defines the model for code block
        """
        super().__init__()
        self.label = ""
        self.syntax = ""
        self.caption = ""
        self.file = ""
        self.content = ""

    def construct(self, label: str, syntax: str, caption: str, file: str = "",
                  content: str = ""):
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
        :return: content is the first positional parameter
        """
        return ['content']