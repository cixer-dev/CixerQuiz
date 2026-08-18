from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.pages.config_menu.config_area.general_config_panel.\
    font_selectors.family_field.brain import FamilyField
from src.view_design.pages.config_menu.config_area.general_config_panel.\
    font_selectors.style_field.brain import StyleField
from src.view_design.page_design_toolkit import cleaner


class FontSelectors(QtW.QVBoxLayout):
    """VBoxLayout that manages font family and style selector sub-panels."""

    sgn_typo_panel_was_changed = QtC.Signal()
    sgn_typo_config_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.family_field = FamilyField(parent_widget)
        self.family_container = QtW.QWidget()
        self.family_container.setLayout(self.family_field)

        self.family_field.sgn_family_changed.connect(self._on_family_changed)
        family_selected = self.family_field.get_selected_family()

        self.style_field = StyleField(self.parent_widget, family_selected)
        self.style_container = QtW.QWidget()
        self.style_container.setLayout(self.style_field)
        self.style_field.sgn_style_changed.connect(self._on_style_changed)

        self.addWidget(self.family_container)
        self.addWidget(self.style_container)

    def _on_family_changed(self, new_family):
        cleaner.clear_container(self.style_container)

        self.style_field = StyleField(self.parent_widget, new_family)
        self.style_field.update_style()
        self.style_container = QtW.QWidget()
        self.style_container.setLayout(self.style_field)
        self.addWidget(self.style_container)

        self.sgn_typo_panel_was_changed.emit()
        self.sgn_typo_config_changed.emit()

    def _on_style_changed(self):
        self.sgn_typo_config_changed.emit()

    def update_size(self, config_size):
        default_height = config_size.height() // 10
        default_width = config_size.width()
        self.family_container.setMinimumSize(default_width, default_height)
        self.style_container.setMinimumSize(default_width, default_height)
