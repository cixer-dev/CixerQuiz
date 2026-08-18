from PySide6 import QtWidgets as QtW, QtGui as QtG

from src.model.configurators.assets_paths_configurator import \
    assets_paths_reader
from src.model.configurators.general_configurator import general_reader


def set_font_configuration(app: QtW.QApplication):
    """Set application font and stylesheet configuration."""
    font_family = general_reader.read_general_config("font_family")
    font_style_text = general_reader.read_general_config("font_style")
    font = QtG.QFont(font_family)
    font.setStyleName(font_style_text)
    qss_path = assets_paths_reader.read_asset_path("current_qss_style_path")

    with open(qss_path, "r") as qss_file:
        app.setStyleSheet(qss_file.read())
    app.setFont(font)
