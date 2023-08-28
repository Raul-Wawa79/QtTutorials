import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
QMessageBox, QLineEdit, QPushButton)
from PyQt6.QtGui import QFont

#Creating the DisplayMessageBox class.
class DisplayMessageBox(QWidget):
  def __init__(self):
    super().__init__()
    self.initializeUI()

  def initializeUI(self):
    self.setGeometry(100, 100, 400, 200)
    self.setWindowTitle('QMessageBox')
    self.displayWidgets()
    self.show()

  #Creating the displayWidgets function
  def displayWidgets(self):
    catalogue_label = QLabel("Author Catalogue", self)
    catalogue_label.move(70, 50)
    catalogue_label.setFont(QFont('Arial', 20))
    auth_label = QLabel("Enter the name of the author you are searching for:", self)
    auth_label.move(70, 95)
    author_name = QLabel("Name:", self)
    author_name.move(70, 120)
    self.auth_entry = QLineEdit(self)
    self.auth_entry.move(115, 120)
    self.auth_entry.resize(240, 20)
    self.auth_entry.setPlaceholderText("Full name")
    search_button = QPushButton("Search", self)
    search_button.move(140, 155)
    search_button.resize(150, 40)
    search_button.clicked.connect(self.displayMessageBox)

  #Creating the displayMessageBox function
  def displayMessageBox(self):
      try:
          with open("authors.txt", "r") as f:
              authors = [line.rstrip('\n') for line in f]
      except FileNotFoundError:
          print("The file cannot be found.")
      not_found_msg = QMessageBox()
      if self.auth_entry.text() in authors:
          QMessageBox().information(self, "Author Found", "Author found in catalogue!", QMessageBox.StandardButton.Ok,
                                    QMessageBox.StandardButton.Ok)
      else:
          not_found_msg = QMessageBox.question(self, "Author Not Found",
                                               "Author not found in catalogue.\nDo you wish to continue?",
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                               QMessageBox.StandardButton.No)
      if not_found_msg == QMessageBox.StandardButton.No:
          print("Closing application.")
          self.close()
      else:
          pass

#Ending the program
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = DisplayMessageBox()
  sys.exit(app.exec())