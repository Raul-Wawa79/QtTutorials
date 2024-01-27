import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow)
from PyQt6.QtGui import QAction

class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Basic Menu Example')
        self.createMenu()
        self.show()

    def createMenu(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec())