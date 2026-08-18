from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC


def move_up_to_down(widget: QtW.QWidget, travel=None):
    """Animates a widget moving vertically down and back up continuously."""
    initial_pos = widget.pos()
    if travel is None:
        travel = 10
    pos_down = get_down_pos(initial_pos, travel)
    pos_up = get_up_pos(initial_pos, travel)
    duration_in_ms = 1500

    a1 = QtC.QPropertyAnimation(widget, b"pos")
    a1.setDuration(duration_in_ms)
    a1.setEasingCurve(QtC.QEasingCurve.Type.InOutSine)
    a1.setStartValue(pos_up)
    a1.setEndValue(pos_down)

    a2 = QtC.QPropertyAnimation(widget, b"pos")
    a2.setDuration(duration_in_ms)
    a2.setEasingCurve(QtC.QEasingCurve.Type.InOutSine)
    a2.setStartValue(pos_down)
    a2.setEndValue(pos_up)

    group = QtC.QSequentialAnimationGroup(widget)
    group.addAnimation(a1)
    group.addAnimation(a2)
    group.setLoopCount(-1)
    group.start()


def get_down_pos(initial_pos, travel):
    return QtC.QPoint(initial_pos.x(), initial_pos.y() - travel)


def get_up_pos(initial_pos, travel):
    return QtC.QPoint(initial_pos.x(), initial_pos.y() + travel)
