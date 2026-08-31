from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.quiz_widgets.\
    progress_timer import ProgressTimer
from src.view_design.custom_widgets.quiz_widgets.\
    level_label import LevelLabel


class InfoPanel(QtW.QGridLayout):
    """QGridLayout containing a level label and a vertical progress timer."""

    sgn_timeout = QtC.Signal()

    def __init__(self, actual_level, duration):
        super().__init__()
        self.actual_level = actual_level
        self.duration = duration

        self.level_label = LevelLabel(str(self.actual_level))
        self.level_label.setAlignment(QtC.Qt.AlignmentFlag.AlignCenter)
        self.timer_bar \
            = ProgressTimer(QtC.Qt.Orientation.Vertical, self.duration)
        self.timer_bar.sgn_timeout.connect(self._on_time_out)

        self.addWidget(self.level_label, 0, 0)
        self.addWidget(self.timer_bar, 2, 0)

    def _on_time_out(self):
        self.sgn_timeout.emit()
