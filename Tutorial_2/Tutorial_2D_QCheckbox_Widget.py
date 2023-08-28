import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, QLabel)
from PyQt6.QtCore import Qt

#Creating the CheckBoxWindow class
class CheckBoxWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.initializeUI()

  def initializeUI(self):
    self.setGeometry(100, 100, 250, 250)
    self.setWindowTitle('QCheckBox Widget')
    self.displayCheckBoxes()
    self.show()

  #Creating the displayCheckboxes function
  def displayCheckBoxes(self):
    header_label = QLabel(self)
    header_label.setText("Which shifts can you work? (Please check all that apply)")
    header_label.setWordWrap(True)
    header_label.move(10, 10)
    header_label.resize(230, 60)
    morning_cb = QCheckBox("Morning [8 AM-2 PM]", self)  # text, parent
    morning_cb.move(20, 80)
  # morning_cb.toggle()
    morning_cb.stateChanged.connect(self.printToTerminal)
    after_cb = QCheckBox("Afternoon [1 PM-8 PM]", self)  # text, parent
    after_cb.move(20, 100)
    after_cb.stateChanged.connect(self.printToTerminal)
    night_cb = QCheckBox("Night [7 PM-3 AM]", self)  # text, parent
    night_cb.move(20, 120)
    night_cb.stateChanged.connect(self.printToTerminal)

  #Creating the printToTerminal function
  def printToTerminal(self, state):
    sender = self.sender()
    if Qt.CheckState(state) == Qt.CheckState.Checked:
      print("{} Selected.".format(sender.text()))
    else:
      print("{} Deselected.".format(sender.text()))

#Ending and running the program
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = CheckBoxWindow()
  sys.exit(app.exec())