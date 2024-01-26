import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

#Creating the SelectItems class
class SelectItems(QWidget):
  def __init__(self):
    super().__init__()
    self.initializeUI()

  def initializeUI(self):
    self.setGeometry(100, 100, 300, 200)
    self.setWindowTitle('ComboBox and SpinBox')
    self.itemsAndPrices()
    self.show()

  #Creating the itemsAndPrices function
  def itemsAndPrices(self):
    info_label = QLabel("Select 2 items you had for lunch and their prices.")
    info_label.setFont(QFont('Arial', 16))
    info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.display_total_label = QLabel("Total Spent: $")
    self.display_total_label.setFont(QFont('Arial', 16))
    self.display_total_label.setAlignment(Qt.AlignmentFlag.AlignRight)
    lunch_list = ["egg", "turkey sandwich", "ham sandwich", "cheese", "hummus",
                  "yogurt", "apple", "banana", "orange", "waffle", "baby carrots", "bread",
                  "pasta", "crackers", "pretzels", "pita chips", "coffee", "soda", "water"]
    lunch_cb1 = QComboBox()
    lunch_cb1.addItems(lunch_list)
    lunch_cb2 = QComboBox()
    lunch_cb2.addItems(lunch_list)
    self.price_sb1 = QSpinBox()
    self.price_sb1.setRange(1, 100)
    self.price_sb1.setPrefix("$")
    self.price_sb1.valueChanged.connect(self.calculateTotal)
    self.price_sb2 = QSpinBox()
    self.price_sb2.setRange(1, 100)
    self.price_sb2.setPrefix("$")
    self.price_sb2.valueChanged.connect(self.calculateTotal)
    h_box1 = QHBoxLayout()
    h_box2 = QHBoxLayout()
    h_box1.addWidget(lunch_cb1)
    h_box1.addWidget(self.price_sb1)
    h_box2.addWidget(lunch_cb2)
    h_box2.addWidget(self.price_sb2)
    v_box = QVBoxLayout()
    v_box.addWidget(info_label)
    v_box.addLayout(h_box1)
    v_box.addLayout(h_box2)
    v_box.addWidget(self.display_total_label)
    self.setLayout(v_box)

  #Creating the calculateTotal function
  def calculateTotal(self):
    total = self.price_sb1.value() + self.price_sb2.value()
    self.display_total_label.setText("Total Spent: ${}".format(str(total)))


#Running the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectItems()
    sys.exit(app.exec())