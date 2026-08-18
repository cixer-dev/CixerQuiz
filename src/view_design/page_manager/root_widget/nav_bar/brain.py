from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.page_manager.root_widget.nav_bar.options_menu \
    import OptionsMenu
from src.view_design.custom_widgets.containers.standard \
    import StandardContainer
from src.view_design.page_manager.root_widget.nav_bar.branding_widget \
    import BrandingWidget
from src.view_design.page_manager.root_widget.nav_bar.contact_me \
    import ContactMe


class NavBar(QtW.QWidget):
    """QWidget that contains the branding widget and options buttons"""
    def __init__(self, page_stack):
        super().__init__()

        self.page_stack = page_stack

        self.branding_widget = BrandingWidget()
        self.contact_me = ContactMe()
        self.options = OptionsMenu(self.page_stack)
        self.options_container = StandardContainer(layout_inside=self.options)

        self.container_layout = QtW.QVBoxLayout()
        self.container_layout.setAlignment(QtC.Qt.AlignmentFlag.AlignTop)

        self.container_layout.addWidget(
            self.branding_widget,
            QtC.Qt.AlignmentFlag.AlignTop
            )
        self.container_layout.addWidget(
            self.contact_me,
            QtC.Qt.AlignmentFlag.AlignTop
            )
        self.container_layout.addWidget(
            self.options_container,
            QtC.Qt.AlignmentFlag.AlignTop
            )

        self.setLayout(self.container_layout)

    def update_btns_size(self, total_width, total_height):
        default_width = total_width
        self.branding_widget.setMaximumSize(
            default_width,
            total_height * 0.3
            )
        self.options_container.setMaximumSize(
            default_width,
            total_height * 0.3
            )
        self.contact_me.setMaximumSize(
            default_width,
            total_height * 0.2
            )

    def press_on_trivia_menu_btn(self):
        self.options.press_trivia_menu_btn()
