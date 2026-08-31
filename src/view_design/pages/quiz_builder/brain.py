from PySide6 import QtWidgets as QtW

from src.model.quiz_builder.brain import QuizBuilder
from src.view_design.custom_widgets.complete_operation_alert import (
    CompleteOperationMessageBox,
)
from src.view_design.custom_widgets.error_handlers.error_alert import (
    ErrorMessageBox,
)
from src.view_design.page_design_toolkit import expander
from src.view_design.pages.quiz_builder.action_bar import BuilderActionBar
from src.view_design.pages.quiz_builder.area.brain import (
    QuizBuilderArea,
)


class QuizBuilderMenu(QtW.QWidget):
    """QWidget menu that builds quiz and emits completion/errors."""

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.container_grid = QtW.QGridLayout()

        self.quiz_manifest_content = {}
        self.levels_data = []

        self.quiz_builder_area = QuizBuilderArea(self.parent_widget)
        self.quiz_ops_bar = BuilderActionBar(self.parent_widget)

        self.quiz_builder_area.sgn_manifest_data_changed.connect(
            self._on_quiz_manifest_data_changed
        )
        self.quiz_builder_area.sgn_levels_data_changed.connect(
            self._on_levels_data_changed
        )

        self.quiz_ops_bar.sgn_confirmed_selection.connect(
            self._on_confirmed_selection
        )

        self.container_grid.addWidget(self.quiz_builder_area, 0, 0)
        self.container_grid.addLayout(self.quiz_ops_bar, 1, 0)

        self._set_row_proportions()
        expander.expand_layout(self.container_grid)

        self.setLayout(self.container_grid)

    def _on_levels_data_changed(self, new_levels_data):
        self.levels_data = new_levels_data

    def _on_quiz_manifest_data_changed(self, new_quiz_manifest_content):
        self.quiz_manifest_content = new_quiz_manifest_content

    def _on_confirmed_selection(self):
        try:
            self.build_quiz_files()
            complete_operation_complete_message_box \
                = CompleteOperationMessageBox(
                    self.parent_widget,
                    "The quiz was made correctly",
                )
            complete_operation_complete_message_box.sgn_accepted_ok.connect(
                self._on_accepted_message
            )
            complete_operation_complete_message_box.show()
        except Exception as msg:
            error_message_box_widget = ErrorMessageBox(
                self.parent_widget,
                message=msg,
            )
            error_message_box_widget.sgn_accepted.connect(
                self._on_accepted_message
            )
            error_message_box_widget.show()

    def _on_accepted_message(self):
        self.parent_widget.switch_to_quiz_menu()

    def build_quiz_files(self):
        quiz_builder = QuizBuilder(
            self.quiz_manifest_content,
            self.levels_data
        )
        quiz_builder.build_quiz()

    def _print_debug(self):
        if self.levels_data:
            for level in self.levels_data:
                for header, data in level.items():
                    print(f"\n: {header}:{data}\n")

    def _set_row_proportions(self):
        self.container_grid.setRowStretch(0, 90)
        self.container_grid.setRowStretch(1, 10)
