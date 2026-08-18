from src.model.translation_handler import _
from src.view_design.custom_widgets.custom_line_edits.field_whit_spin_box \
    import FieldWithSpinBox


class NumPossibleQuestionsField(FieldWithSpinBox):
    """FieldWithSpinBox default_field to select the number of possible \
        questions."""

    def __init__(self, num_possible_questions):
        super().__init__(
            _("Possible\nquestions"),
            default_value=num_possible_questions,
        )
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 90)
