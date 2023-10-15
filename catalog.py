import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect, QPushButton, QLabel, QFrame


class Selection(QDialog):

    def __init__(self):
        super(Selection, self).__init__()
        ui, _ = uic.loadUiType('ui/catalog.ui')
        self.ui = ui()
        self.ui.setupUi(self)

        self.select_wood()
        # self.select_fabric()

    def select_wood(self):
        for child in self.findChildren(QPushButton):
            pic = child.objectName().split("_")[-1]
            child.setStyleSheet(f"""QPushButton {{
                                    background-color: grey;
                                    border-image: url('icons/materials/{pic}.jpg') 3 10 3 10;
                                    border-top: 10px transparent;
                                    border-bottom: 3px transparent;
                                    border-right: 10px transparent;
                                    border-left: 10px transparent;
                                    border-radius: 75px;
                                    max-width: 150px;
                                    max-height: 150px;
                                    min-width: 150px;
                                    min-height: 150px;
                                }}""")
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(16)
            child.setGraphicsEffect(shadow)

    def select_fabric(self):
        change_pic = {"larch":"leather", "oak":"eco_leather", "birch":"mat", "cherry":"chenille", "alder":"nat_suede",
                      "pine":"faux_suede", "ash":"flock", "beech":"microfiber", "walnut":"boucle", "apple":"velours",
                      "red": "tapestry", "ebony": "jacquard"}
        change_text ={"larch": "Натуральная кожа", "oak": "Экокожа", "birch": "Рогожа", "cherry": "Шенилл",
                      "alder": "Натуральная замша", "pine": "Искусственная замша", "ash": "Флок", "beech": "Микрофибра",
                      "walnut": "Букле", "apple": "Велюр", "red": "Гобелен", "ebony": "Жаккард"}
        for child in self.findChildren(QPushButton):
            pic = child.objectName().split("_")[-1]
            child.setStyleSheet(f"""QPushButton {{
                                    background-color: transparent;
                                    border-image: url('icons/materials/{change_pic[pic]}.jpg') 3 10 3 10;
                                    border-top: 10px transparent;
                                    border-bottom: 3px transparent;
                                    border-right: 10px transparent;
                                    border-left: 10px transparent;
                                    border-radius: 75px;
                                    max-width: 150px;
                                    max-height: 150px;
                                    min-width: 150px;
                                    min-height: 150px;
                                }}""")
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(20)
            child.setGraphicsEffect(shadow)

        for child in self.findChildren(QLabel):
            pic = child.objectName().split("_")[-1]
            child.setText(change_text[pic])


app = QApplication(sys.argv)
window = Selection()
window.show()
sys.exit(app.exec_())
