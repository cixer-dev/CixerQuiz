from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class CompleteOperationMessageBox(QtC.QObject):
    """A QMessageBox wrapper emitting a signal when the user accepts."""

    sgn_accepted_ok = QtC.Signal(str)

    def __init__(
        self,
        parent_widget,
        message,
        title=None,
    ):
        super().__init__()
        self.parent_widget = parent_widget
        self.message = message
        self.title = self._build_title(title)

    def _build_title(self, title):
        if title:
            return str(title)
        else:
            return _("Operation complete")

    def show(self):
        msg_box = QtW.QMessageBox(self.parent_widget)
        msg_box.setWindowTitle(self.title)
        msg_box.setText(self.message)
        msg_box.setIcon(QtW.QMessageBox.Icon.Information)

        ok_button = msg_box.addButton(
            "OK",
            QtW.QMessageBox.ButtonRole.AcceptRole,
        )
        ok_button.clicked.connect(self._on_button_clicked)
        msg_box.exec()

    def _on_button_clicked(self):
        self.sgn_accepted_ok.emit(str)

    def _update_message(self, new_message):
        self.message = new_message
