from src.view_design.in_quiz.quizzes_templates.brain \
    import QuizLevelTemplate
from src.view_design.custom_widgets.quiz_widgets.answers_panel.only_label \
    import APOnlyLabel
from src.view_design.custom_widgets.quiz_widgets.interactive_panels.\
    text_with_texts import InteractivePanelTextWithTexts
from src.view_design.custom_widgets.quiz_widgets.question_panel.\
    only_plaintext import QPOnlyPlaintext


class QuizLevelsTextTexts(QuizLevelTemplate):
    """Quiz level with text-based widgets for question and answer panels."""

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
