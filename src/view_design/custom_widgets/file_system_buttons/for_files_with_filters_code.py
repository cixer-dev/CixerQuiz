from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.file_system_buttons.template \
    import FileSystemButtonTemplate
from src.model.translation_handler import _
from src.model.configurators.accepted_formats_configurator import (
    accepted_formats_formatter,
)


class FilesystemForFilesWithFilters(FileSystemButtonTemplate):
    """QPushButton to select a file matching accepted formats and \
    emit its path."""

    def __init__(self, parent_widget, filters_code):
        super().__init__(parent_widget)
        self.filters_code = filters_code
        self.pressed.connect(self._on_open_filesystem)

    def _on_open_filesystem(self):
        filter_pattern = self._get_filter()

        filepath, x = QtW.QFileDialog.getOpenFileName(
            self.parent_widget,
            _("Select a file to attach to this quiz"),
            self.initial_directory,
            filter_pattern,
        )
        if filepath:
            self.sgn_path_changed.emit(filepath)

    def _get_filter(self):
        return accepted_formats_formatter.get_filter_to_accepted_formats(
            self.filters_code
        )
