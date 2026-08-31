import os

from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.custom_widgets.push_buttons.\
    standard_button_with_icon import StandardButtonWithIcon


class FileSystemButtonTemplate(StandardButtonWithIcon):
    """QPushButton to select a file matching accepted suffixes and \
    emit its path."""

    sgn_path_changed = QtC.Signal(str)

    def __init__(self, parent_widget):
        super().__init__(standard_icon_key="add_file_icon_path")
        self.parent_widget = parent_widget
        self.initial_directory = os.path.expanduser("~")
        self.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding
        )
