from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class LossReasonExplanationPlaintext(QtW.QPlainTextEdit):
    """QPlaintext text that displays the correct answer explanation."""

    def __init__(self, question: str, correct_answer):
        text = _("The correct answer to: ") + "'" + question + \
            "'" + _(" is: ") + "'" + correct_answer + "'"
        super().__init__(text)
        self.setReadOnly(True)
