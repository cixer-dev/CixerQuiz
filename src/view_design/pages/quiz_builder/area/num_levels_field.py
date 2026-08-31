from src.model.translation_handler import _
from src.view_design.custom_widgets.custom_line_edits.\
    field_whit_spin_box import FieldWithSpinBox


class NumLevelsField(FieldWithSpinBox):
    """FieldWithSpinBox for setting the number of quiz levels."""

    def __init__(self, default_num_levels_field):
        super().__init__(
            _("Number of\nlevels"),
            default_value=default_num_levels_field,
        )
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 90)
