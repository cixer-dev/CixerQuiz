import sys

from PySide6 import QtWidgets as QtW

from src.view_design.page_manager.brain import MainStack
from src.view_design.general_app_configurator.global_filter \
    import GlobalFilter
from src.view_design.general_app_configurator \
    import font_configurator


app = QtW.QApplication(sys.argv)
global_filter = GlobalFilter(app)
app.installEventFilter(global_filter)
font_configurator.set_font_configuration(app)
main_window = MainStack()
main_window.showFullScreen()
sys.exit(app.exec())
