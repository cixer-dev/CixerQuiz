import webbrowser

from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.model.translation_handler import _
from src.model.configurators.general_configurator import general_reader
from src.view_design.custom_widgets.push_buttons.\
    standard_button_with_icon import StandardButtonWithIcon


class ContactMe(QtW.QWidget):
    def __init__(self):
        super().__init__()
        self.container_layout = QtW.QGridLayout()

        self.contact_msg \
            = _("If you want to reach me, check my GitHub "
                "information")
        self.header_plaintext \
            = QtW.QPlainTextEdit(self.contact_msg)
        self.header_plaintext.setObjectName("TransparentPlaintext")
        self.header_plaintext.setReadOnly(True)
        self.header_plaintext.setVerticalScrollBarPolicy(
            QtC.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.header_plaintext.setHorizontalScrollBarPolicy(
            QtC.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.github_logo \
            = StandardButtonWithIcon("github_logo", icon_percent=1.0)
        self.github_logo.setObjectName("StaticBtn")
        self.github_logo.pressed.connect(self._open_github)

        self.container_layout.addWidget(
            self.github_logo,
            0,
            0
        )
        self.container_layout.addWidget(self.header_plaintext, 0, 1)

        self.container_layout.setColumnStretch(0, 20)
        self.container_layout.setColumnStretch(1, 80)

        self.setLayout(self.container_layout)

    def _open_github(self):
        github_user_url = general_reader.read_general_config("github_repo_url")
        webbrowser.open(github_user_url)

    def _update_github_logo(self):
        self.github_logo.setMaximumHeight(self.height()//2)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_github_logo()
