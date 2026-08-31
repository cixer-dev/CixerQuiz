from PySide6 import QtWidgets as QtW


class QPOnlyPlaintext(QtW.QPlainTextEdit):
    """A QPlaintext widget that containing a single question text."""

    def __init__(self, question_text):
        super().__init__(question_text)
        self.setReadOnly(True)
