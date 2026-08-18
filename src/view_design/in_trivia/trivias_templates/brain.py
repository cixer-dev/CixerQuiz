from typing import Any

from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.trivia_widgets.info_panels.\
    brain import InfoPanel
from src.view_design.page_design_toolkit import expander


class TriviaLevelTemplate(QtW.QWidget):
    """Template panel for trivia level questions with video answers.

    Provides an info panel and an interactive area, emits timeout and answer
    correctness signals, and manages the layout proportions and expansion.
    """

    sgn_resized = QtC.Signal()
    sgn_pressed_answer_is_correct = QtC.Signal()
    sgn_pressed_answer_is_incorrect = QtC.Signal(dict)
    sgn_timeout = QtC.Signal()

    def __init__(
        self,
        data_for_display: dict[str, Any]
            ):
        super().__init__()
        self.data = data_for_display
        self.correct_answer = self.data["correct_answer"]
        self.duration = self.data["trivia_duration"]
        self.actual_level = self.data["actual_level"]

        self.container_layout = QtW.QGridLayout()
        self.question_panel = None
        self.answer_panel = None
        self.interactive_panel = None
        self.info_panel = InfoPanel(self.actual_level, self.duration)
        self.info_panel.sgn_timeout.connect(self._on_timeout)
        self.setLayout(self.container_layout)

        self.col_to_proportion = {
            "0": 10,
            "1": 10,
            "2": 10,
            "3": 60,
            "4": 10
        }
        self.interactive_panel_col_proportion \
            = self._get_interactive_panel_col_proportion()

    def _on_timeout(self):
        self.sgn_timeout.emit()

    def _get_interactive_panel_col_proportion(self):
        return self.col_to_proportion["3"]

    def _build_interactive_panel(self):
        self.sgn_resized.connect(self._build_question_panel)
        self.sgn_resized.connect(self._build_answers_panel)
        self._build_question_panel()
        self._build_answers_panel()
        self._connect_answers_signals()
        self._update_graphics()

    def _build_question_panel(self):
        if not self.question_panel:
            raise AttributeError(
                "question_panel has not been initialized. "
                "Ensure the question_panel is set before calling \
                _build_question_panel()."
            )
        if not self.interactive_panel:
            raise AttributeError(
                "interactive_panel has not been initialized. "
                "Ensure the question_panel is set before calling"
            )
        else:
            max_width_size \
                = self.width() * self.interactive_panel_col_proportion // 100
            max_height_size \
                = self.height() \
                * self.interactive_panel.row_question_proportion // 100
            self.question_panel.setMaximumSize(
                max_width_size,
                max_height_size
            )

    def _build_answers_panel(self):
        if not self.answer_panel:
            raise AttributeError(
                "answer_panel has not been initialized. "
                "Ensure the question_panel is set before calling")
        if not self.interactive_panel:
            raise AttributeError(
                "interactive_panel has not been initialized. "
                "Ensure the question_panel is set before calling"
            )
        else:
            max_width_size \
                = self.width() * self.interactive_panel_col_proportion // 100
            max_height_size \
                = self.height() \
                * self.interactive_panel.row_answer_proportion // 100
            self.answer_panel.setMaximumSize(
                max_width_size,
                max_height_size
            )

    def _connect_answers_signals(self):
        if not self.answer_panel:
            raise AttributeError(
                "answer_panel has not been initialized. "
                "Ensure _build_answers_panel() is called before connecting \
                signals."
            )
        else:
            self.answer_panel.sgn_pressed_answer_is_correct.connect(
                self.sgn_pressed_answer_is_correct
            )
            self.answer_panel.sgn_pressed_answer_is_incorrect.connect(
                self.sgn_pressed_answer_is_incorrect
            )

    def _update_graphics(self):
        self._build_container_layout()
        self._set_column_proportion(self.interactive_panel_col_proportion)
        self._set_row_proportion()
        expander.expand_layout(self.container_layout)

    def _build_container_layout(self):
        if not self.interactive_panel:
            raise AttributeError(
                "interactive_panel has not been initialized. "
                "Ensure the question_panel is set before calling"
            )
        else:
            self.container_layout.addLayout(self.info_panel, 1, 1)
            self.container_layout.addLayout(self.interactive_panel, 1, 3)

    def _set_column_proportion(self, interactive_panel_col_proportion):
        self.container_layout.setColumnStretch(0, 10)
        self.container_layout.setColumnStretch(1, 10)
        self.container_layout.setColumnStretch(2, 10)
        self.container_layout.setColumnStretch(
            3,
            interactive_panel_col_proportion
            )
        self.container_layout.setColumnStretch(4, 10)

    def _set_row_proportion(self):
        self.container_layout.setRowStretch(0, 5)
        self.container_layout.setRowStretch(1, 90)
        self.container_layout.setRowStretch(2, 5)

    def _change_interactive_panel_distribution(self):
        self.col_to_proportion["2"] = 30
        self.col_to_proportion["3"] = 40
        self.interactive_panel_col_proportion \
            = self._get_interactive_panel_col_proportion()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.sgn_resized.emit()
