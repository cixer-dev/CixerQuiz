from PySide6 import QtWidgets as QtW


class QuizDescriptionPlainText(QtW.QPlainTextEdit):
    """QPlainText that contains the quiz description."""

    def __init__(self, quiz_info):
        self.quiz_description = quiz_info["quiz_description"]
        super().__init__(self.quiz_description)
        self.setReadOnly(True)
