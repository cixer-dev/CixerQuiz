from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.pages.config_menu.config_area.general_config_panel.\
    font_selectors.family_field.family_selector import FamilySelector


class FamilyField(QtW.QGridLayout):
    """QGridLayout containing a font family label and selector."""

    sgn_family_changed = QtC.Signal(str)

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.family_label = QtW.QLabel(_("Font family") + ":")
        self.family_selector = FamilySelector(self.parent_widget)
        self.family_selector.sgn_family_changed.connect(
            self.sgn_family_changed
        )

        self.addWidget(self.family_label, 0, 0)
        self.addWidget(self.family_selector, 0, 1)
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 20)
        self.setColumnStretch(1, 80)

    def get_selected_family(self):
        return self.family_selector.family_selected

    def update_size(self, config_size):
        default_height = config_size.height() // 10
        default_width = config_size.width()
        self.family_label.setMinimumSize(default_width, default_height)
        self.family_selector.setMinimumSize(default_width, default_height)
