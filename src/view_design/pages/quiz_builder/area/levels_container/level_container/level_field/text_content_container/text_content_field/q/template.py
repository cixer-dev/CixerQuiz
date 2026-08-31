from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.custom_widgets.custom_line_edits.simple_field import (
    SimpleField,
)


class QuestionField(QtW.QGridLayout):
    """QGridLayout template for the answer fields."""

    sgn_question_content_changed = QtC.Signal(dict)

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.question = ""
        self.question_field = SimpleField(_("Question\ntext"))
