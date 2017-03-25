from src.models.base_model import BaseModel


class BaseCompiler(BaseModel):
    def __construct__(self, **karg):
        """
        this is inherited from BaseModel, see models/base_model.py for more
        :param karg:
        """
        raise NotImplementedError

    @staticmethod
    def get_content_data_name() -> list:
        """
        this is inherited from BaseModel, see models/base_model.py for more
        """
        raise NotImplementedError

    def compile(self) -> str:
        raise NotImplementedError
