from PySide6 import QtCore as QtC
from PySide6 import QtGui as QtG

from src.model.translation_handler import _
from src.view_design.custom_widgets.custom_line_edits.simple_field import (
    SimpleField,
)


class NameField(SimpleField):
    """SimpleField for setting the quiz name (max 64 characters)."""

    def __init__(self, default_name):
        super().__init__(
            _("Quiz\nname"),
            default_value=default_name,
            placeholder=_("Set the quiz name to no more than 64 characters"),
        )
        regex = QtC.QRegularExpression(r"^.{0,64}$")
        string_validator = QtG.QRegularExpressionValidator(regex, self)
        self.field_line.setValidator(string_validator)
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 90)
