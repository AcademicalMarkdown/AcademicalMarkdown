from src.models.base_model import BaseModel


class TheoremModel(BaseModel):
    def __init__(self, label: str, content: str,
                 theorem_type: str = "Theorem"):
        """
        this class is the model for theorem block
        :param label: the label of the theorem for cross ref
        :param content: the content of the theorem
        :param theorem_type: this is latex theorem type,
                                typically takes on "Lemma", "Definition"...
        """
        super().__init__()
        self.label = label
        self.content = content
        self.theorem_type = theorem_type

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
        :return: content is the first positional
                    theorem_type is the second positional parameter
        """
        return ["content", "theorem_type"]
