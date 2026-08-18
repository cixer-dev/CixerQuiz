from src.model.translation_handler import _
from src.view_design.custom_widgets.plaintexts.huge_header import \
    HugeHeader


class LoadingPlaintext(HugeHeader):
    """Loading text display widget."""

    def __init__(self):
        super().__init__(_("Loading..."))
