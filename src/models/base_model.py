from typing import Union


class BaseModel:
    def __init__(self):
        """
        this is a prototype for all the models
        """
        # use the raw data for current block compile
        # this means do not change anything in this block's compile result
        # including not compile embedded statement, not unescape characters
        # and so on.
        self.__use_raw_data__ = False

    @property
    def use_raw_data(self):
        return self.__use_raw_data__

    def load_dict(self, input_dict: dict):
        """
        prototype to load a dict to the class
        :param input_dict: the input dictionary
        """
        self.__construct__(**input_dict)

    def __construct__(self, **karg):
        """
        this function instead of __init__ constructs the class
        :param karg: all the parameter to send into the class
        """
        raise NotImplementedError

    @staticmethod
    def get_content_data_name() -> Union[str, None]:
        """
        this function is a prototype.
        this function gives a string that represent the name of the content 
        property, that can be directly write in the content block
        
        Example:
        ==== block_type
        content_block
        ---
        meta_block
        ====
        
        you can see all the block of mdac grammar 
        """
        raise NotImplementedError
