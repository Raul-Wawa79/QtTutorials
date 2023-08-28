import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt

#Creating the EntryWindow class
class EntryWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.initializeUI()

  #Creating the initializeUI function
  def initializeUI(self):
    self.setGeometry(100, 100, 400, 200)
    self.setWindowTitle('QLineEdit Widget')
    self.displayWidgets()
    self.show()

  #Creating the displayWidgets function
  def displayWidgets(self):
    QLabel("Please enter your name below.", self).move(100, 10)
    name_label = QLabel("Name:", self)
    name_label.move(70, 50)
    self.name_entry = QLineEdit(self)
    self.name_entry.setAlignment(Qt.AlignmentFlag.AlignLeft)
    self.name_entry.move(130, 50)
    self.name_entry.resize(200, 20)
    self.clear_button = QPushButton('Clear', self)
    self.clear_button.clicked.connect(self.clearEntries)
    self.clear_button.move(160, 110)

  #Creating the clearEntries function
  def clearEntries(self):
    sender = self.sender()
    if sender.text() == 'Clear':
      self.name_entry.clear()

  #Running the program
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = EntryWindow()
  sys.exit(app.exec())