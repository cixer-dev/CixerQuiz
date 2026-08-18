from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW
from src.view_design.custom_widgets.push_buttons.cancel_button \
    import CancelButton
from src.view_design.custom_widgets.push_buttons.ok_button \
    import OkButton

from src.model.translation_handler import _


class WarningMessageBox(QtC.QObject):
    """QMessageBox that displays a warning message with OK and \
    Cancel actions."""

    sgn_ok_pressed = QtC.Signal()

    def __init__(
        self,
        parent_widget,
        message=None,
        title=None,
    ):
        super().__init__()
        self.parent_widget = parent_widget
        self.message = self._build_message(message)
        self.title = self._build_title(title)

    def _build_message(self, message):
        if message:
            return str(message)
        else:
            return _("Are you sure you want to continue?")

    def _build_title(self, title):
        if title:
            return str(title)
        else:
            return _("Warning!")

    def show(self):
        msg_box = QtW.QMessageBox(self.parent_widget)
        msg_box.setWindowTitle(self.title)
        msg_box.setText(self.message)
        msg_box.setIcon(QtW.QMessageBox.Icon.Warning)

        ok_button = OkButton()
        cancel_button = CancelButton()

        msg_box.addButton(ok_button, QtW.QMessageBox.ButtonRole.AcceptRole)
        msg_box.addButton(cancel_button, QtW.QMessageBox.ButtonRole.RejectRole)

        ok_button.pressed.connect(self._on_ok_button_pressed)

        msg_box.exec()

    def _on_ok_button_pressed(self):
        self.sgn_ok_pressed.emit()
