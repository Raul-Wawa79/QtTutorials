import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

#Creating the DisplaySurvey class
class DisplaySurvey(QWidget):
  def __init__(self):
    super().__init__()
    self.initializeUI()

  def initializeUI(self):
    self.setGeometry(300, 100, 600, 235)
    self.setWindowTitle('Survey GUI')
    self.displayWidgets()
    self.show()

  #Creating the displayWidgets function
  def displayWidgets(self):
    title = QLabel("Restaurant Name")
    title.setFont(QFont('Arial', 21))
    question = QLabel("How would you rate your service today?")
    question.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_h_box = QHBoxLayout()
    title_h_box.addStretch()
    title_h_box.addWidget(title)
    title_h_box.addStretch()
    ratings = ["Not Satisfied", "Average", "Satisfied"]
    ratings_h_box = QHBoxLayout()
    ratings_h_box.setSpacing(60)  # Set spacing between in widgets in horizontal layout
    ratings_h_box.addStretch()
    for rating in ratings:
      rate_label = QLabel(rating, self)
      ratings_h_box.addWidget(rate_label)
    ratings_h_box.addStretch()
    cb_h_box = QHBoxLayout()
    cb_h_box.setSpacing(100)  # Set spacing between in widgets in horizontal layout
    scale_bg = QButtonGroup(self)
    cb_h_box.addStretch()
    for cb in range(len(ratings)):
      scale_cb = QCheckBox(str(cb), self)
      cb_h_box.addWidget(scale_cb)
      scale_bg.addButton(scale_cb)
    cb_h_box.addStretch()
    scale_bg.buttonClicked.connect(self.checkboxClicked)
    close_button = QPushButton("Close", self)
    close_button.clicked.connect(self.close)
    v_box = QVBoxLayout()
    v_box.addLayout(title_h_box)
    v_box.addWidget(question)
    v_box.addStretch(1)
    v_box.addLayout(ratings_h_box)
    v_box.addLayout(cb_h_box)
    v_box.addStretch(2)
    v_box.addWidget(close_button)
    self.setLayout(v_box)  # Set main layout of the window

  #Creating the checkboxClicked function
  def checkboxClicked(self, cb):
    print("{} Selected.".format(cb.text()))

#Running the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplaySurvey()
    sys.exit(app.exec())
