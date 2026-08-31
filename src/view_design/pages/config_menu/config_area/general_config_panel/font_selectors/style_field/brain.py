from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.pages.config_menu.config_area.general_config_panel.\
    font_selectors.style_field.style_selector import StyleSelector


class StyleField(QtW.QGridLayout):
    """QGridLayout" containing a font style label and selector."""

    sgn_style_changed = QtC.Signal()

    def __init__(self, parent_widget, family):
        super().__init__()

        self.parent_widget = parent_widget
        self.family = family

        self.style_label = QtW.QLabel(_("Font style") + ":")
        self.style_selector = StyleSelector(self.parent_widget, self.family)
        self.style_selector.sgn_style_changed.connect(
            self.sgn_style_changed.emit
        )

        self.addWidget(self.style_label, 0, 0)
        self.addWidget(self.style_selector, 0, 1)

        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 20)
        self.setColumnStretch(1, 80)

    def update_style(self):
        self.style_selector.update_style()

    def update_size(self, config_size):
        default_height = config_size.height() // 10
        default_width = config_size.width()
        self.style_label.setMinimumSize(default_width, default_height)
        self.style_selector.setMinimumSize(default_width, default_height)
