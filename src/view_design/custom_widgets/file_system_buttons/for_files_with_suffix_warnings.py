from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.custom_widgets.file_system_buttons.template \
    import FileSystemButtonTemplate
from src.model.configurators.accepted_formats_configurator import (
    accepted_formats_formatter,
)
from src.view_design.custom_widgets.error_handlers.warning import (
    WarningMessageBox,
)


class FilesystemForFilesWithSuffixWarning(FileSystemButtonTemplate):
    """QPushButton to select a file matching accepted suffixes and \
    emit its path."""

    def __init__(self, parent_widget, suffix):
        super().__init__(parent_widget)
        self.parent_widget = parent_widget
        self.suffix = suffix

        self.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding,
        )
        self.pressed.connect(self._show_warning_msg)

    def _show_warning_msg(self):
        warning_message = _(
            "Selecting an invalid or impossible path may cause the program "
            "to fail."
            "Press OK to continue or Cancel to abort."
        )
        warning_box = WarningMessageBox(
            self.parent_widget,
            warning_message,
        )
        warning_box.sgn_ok_pressed.connect(self._on_open_filesystem)
        warning_box.show()

    def _on_open_filesystem(self):
        formatted_suffix = (
            accepted_formats_formatter.get_formatted_suffix_to_qdialog_pattern(
                self.suffix
            )
        )

        filepath, x = QtW.QFileDialog.getOpenFileName(
            self.parent_widget,
            _("Select a file to attach to this quiz"),
            self.initial_directory,
            formatted_suffix,
        )
        if filepath:
            self.sgn_path_changed.emit(filepath)
