from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.pages.config_menu.config_area.general_config_panel.\
    language_field.brain import LanguageField
from src.view_design.pages.config_menu.config_area.general_config_panel.\
    font_selectors.brain import FontSelectors
from src.view_design.custom_widgets.plaintexts.big_header \
    import BigHeaderColored


class GeneralPanel(QtW.QVBoxLayout):
    """QVBoxLayout containing general configuration controls."""

    sgn_general_panel_was_changed = QtC.Signal()
    sgn_general_config_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.general_label = BigHeaderColored(_("General config"))
        self.language_field = LanguageField(self.parent_widget)
        self.font_selector = FontSelectors(self.parent_widget)

        self.language_field.sgn_language_changed.connect(
            self._on_language_changed
        )
        self.font_selector.sgn_typo_config_changed.connect(
            self._on_typo_config_changed
        )

        self.font_selector.sgn_typo_panel_was_changed.connect(
            self._on_typo_panel_was_changed
        )

        self.language_container = QtW.QWidget()
        self.language_container.setLayout(self.language_field)

        self.addWidget(self.general_label)
        self.addWidget(self.language_container)
        self.addLayout(self.font_selector)

    def _on_language_changed(self):
        self.sgn_general_config_changed.emit()

    def _on_font_size_changed(self):
        self.sgn_general_config_changed.emit()

    def _on_typo_config_changed(self):
        self.sgn_general_config_changed.emit()

    def _on_typo_panel_was_changed(self):
        self.sgn_general_panel_was_changed.emit()

    def update_sizes(self, config_size):
        default_height = config_size.height() // 10
        default_width = config_size.width()
        self.general_label.setMinimumSize(default_width, default_height)
        self.language_container.setMinimumSize(default_width, default_height)
        self.font_selector.update_size(config_size)
