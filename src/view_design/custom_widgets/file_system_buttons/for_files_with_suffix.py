from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.custom_widgets.file_system_buttons.template \
    import FileSystemButtonTemplate
from src.model.configurators.accepted_formats_configurator import (
    accepted_formats_formatter,
)


class FilesystemForFilesWithSuffix(FileSystemButtonTemplate):
    """QPushButton to select a file matching accepted suffixes and \
    emit its path."""

    def __init__(self, parent_widget, suffix):
        super().__init__(parent_widget)
        self.parent_widget = parent_widget
        self.suffix = suffix
        self.pressed.connect(self._on_open_filesystem)

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
