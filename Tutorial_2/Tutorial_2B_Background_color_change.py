import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, pyqtSignal, QObject

#Creating the SendSignal class
class SendSignal(QObject):
  change_style = pyqtSignal()

#Creating the Example class
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Create Custom Signals')
        self.setupLabel()
        self.show()

#Creating the setupLabel function
    def setupLabel(self):
        self.index = 0
        self.direction = ""
        self.colors_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.label = QLabel()
        self.label.setStyleSheet("background-color: {}".format(self.colors_list[self.index]))
        self.setCentralWidget(self.label)

        self.sig = SendSignal()
        self.sig.change_style.connect(self.changeBackground)

#Creating the keyPressEvent function
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key.Key_Up):
            self.direction = "up"
            self.sig.change_style.emit()
        elif event.key() == Qt.Key.Key_Down:
            self.direction = "down"
            self.sig.change_style.emit()

    #Creating the changeBackground function
    def changeBackground(self):
        if self.direction == "up" and self.index < len(self.colors_list) - 1:
         self.index = self.index + 1
         self.label.setStyleSheet("background-color: {}".format(self.colors_list[self.index]))
        elif self.direction == "down" and self.index > 0:
         self.index = self.index - 1
         self.label.setStyleSheet("background-color: {}".format(self.colors_list[self.index]))

#Running the program
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Example()
  sys.exit(app.exec())