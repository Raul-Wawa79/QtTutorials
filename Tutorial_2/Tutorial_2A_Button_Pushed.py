import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

#Creating the ButtonWindow class
class ButtonWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.initializeUI()

  #Creating the initializeUI function
  def initializeUI(self):
        self.setGeometry(100, 100, 230, 150)
        self.setWindowTitle('QPushButton')
        self.displayButton()
        self.show()

  #Creating the displayButton function
  def displayButton(self):
    name_label = QLabel(self)
    name_label.setText("Don't push the button.")
    name_label.move(60, 30)
    button = QPushButton('Push Me', self)
    button.clicked.connect(self.buttonClicked)
    button.move(80, 70)

  #Creating the buttonClicked function
  def buttonClicked(self):
    print("The window has been closed.")
    self.close()

#Running the program
if __name__ == '__main__':
      app = QApplication(sys.argv)
      window = ButtonWindow()
      sys.exit(app.exec())
