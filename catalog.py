import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QGraphicsDropShadowEffect, QPushButton, QLabel, QFrame


class CatalogWood(QDialog):

    def __init__(self):
        super(CatalogWood, self).__init__()
        ui, _ = uic.loadUiType('ui/catalog_wood.ui')
        self.ui = ui()
        self.ui.setupUi(self)
        self.result = None

        for child in self.findChildren(QPushButton):
                pic = "_".join(child.objectName().split("_")[1:])
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
                child.clicked.connect(self.return_wood)

    def return_wood(self):
        d = {"larch": "Лиственница",
             "oak": "Дуб",
             "birch": "Береза",
             "cherry": "Вишня",
             "alder": "Ольха",
             "ash": "Ясень",
             "pine": "Сосна",
             "beech": "Бук",
             "walnut": "Орех",
             "apple": "Яблоня",
             "red": "Красное дерево",
             "ebony": "Черное дерево"
             }
        self.result = d["_".join(self.sender().objectName().split("_")[1:])]
        self.close_dlg()

    def close_dlg(self):
        self.accept()


class CatalogUpholstery(QDialog):

    def __init__(self):
        super(CatalogUpholstery, self).__init__()
        ui, _ = uic.loadUiType('ui/catalog_upholstery.ui')
        self.ui = ui()
        self.ui.setupUi(self)
        self.result = None

        for child in self.findChildren(QPushButton):
            pic = "_".join(child.objectName().split("_")[1:])
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
            child.clicked.connect(self.return_upholstery)

    def return_upholstery(self):
        d = {"leather": "Кожа",
             "eco_leather": "Экокожа",
             "mat": "Рогожа",
             "chenille": "Шенилл",
             "nat_suede": "Натуральная замша",
             "faux_suede": "Искусственная замша",
             "flock": "Флок",
             "microfiber": "Микрофибра",
             "boucle": "Букле",
             "velours": "Велюр",
             "tapestry": "Гобелен",
             "jacquard": "Жаккард"
             }
        self.result = d["_".join(self.sender().objectName().split("_")[1:])]
        self.close_dlg()

    def close_dlg(self):
        self.accept()