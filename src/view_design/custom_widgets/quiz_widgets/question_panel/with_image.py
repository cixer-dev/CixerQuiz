from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.quiz_widgets.\
    image_label import ImageLabel
from src.view_design.custom_widgets.quiz_widgets.\
    question_panel.only_plaintext import QPOnlyPlaintext


class QPWithImage(QtW.QWidget):
    """A widget that displays a question_text and an associated image."""

    def __init__(self, question_to_image_path):
        super().__init__()
        self.grid_container = QtW.QGridLayout()
        for question, image_path in question_to_image_path.items():
            self.question, self.image_path = question, image_path

        question_label = QPOnlyPlaintext(self.question)

        self.question_image_label = ImageLabel(self.image_path)

        self.grid_container.addWidget(question_label, 0, 0)
        self.grid_container.addWidget(self.question_image_label, 1, 0)

        self.setLayout(self.grid_container)

        self.grid_container.setRowStretch(0, 20)
        self.grid_container.setRowStretch(1, 80)

    def update_image_label(self):
        self.question_image_label._update_image_size()
