from markdown_for_academia.models.base_model import BaseModel


class BlockModel(BaseModel):
    def __init__(self):
        """
        an mdac block has the following construction:
        ===== block_type
        content_block
        ---
        meta_block
        =====

        meta_block and the leading "---" is optional
        """
        super().__init__()
        self.block_type = ''  # the type of current block
        self.content_block = ''  # the content block
        self.meta_block = ''  # the meta block, yaml format

    def __construct__(self, content_block: str,
                      meta_block: str = '---', block_type: str = 'code'):
        """
        the function used to put value nto class
        :param content_block: the content inside the content block
        :param meta_block: the meta data block, in yaml format, optional
        :param block_type: the type of current block. if none specified, regard
                            current block as code block
        """
        self.block_type = block_type
        self.content_block = content_block
        self.meta_block = meta_block

    @staticmethod
    def get_content_data_name() -> None:
        """
        this method do not really make sense in this model
        """
        return None
