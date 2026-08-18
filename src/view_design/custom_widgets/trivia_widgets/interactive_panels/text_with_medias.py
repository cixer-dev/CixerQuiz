from src.view_design.custom_widgets.trivia_widgets.interactive_panels.brain \
    import InteractivePanelTemplate


class InteractivePanelTextWithMedias(InteractivePanelTemplate):
    """Interactive panel template with text question and media answer areas."""

    def __init__(self, question_panel, answer_panel):
        super().__init__(
            question_panel,
            answer_panel,
            row_question_proportion=20,
            row_space_proportion=10,
            row_answer_proportion=70
        )
