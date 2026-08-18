from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.view_design.custom_widgets.custom_line_edits.simple_field import (
    SimpleField,
)
from src.view_design.custom_widgets.push_buttons.delete_button \
    import DeleteButton
from src.view_design.custom_widgets.push_buttons.add_button import AddButton


class AnswerField(QtW.QGridLayout):
    """QGridLayout template for an answer text default field."""

    sgn_add_answer = QtC.Signal()
    sgn_remove_answer = QtC.Signal()
    sgn_answer_content_changed = QtC.Signal(object)

    def __init__(
        self,
        parent_widget,
        answer_title=None
            ):
        super().__init__()
        self.parent_widget = parent_widget
        self.answer_title = self._build_answer_title(answer_title)
        self.answer_text = ""
        self.answer_text_field = SimpleField(self.answer_title)

        self.answer_text_field.sgn_field_content_changed.connect(
            self.on_answer_text_changed
        )

        self.add_answer_btn = AddButton()
        self.delete_answer_btn = DeleteButton()

        self.add_answer_btn.pressed.connect(self.on_add_answer)
        self.delete_answer_btn.pressed.connect(self.on_delete_answer)

    def _build_answer_title(self, answer_title):
        if answer_title:
            return answer_title
        else:
            return _("Answer\ntext")

    def on_add_answer(self):
        self.sgn_add_answer.emit()

    def on_delete_answer(self):
        self.sgn_remove_answer.emit()

    def on_answer_text_changed(self, answer_text):
        self.answer_text = answer_text
        self.sgn_answer_content_changed.emit(self.answer_text)
