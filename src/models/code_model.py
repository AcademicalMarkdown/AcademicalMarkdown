class CodeModel:
    def __init__(self, label: str, syntax: str, caption: str,
                 file: str = "", content: str = ""):
        """
        this class defines the model for code block
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
        self.__init__(**input_dict)

    @staticmethod
    def get_positional() -> list:
        """
        this function returns the parameters that support positional parameter
        :return: content is the first positional parameter
        """
        return ['content']
