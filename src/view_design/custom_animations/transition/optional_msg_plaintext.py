from src.view_design.custom_widgets.plaintexts.huge_header import \
    HugeHeader


class OptionalMsgPlaintext(HugeHeader):
    """Optional message plaintext display widget."""

    def __init__(self, optional_msg: str):
        super().__init__(optional_msg)
