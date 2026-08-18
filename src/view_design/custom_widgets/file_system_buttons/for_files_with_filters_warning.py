from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.file_system_buttons.template \
    import FileSystemButtonTemplate
from src.model.translation_handler import _
from src.model.configurators.accepted_formats_configurator \
    import accepted_formats_formatter
from src.view_design.custom_widgets.error_handlers.warning \
    import WarningMessageBox


class FilesystemForFilesWithFiltersWarnings(FileSystemButtonTemplate):
    """QPushButton to select a file matching accepted formats with \
    a rejection warning."""

    def __init__(self, parent_widget, filters_code):
        super().__init__(parent_widget)
        self.filters_code = filters_code
        self.pressed.connect(self._show_warning_msg)

    def _show_warning_msg(self):
        warning_message = _(
            "Selecting an invalid or impossible path may cause the program "
            "to fail. "
            "Press OK to continue or Cancel to abort."
        )
        warning_box = WarningMessageBox(
            self.parent_widget,
            warning_message,
        )
        warning_box.show()
        warning_box.sgn_ok_pressed.connect(self._on_open_filesystem)

    def _on_open_filesystem(self):
        filter_pattern = self._get_filter()

        filepath, x = QtW.QFileDialog.getOpenFileName(
            self.parent_widget,
            _("Select a file to attach to this trivia"),
            self.initial_directory,
            filter_pattern,
        )
        if filepath:
            self.sgn_path_changed.emit(filepath)

    def _get_filter(self):
        return accepted_formats_formatter.get_filter_to_accepted_formats(
            self.filters_code
        )
