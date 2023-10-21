import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect, QPushButton, QGraphicsOpacityEffect, QMenuBar, QDialog
from catalog import CatalogWood, CatalogUpholstery


class Main(QWidget):

    def __init__(self):
        super(Main, self).__init__()
        ui, _ = uic.loadUiType('ui/main.ui')
        self.ui = ui()
        self.ui.setupUi(self)
        self.setWindowTitle("Мода на комоды - Калькулятор стоимости мебельных изделий")

        self.dlg = None
        self.wood = None
        self.upholstery = None
        self.width = 0
        self.height = 0
        self.deep = 0
        self.section = 0
        self.box = 0
        self.shelf = 0
        self.legs = False

        self.ui.btn_wood.setIcon(QIcon("icons/material.png"))
        self.ui.btn_upholstery.setIcon(QIcon("icons/upholstery.png"))
        self.ui.btn_clear.setIcon(QIcon("icons/clear.png"))
        self.ui.btn_save.setIcon(QIcon("icons/save.png"))

        self.ui.btn_wood.clicked.connect(self.choose_wood)
        self.ui.btn_upholstery.clicked.connect(self.choose_upholstery)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_save.clicked.connect(self.save)

        self.ui.sb_height.valueChanged.connect(self.change_height)
        self.ui.sb_width.valueChanged.connect(self.change_width)
        self.ui.sb_deep.valueChanged.connect(self.change_deep)
        self.ui.sb_section.valueChanged.connect(self.change_sections)
        self.ui.sb_box.valueChanged.connect(self.change_boxes)
        self.ui.sb_shelf.valueChanged.connect(self.change_shelves)
        self.ui.check_legs.stateChanged.connect(self.change_legs)

    def choose_wood(self):
        self.dlg = CatalogWood()
        self.dlg.show()
        if self.dlg.exec_():
            self.wood = self.dlg.result
            self.ui.wood.setText(self.wood)
            self.calculate()
    def choose_upholstery(self):
        self.dlg = CatalogUpholstery()
        self.dlg.show()
        if self.dlg.exec_():
            self.upholstery = self.dlg.result
            self.ui.upholstery.setText(self.upholstery)
            self.calculate()

    def change_height(self):
        self.height = float(self.ui.sb_height.value())
        self.calculate()

    def change_width(self):
        self.width = float(self.ui.sb_width.value())
        self.calculate()

    def change_deep(self):
        self.deep = float(self.ui.sb_deep.value())
        self.calculate()

    def change_sections(self):
        self.section = int(self.ui.sb_section.value())
        self.calculate()

    def change_boxes(self):
        self.box = int(self.ui.sb_box.value())
        self.calculate()

    def change_shelves(self):
        self.shelf = int(self.ui.sb_shelf.value())
        self.calculate()

    def change_legs(self):
        self.legs = self.ui.check_legs.isChecked()
        self.calculate()

    def calculate(self):
        print("calculate")



app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())
