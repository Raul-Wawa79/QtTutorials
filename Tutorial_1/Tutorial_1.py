import sys
from PyQt6.QtWidgets import QApplication, QWidget

#Creating the EmptyWindow class
class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(150, 50, 700, 700)
        self.setWindowTitle('Empty Window in PyQt')
        self.show()

#Ending off by running the program.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())