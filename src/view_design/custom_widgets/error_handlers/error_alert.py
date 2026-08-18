import traceback

from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.model.translation_handler import _


class ErrorMessageBox(QtC.QObject):
    """QMessageBox that displays a critical error message and emits a signal \
    when sgn_accepted."""

    sgn_accepted = QtC.Signal()

    def __init__(
        self,
        parent_widget,
        message,
        title=None,
    ):
        super().__init__()
        self.parent_widget = parent_widget
        self.message = self._build_msg(message)
        self.title = self._build_title(title)

    def _build_msg(self, msg):
        if msg:
            if isinstance(msg, str):
                return msg
            elif isinstance(msg, Exception):
                return traceback.format_exc(limit=0)
            else:
                return str(msg)
        else:
            return _("A critical error occurred")

    def _build_title(self, title):
        if title:
            return title
        else:
            return _("An error occurred")

    def show(self):
        msg_box = QtW.QMessageBox(self.parent_widget)
        msg_box.setWindowTitle(self.title)
        msg_box.setText(self.message)
        msg_box.setIcon(QtW.QMessageBox.Icon.Critical)
        ok_button \
            = msg_box.addButton("OK", QtW.QMessageBox.ButtonRole.AcceptRole)
        ok_button.clicked.connect(self._on_button_clicked)
        msg_box.exec()

    def _on_button_clicked(self):
        self.sgn_accepted.emit()
