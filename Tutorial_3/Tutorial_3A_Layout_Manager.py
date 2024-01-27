import self as self
from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout,
                             QFormLayout, QVBoxLayout, QTextEdit, QFileDialog)

#Creating a layout and initializing it
v_box = QVBoxLayout()
parent_window.setLayout(v_box)

#Creating a QTextEdit and adding it
name = QTextEdit()
v_box.addWidget(name)

#Opening a file with the QFileDialog module
file_name = QFileDialog.getOpenFileName(self, 'Open File', "/Users/user_name/Desktop/","All Files (*);;Text Files (*.txt)")

#Saving a file with the QFileDialog module
file_name = QFileDialog.getSaveFileName(self, 'Save File', "/Users/user_name/Desktop/","All Files (*);;Text Files (*.txt)")

#Adjusting the appearance of our dialog boxes
options = QFileDialog.Options()
options = QFileDialog.DontUseNativeDialog