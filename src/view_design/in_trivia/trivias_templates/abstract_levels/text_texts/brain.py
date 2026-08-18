from src.view_design.in_trivia.trivias_templates.brain \
    import TriviaLevelTemplate
from src.view_design.custom_widgets.trivia_widgets.answers_panel.only_label \
    import APOnlyLabel
from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    text_with_texts import InteractivePanelTextWithTexts
from src.view_design.custom_widgets.trivia_widgets.question_panel.\
    only_plaintext import QPOnlyPlaintext


class TriviaLevelsTextTexts(TriviaLevelTemplate):
    """Trivia level with text-based widgets for question and answer panels."""

    def __init__(
        self,
        data_for_display
            ):
        super().__init__(data_for_display)

        self.question = data_for_display["question"]
        self.answers = data_for_display["answers"]
        self.correct_answer = data_for_display["correct_answer"]

        self.question_panel = QPOnlyPlaintext(self.question)
        self.answer_panel = APOnlyLabel(
            self.answers, self.correct_answer, self.question
        )
        self.interactive_panel = InteractivePanelTextWithTexts(
            self.question_panel,
            self.answer_panel
        )
        self._change_interactive_panel_distribution()
        self._build_interactive_panel()
