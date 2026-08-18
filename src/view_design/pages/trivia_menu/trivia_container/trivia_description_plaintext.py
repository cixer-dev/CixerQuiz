from PySide6 import QtWidgets as QtW


class TriviaDescriptionPlainText(QtW.QPlainTextEdit):
    """QPlainText that contains the trivia description."""

    def __init__(self, trivia_info):
        self.trivia_description = trivia_info["trivia_description"]
        super().__init__(self.trivia_description)
        self.setReadOnly(True)
