from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.configurators.general_configurator import (
    general_formatter,
    general_reader,
    general_writer,
)


class LanguageSelector(QtW.QComboBox):
    """QComboBox that lets the user select the current language."""

    sgn_language_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.language_to_code = general_reader.read_general_config(
            "languages_to_code"
        )
        self.language_options = general_formatter.get_lang_options()
        self.current_language = general_reader.read_general_config(
            "current_language"
        )

        self.addItems(self.language_options)
        self.setCurrentText(self.current_language)
        self.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding,
        )
        self.currentTextChanged.connect(
            self._on_language_selection_changed
        )

    def _on_language_selection_changed(self, language):
        general_writer.set_general_config(
            "current_language",
            language,
        )
        language_code = self.language_to_code[language]
        general_writer.set_general_config(
            "current_language_code",
            language_code
        )
        self.sgn_language_changed.emit()
