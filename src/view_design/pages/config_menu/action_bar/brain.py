from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC
from src.model.translation_handler import _
from src.view_design.pages.config_menu.action_bar.reset_default_config \
    import ResetDefaultConfig


class ConfigActionBar(QtW.QGridLayout):
    """QGridLayout action bar for the application actions."""
    sgn_save_btn_pressed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.save_changes_btn = QtW.QPushButton(_("Save changes"))
        self.save_changes_btn.setObjectName("action_btn")
        self.save_changes_btn.pressed.connect(self.sgn_save_btn_pressed.emit)

        self.reset_default_config = ResetDefaultConfig(self.parent_widget)
        self.addWidget(self.save_changes_btn, 0, 1)
        self.addWidget(self.reset_default_config, 0, 3)
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 20)
        self.setColumnStretch(1, 20)
        self.setColumnStretch(2, 20)
        self.setColumnStretch(3, 20)
        self.setColumnStretch(4, 20)
