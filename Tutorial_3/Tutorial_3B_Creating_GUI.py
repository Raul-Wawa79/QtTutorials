import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QTextEdit,
QMessageBox, QFileDialog)
from PyQt6 import QtWidgets

#Creating the Notepad class
class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 700, 700)
        self.setWindowTitle('Notepad GUI')
        self.notepadWidgets()
        self.show()

    #Creating the notepadWidgets function
    def notepadWidgets(self):
        new_button = QPushButton("New", self)
        new_button.move(10, 20)
        new_button.clicked.connect(self.clearText)
        save_button = QPushButton("Save", self)
        save_button.move(80, 20)
        save_button.clicked.connect(self.saveText)
        self.text_field = QTextEdit(self)
        self.text_field.resize(680, 630)
        self.text_field.move(10, 60)

    #Creating the clearText function
    def clearText(self):
        answer = QMessageBox.question(self, "Clear Text", "Do you want to clear the text?",
                                      QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        if answer == QMessageBox.StandardButton.Yes:
            self.text_field.clear()
        else:
            pass

    #Creating the saveText function
    def saveText(self):
        notepad_text = self.text_field.toPlainText()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            with open(file_name, 'w') as f:
                f.write(notepad_text)

#Ending and running the program
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Notepad()
  sys.exit(app.exec())