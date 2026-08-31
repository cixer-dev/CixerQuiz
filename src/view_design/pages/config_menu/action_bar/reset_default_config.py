from PySide6 import QtWidgets as QtW

from src.view_design.page_design_toolkit import system_operations_handler
from src.model.translation_handler import _
from src.model.configurators.general_configurator import reset_default_config
from src.view_design.custom_widgets.error_handlers.warning import (
    WarningMessageBox,
)


class ResetDefaultConfig(QtW.QPushButton):
    """QPushButton that warns the user, then resets configuration and restarts\
        the program."""

    def __init__(self, parent_widget):
        self.parent_widget = parent_widget
        super().__init__(
            _("Reset config")
        )
        self.pressed.connect(self._on_warning_reset_config)

    def _on_warning_reset_config(self):
        warning_msg = (
            f"{_('If you reset to default config you will lose all \
                your settings. ')}"
            f"{_('Press OK only if you are sure of your option')}"
        )
        warning_reset_config = WarningMessageBox(
            self.parent_widget,
            warning_msg,
        )
        warning_reset_config.sgn_ok_pressed.connect(self._on_reset_config)
        warning_reset_config.show()

    @staticmethod
    def _on_reset_config():
        reset_default_config.reset_default_config()
        system_operations_handler.restart_program()
