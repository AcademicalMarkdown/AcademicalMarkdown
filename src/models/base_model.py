class BaseModel:
    def __init__(self):
        """
        this is a prototype for all the models
        """
        pass

    def load_dict(self, input_dict: dict):
        """
        prototype to load a dict to the class
        :param input_dict: the input dictionary
        """
        raise NotImplementedError

    def construct(self, **karg):
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
