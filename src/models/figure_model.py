from src.models.base_model import BaseModel


class FigureModel(BaseModel):
    def __init__(self):
        """
        this class defines the model for figure block
        """
        super().__init__()
        self.code = ""
        self.label = ""
        self.source = ""
        self.caption = ""
        self.width = ""
        self.height = ""

    def __construct__(self, label: str, source: str, caption: str,
                      width: str = '', height: str = '', code: str = ''):
        """
        this function is used to construct current class
        :param code: the code to exec will compile,
                        you can use this to generate the figure you want to use
        :param label: the label of the figure to cross ref
        :param source: the image source, can be both web and local
        :param caption: the caption of current figure
        :param width: the width of the image
        :param height: not recommended, recommend to use width
        """
        self.label = label
        self.source = source
        self.caption = caption
        self.width = width
        self.height = height
        self.code = code

    @staticmethod
    def get_positional() -> list:
        """
        this function returns the parameters that support positional parameter
        :return: no parameter support positional
        """
        return ['code']
