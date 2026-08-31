from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class CancelButton(QtW.QPushButton):
    """Generic QPushButton for canceling operations."""

    def __init__(self) -> None:
        super().__init__(_("Cancel"))
