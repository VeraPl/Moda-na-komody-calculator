import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect, QPushButton, QGraphicsOpacityEffect


class Main(QWidget):

    def __init__(self):
        super(Main, self).__init__()
        ui, _ = uic.loadUiType('ui/main.ui')
        self.ui = ui()
        self.ui.setupUi(self)

        self.ui.logo.setPixmap(QPixmap('icons/logo.png'))
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.7)
        self.ui.frame.setGraphicsEffect(self.opacity_effect)


app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())
