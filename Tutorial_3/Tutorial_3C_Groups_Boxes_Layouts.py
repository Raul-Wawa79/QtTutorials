from PyQt6.QtWidgets import QButtonGroup, QCheckBox

#Creating the QButtonGroup Class
b_group = QButtonGroup() # Create instance of QButtonGroup
# Create two checkboxes
cb_1 = QCheckBox("CB 1")
cb_2 = QCheckBox("CB 2")
# Add checkboxes into QButtonGroup
b_group.addButton(cb_1)
b_group.addButton(cb_2)
# Connect all buttons in a group to one signal
b_group.buttonClicked.connect(cbClicked)
def cbClicked(cb):
  print(cb)

#Creating horizontal layouts with PyQt
# Create horizontal layouts
title_h_box = QHBoxLayout()
title_h_box.addStretch()
title_h_box.addWidget(title)
title_h_box.addStretch()

#Creating a horizontal and a vertical layout
v_box = QVBoxLayout() # Create vertical layout
v_box.addLayout(title_h_box) # Add horizontal layout
v_box.addWidget(question) # Add widget