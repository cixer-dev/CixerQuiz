from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.custom_widgets.error_handlers.warning import \
    WarningMessageBox
from src.view_design.custom_widgets.file_system_buttons.template \
    import FileSystemButtonTemplate


class FilesystemButtonForDirectory(FileSystemButtonTemplate):
    """QPushButton to select a directory, emit its path, and display \
    a warning message."""

    def __init__(self, parent_widget):
        super().__init__(parent_widget)
        self.pressed.connect(self._show_warning_msg)

    def _show_warning_msg(self):
        warning_message = (
            _(
                "Selecting an invalid or impossible path may cause "
                "the program to fail. "
                "Press OK to continue or Cancel to abort."
            )
        )
        warning_box = WarningMessageBox(
            self.parent_widget,
            warning_message
        )
        warning_box.sgn_ok_pressed.connect(self._on_open_filesystem)
        warning_box.show()

    def _on_open_filesystem(self):
        dirpath = QtW.QFileDialog.getExistingDirectory(
            self.parent_widget,
            _("Select a directory"),
            self.initial_directory,
        )
        if dirpath:
            self.sgn_path_changed.emit(dirpath)
