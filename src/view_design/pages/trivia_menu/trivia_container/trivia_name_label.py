from PySide6 import QtWidgets as QtW


class TriviaNameLabel(QtW.QLabel):
    """QLabel that contains the trivia name."""

    def __init__(self, trivia_info):
        self.trivia_name = trivia_info["trivia_name"]
        super().__init__(self.trivia_name)
