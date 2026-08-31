from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.push_buttons.ok_button \
    import OkButton

from src.model.translation_handler import _


class WarningWithoutCancelButtonMessageBox(QtC.QObject):
    """QMessageBox that displays a warning message with only an OK action."""

    sgn_ok_pressed = QtC.Signal()

    def __init__(
        self,
        parent_widget,
        message,
        title=None,
    ):
        super().__init__()
        self.parent_widget = parent_widget
        self.is_visible = False
        self.message = str(message)
        self.title = self._build_title(title)

    def _build_title(self, title):
        if not title:
            return _("Warning!")
        else:
            return title

    def show(self):
        if not self.is_visible:
            msg_box = QtW.QMessageBox(self.parent_widget)
            msg_box.setWindowTitle(self.title)
            msg_box.setText(self.message)
            msg_box.setIcon(QtW.QMessageBox.Icon.Warning)

            ok_button = OkButton()
            msg_box.addButton(ok_button, QtW.QMessageBox.ButtonRole.AcceptRole)

            ok_button.pressed.connect(self._on_ok_button_pressed)

            msg_box.exec()
            self.is_visible = True

    def _on_ok_button_pressed(self):
        self.sgn_ok_pressed.emit()
