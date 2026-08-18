from src.model.translation_handler import _
from src.view_design.custom_widgets.custom_line_edits.field_whit_spin_box \
    import FieldWithSpinBox


class DurationField(FieldWithSpinBox):
    """FieldWithSpinBox for setting trivia duration in seconds."""

    def __init__(self, default_duration):
        super().__init__(
            _("Trivia level\nduration"),
            default_value=default_duration,
        )
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 90)
