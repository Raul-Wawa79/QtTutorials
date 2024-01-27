import random
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QVBoxLayout)

class ChangeIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('QIcon Example')
        self.createWidgets()
        self.show()

    def createWidgets(self):
        info_label = QLabel("Click on the button and select a fruit.")
        self.images = [
            "1_apple.png"
        ]
        self.icon_button = QPushButton(self)
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)
        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addWidget(self.icon_button)
        self.setLayout(v_box)

    def changeButtonIcon(self):
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChangeIcon()
    sys.exit(app.exec())