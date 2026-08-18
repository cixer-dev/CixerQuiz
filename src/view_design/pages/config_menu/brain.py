from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.error_handlers.\
    warning_without_cancel_button import WarningWithoutCancelButtonMessageBox
from src.model.translation_handler import _
from src.view_design.page_design_toolkit \
    import expander, system_operations_handler
from src.view_design.pages.config_menu.action_bar.brain import ConfigActionBar
from src.view_design.pages.config_menu.config_area.brain import ConfigArea


class ConfigMenu(QtW.QWidget):
    """Stacked trivia widget that hosts the configuration area \
    and action bar."""

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.grid_container = QtW.QGridLayout()

        self.config_area = ConfigArea(self.parent_widget)
        self.config_action_bar = ConfigActionBar(self.parent_widget)

        self.config_action_bar.sgn_save_btn_pressed.connect(
            self._on_reset_warning
        )

        self.grid_container.addWidget(self.config_area, 0, 0)
        self.grid_container.addLayout(self.config_action_bar, 1, 0)
        self.setLayout(self.grid_container)

        expander.expand_layout(self.grid_container)
        self._set_row_proportion()

    def _on_reset_warning(self):
        self.reset_warning = WarningWithoutCancelButtonMessageBox(
            self.parent_widget,
            _(
                "For the changes to apply correctly, the program needs to be "
                "reset. "
                "Press OK to continue."
            )
        )
        self.reset_warning.sgn_ok_pressed.connect(self._on_reset_program)
        self.reset_warning.show()

    @staticmethod
    def _on_reset_program():
        system_operations_handler.reset_program()

    def _set_row_proportion(self):
        self.grid_container.setRowStretch(0, 90)
        self.grid_container.setRowStretch(1, 10)
