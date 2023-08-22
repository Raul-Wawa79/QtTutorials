import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

#Creating the HelloWorldWindow class
class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(150, 50, 700, 700)
        self.setWindowTitle('QLabel')
        self.displayLabels()
        self.show()

#Creating the displayLabels function
    def displayLabels(self):
        text = QLabel(self)
        text.setText("Hello")
        text.move(260, 15)
        image = "world2.png"
        try:
            with open(image):
                world_image = QLabel(self)
            pixmap = QPixmap(image)
            world_image.setPixmap(pixmap)
            world_image.move(25, 40)
        except FileNotFoundError:
            print("Image not found.")

#Ending and running the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    sys.exit(app.exec())