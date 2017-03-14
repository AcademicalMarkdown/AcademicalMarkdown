from src.models.base_model import BaseModel


class FigureModel(BaseModel):
    def __init__(self, label: str, source: str, caption: str, width: str = '',
                 height: str = ''):
        """
        this class defines the model for figure block
        :param label: the label of the figure to cross ref
        :param source: the image source, can be both web and local
        :param caption: the caption of current figure
        :param width: the width of the image
        :param height: not recommended, recommend to use width
        """
        super().__init__()
        self.label = label
        self.source = source
        self.caption = caption
        self.width = width
        self.height = height

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
