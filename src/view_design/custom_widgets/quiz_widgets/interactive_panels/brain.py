from PySide6 import QtWidgets as QtW


class InteractivePanelTemplate(QtW.QGridLayout):
    """QGridLayout template that places a question text panel and \
        an answer panel."""

    def __init__(self,
                 question_panel,
                 answer_panel,
                 row_question_proportion,
                 row_space_proportion,
                 row_answer_proportion):
        super().__init__()
        self.question_panel = question_panel
        self.answer_panel = answer_panel
        self.row_question_proportion = row_question_proportion
        self.row_space_proportion = row_space_proportion
        self.row_answer_proportion = row_answer_proportion

        self.addWidget(self.question_panel, 0, 1)
        self.addWidget(self.answer_panel, 2, 1)

        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 80)
        self.setColumnStretch(2, 10)

        self.setRowStretch(0, row_question_proportion)
        self.setRowStretch(1, row_space_proportion)
        self.setRowStretch(2, row_answer_proportion)
