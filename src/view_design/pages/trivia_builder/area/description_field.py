from src.model.translation_handler import _
from src.view_design.custom_widgets.custom_line_edits.simple_field import (
    SimpleField,
)


class DescriptionField(SimpleField):
    """SimpleField for setting the trivia description."""

    def __init__(self, default_description):
        super().__init__(
            _("Trivia\ndescription"),
            default_value=default_description,
            placeholder=_("Set the trivia description here"),
        )
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 90)
