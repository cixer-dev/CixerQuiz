from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.pages.config_menu.config_area.general_config_panel.\
    language_field.language_selector import LanguageSelector


class LanguageField(QtW.QGridLayout):
    """QGridLayout that contains a language label and selector."""

    sgn_language_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()

        self.parent_widget = parent_widget
        self.language_field_label = QtW.QLabel(_("Language") + ":")
        self.addWidget(self.language_field_label, 0, 0)

        self.language_selector = LanguageSelector(self.parent_widget)
        self.addWidget(self.language_selector, 0, 1)

        self.language_selector.sgn_language_changed.connect(
            self._on_selected_language_changed
        )
        self._set_column_proportion()

    def _on_selected_language_changed(self):
        self.sgn_language_changed.emit()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 20)
        self.setColumnStretch(1, 80)
