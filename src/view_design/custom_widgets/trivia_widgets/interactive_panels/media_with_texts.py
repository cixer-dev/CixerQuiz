from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    brain import InteractivePanelTemplate


class InteractivePanelMediaWithTexts(InteractivePanelTemplate):
    """QGridLayout interactive panel template with media question and \
        text answer areas."""

    def __init__(self, question_panel, answer_panel):
        super().__init__(
            question_panel,
            answer_panel,
            row_question_proportion=60,
            row_space_proportion=10,
            row_answer_proportion=30
        )
