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
    def get_positional() -> list:
        """
        this function is a prototype.
        this function returns the parameters that support positional parameter
        :return: empty list
        """
        raise NotImplementedError
