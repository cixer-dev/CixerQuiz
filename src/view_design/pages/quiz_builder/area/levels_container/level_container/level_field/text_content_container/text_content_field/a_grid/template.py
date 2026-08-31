from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.page_design_toolkit import expander
from src.view_design.pages.quiz_builder.area.levels_container\
    .level_container.level_field.text_content_container.\
    text_content_field.a_grid.individual_a.template \
    import AnswerField


class AnswerGridField(QtW.QGridLayout):
    """AnswerGridField template for managing multiple answers."""

    sgn_num_answers_changed = QtC.Signal(int)
    sgn_answer_content_changed = QtC.Signal(list)

    def __init__(self, parent_widget, num_answers):
        super().__init__()

        self.parent_widget = parent_widget
        self.num_answers = num_answers

        self.answers = []
        self.answers_containers = []
        expander.expand_layout(self)

    def _build_answer_field_connections(
            self,
            answer_field: AnswerField,
            answer_index
            ):
        answer_field.sgn_remove_answer.connect(
            lambda: self._on_remove_answer(self.num_answers)
        )
        answer_field.sgn_add_answer.connect(
            lambda: self.on_add_answer(self.num_answers + 1)
        )
        answer_field.sgn_answer_content_changed.connect(
            lambda new_answer_content, idx=answer_index:
            self._on_answer_content_changed(
                new_answer_content,
                idx,
            )
        )

    def _append_answer_in_container(self, answer_field, answer_index):
        answer_container_field = QtW.QWidget()
        answer_container_field.setLayout(answer_field)
        self.addWidget(answer_container_field, answer_index, 0)
        self.answers_containers.append(answer_container_field)

    def update_answers_size(self, tb_area_size):
        answers_container_width = tb_area_size.width()
        answers_container_height = tb_area_size.height() // 10
        for answer_container in self.answers_containers:
            answer_container.setMaximumWidth(answers_container_width)
            answer_container.setFixedHeight(answers_container_height)

    def _on_answer_content_changed(self, new_answer_content, answer_index):
        self._handler_length_list(self.answers, answer_index)
        self.answers[answer_index] = new_answer_content
        self.sgn_answer_content_changed.emit(self.answers)

    def on_add_answer(self, num_answers):
        self.sgn_num_answers_changed.emit(num_answers)

    def _on_remove_answer(self, num_answers):
        if num_answers > 2:
            self.num_answers -= 1
            self.sgn_num_answers_changed.emit(self.num_answers)

    def get_answer_content_changed_signal(self):
        return self.sgn_answer_content_changed

    @staticmethod
    def _handler_length_list(array, index):
        if len(array) <= index:
            needed_list_positions = index - len(array) + 1
            array.extend([{}] * needed_list_positions)
