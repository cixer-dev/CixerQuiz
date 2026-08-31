from PySide6 import QtWidgets as QtW


class QuizNameLabel(QtW.QLabel):
    """QLabel that contains the quiz name."""

    def __init__(self, quiz_info):
        self.quiz_name = quiz_info["quiz_name"]
        super().__init__(self.quiz_name)
