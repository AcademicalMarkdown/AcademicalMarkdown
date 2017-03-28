from markdown_for_academia.models.base_model import BaseModel


class TheoremModel(BaseModel):
    def __init__(self):
        """
        this class is the model for theorem block
        """
        super().__init__()
        self.__use_raw_data__ = False
        self.label = ''
        self.content = ''
        self.theorem_type = ''

    def __construct__(self, content: str, theorem_type: str = "Theorem",
                      label: str = ''):
        """
        this method fills the class in with data
        :param label: the label of the theorem for cross ref
        :param content: the content of the theorem
        :param theorem_type: this is latex theorem type,
                                typically takes on "Lemma", "Definition"...
        """
        self.label = label
        self.content = content
        self.theorem_type = theorem_type

    @staticmethod
    def get_content_data_name() -> str:
        """
        this function tells you the 'content' parameter is in the content block
        see base_model for more information on content_block
        :return: the content block implicitly specify the content parameter
        """
        return "content"
