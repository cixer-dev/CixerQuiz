from typing import Optional

from PySide6 import QtCore as QtC
from PySide6 import QtGui as QtG
from PySide6 import QtSvgWidgets as QtS
from PySide6 import QtWidgets as QtW

from src.model.configurators.assets_paths_configurator import \
    assets_paths_reader
from src.view_design.custom_animations.transition.\
    loading_plaintext import LoadingPlaintext
from src.view_design.custom_animations.transition.\
    optional_msg_plaintext import OptionalMsgPlaintext


class SceneTransition(QtW.QWidget):
    """QWidget loading spinner with a rotation animation."""
    sgn_timeout = QtC.Signal()

    def __init__(
        self,
        parent_stack: QtW.QStackedWidget,
        optional_msg: Optional[str] = None,
        duration: Optional[int] = None
    ):
        super().__init__()
        self.parent_stack = parent_stack
        self.optional_msg = optional_msg
        self.icon_path = assets_paths_reader.read_asset_path(
            "star_logo"
        )
        self.duration = self._build_duration(duration)

        self.container_layout = QtW.QGridLayout()
        self.loading_plaintext = self._build_loading_plaintext()

        self.graphic_object = QtW.QGraphicsView()
        self.scene = QtW.QGraphicsScene()
        self.svg_item = QtS.QGraphicsSvgItem(self.icon_path)

        self.svg_item.setTransformOriginPoint(
            self.svg_item.boundingRect().center()
        )
        self.scene.addItem(self.svg_item)
        self.graphic_object.setScene(self.scene)
        self.graphic_object.setSceneRect(self.svg_item.boundingRect())

        self.rotation_animation = QtC.QVariantAnimation()
        self.rotation_animation.setDuration(self.duration)
        self.rotation_animation.setStartValue(0)
        self.rotation_animation.setEndValue(360)
        self.rotation_animation.valueChanged.connect(
            self._on_rotation_changed
        )
        self.rotation_animation.finished.connect(self.sgn_timeout.emit)

        self._set_column_proportion()
        self._set_row_proportion()

        self.container_layout.addWidget(self.graphic_object, 1, 1)
        self.container_layout.addWidget(self.loading_plaintext, 2, 1)
        self.setLayout(self.container_layout)

        self.parent_stack.addWidget(self)
        self.parent_stack.setCurrentWidget(self)
        self.start()

        self._fit_svg_to_view()

    def _fit_svg_to_view(self):
        scene_rect = self.svg_item.boundingRect()
        self.scene.setSceneRect(scene_rect)

        self.graphic_object.fitInView(
            scene_rect,
            QtC.Qt.AspectRatioMode.KeepAspectRatio
        )

    @staticmethod
    def _build_duration(duration: Optional[int]) -> int:
        if duration:
            return duration
        else:
            return 3000

    def _set_column_proportion(self):
        self.container_layout.setColumnStretch(0, 30)
        self.container_layout.setColumnStretch(1, 40)
        self.container_layout.setColumnStretch(2, 30)

    def _set_row_proportion(self):
        self.container_layout.setRowStretch(0, 5)
        self.container_layout.setRowStretch(1, 80)
        self.container_layout.setRowStretch(2, 10)
        self.container_layout.setRowStretch(3, 5)

    def _build_loading_plaintext(
        self
    ) -> LoadingPlaintext | OptionalMsgPlaintext:
        if self.optional_msg:
            return OptionalMsgPlaintext(self.optional_msg)
        return LoadingPlaintext()

    def _on_rotation_changed(self, value: int):
        rotation_angle = value % 360
        self.svg_item.setRotation(rotation_angle)

    def start(self):
        self.rotation_animation.start()

    def stop(self):
        self.rotation_animation.stop()

    def resizeEvent(self, event: QtG.QResizeEvent):
        super().resizeEvent(event)
        self._fit_svg_to_view()
