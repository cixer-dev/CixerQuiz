from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.model.translation_handler import _


class OptionsMenu(QtW.QVBoxLayout):
    """A QGridLayout that contains the checkable buttons for to navigate in \
        game options."""

    def __init__(self, page_stack):
        super().__init__()
        self.page_stack = page_stack

        self.trivia_menu_btn = QtW.QPushButton(_("Local trivias"))
        self.trivia_builder_btn = QtW.QPushButton(_("Trivia builder"))
        self.config_menu_btn = QtW.QPushButton(_("Configurations"))
        self.thanks_btn = QtW.QPushButton(_("Thanks and\nContact"))

        self.btns_list = [
            self.trivia_menu_btn,
            self.trivia_builder_btn,
            self.config_menu_btn
        ]

        self.trivia_menu_btn.pressed.connect(self.on_trivia_menu_pressed)
        self.config_menu_btn.pressed.connect(self._on_config_menu_pressed)
        self.thanks_btn.pressed.connect(self._on_thanks_btn_pressed)
        self.trivia_builder_btn.pressed.connect(
            self._on_trivia_builder_pressed
            )

        for btn in self.btns_list:
            self.setAlignment(
                QtC.Qt.AlignmentFlag.AlignLeft | QtC.Qt.AlignmentFlag.AlignTop)
            btn.setCheckable(True)
            self.addWidget(btn)

        self._disable_btns_checkable_status(self.trivia_menu_btn)

    def press_trivia_menu_btn(self):
        self._disable_btns_checkable_status(self.trivia_menu_btn)

    def on_trivia_menu_pressed(self):
        self._disable_btns_checkable_status(self.trivia_menu_btn)
        self.page_stack.switch_to_trivia_menu()

    def _on_config_menu_pressed(self):
        self._disable_btns_checkable_status(self.config_menu_btn)
        self.page_stack.switch_to_config_menu()

    def _on_thanks_btn_pressed(self):
        self._disable_btns_checkable_status(self.thanks_btn)
        self.page_stack.switch_to_thanks_and_contact_menu()

    def _on_trivia_builder_pressed(self):
        self._disable_btns_checkable_status(self.trivia_builder_btn)
        self.page_stack.switch_to_trivia_builder()

    def _disable_btns_checkable_status(self, new_current_btn):
        for btn in self.btns_list:
            if btn == new_current_btn:
                btn.setChecked(True)
            else:
                btn.setChecked(False)
            btn.update()
