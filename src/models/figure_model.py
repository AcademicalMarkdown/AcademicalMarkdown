from typing import Union

from src.models.base_model import BaseModel


class FigureModel(BaseModel):
    def __init__(self):
        """
        this class defines the model for figure block
        """
        super().__init__()
        self.__use_raw_data__ = False
        self.label = ""
        self.source = ""
        self.caption = ""
        self.width = ""
        self.height = ""

    def __construct__(self, source: str, caption: str,
                      width: Union[str, int] = '',
                      height: Union[str, int] = '',
                      label: str = ''):
        """
        this function is used to construct current class
        :param label: the label of the figure to cross ref
        :param source: the image source, can be both web and local
        :param caption: the caption of current figure
        :param width: the width of the image
        :param height: not recommended, recommend to use width
        """
        self.label = label
        self.source = source
        self.caption = caption
        self.width = str(width)
        self.height = str(height)

    @staticmethod
    def get_content_data_name() -> str:
        """
        this function tells you the 'code' parameter is in the content block
        see base_model for more information on content block
        :return: the content block implicitly specify the code parameter
        """
        return 'source'
