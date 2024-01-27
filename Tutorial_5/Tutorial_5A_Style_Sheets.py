import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel,
                             QRadioButton, QGroupBox, QLineEdit, QHBoxLayout, QVBoxLayout)

class ContactForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Contact Form')
        self.setupTabs()
        self.show()

    def setupTabs(self):
        self.tab_bar = QTabWidget(self)
        self.prof_details_tab = QWidget()
        self.background_tab = QWidget()
        self.tab_bar.addTab(self.prof_details_tab, "Profile Details")
        self.tab_bar.addTab(self.background_tab, "Background")
        self.profileDetailsTab()
        self.backgroundTab()
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)
        self.setLayout(main_h_box)

    def profileDetailsTab(self):
        name_label = QLabel("Name")
        name_entry = QLineEdit()
        address_label = QLabel("Address")
        address_entry = QLineEdit()
        gender_gb = QGroupBox("Gender")
        male_rb = QRadioButton("Male")
        female_rb = QRadioButton("Female")
        gender_h_box = QHBoxLayout()
        gender_h_box.addWidget(male_rb)
        gender_h_box.addWidget(female_rb)
        gender_gb.setLayout(gender_h_box)
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(name_label)
        tab_v_box.addWidget(name_entry)
        tab_v_box.addStretch()
        tab_v_box.addWidget(address_label)
        tab_v_box.addWidget(address_entry)
        tab_v_box.addStretch()
        tab_v_box.addWidget(gender_gb)
        self.prof_details_tab.setLayout(tab_v_box)

    def backgroundTab(self):
        self.education_gb = QGroupBox("Highest Level of Education")
        ed_v_box = QVBoxLayout()
        education_list = ["High School Diploma", "Associate's Degree",
                          "Bachelor's Degree", "Master's Degree", "Doctorate or Higher"]
        for ed in education_list:
            self.education_rb = QRadioButton(ed)
            ed_v_box.addWidget(self.education_rb)
        self.education_gb.setLayout(ed_v_box)
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(self.education_gb)
        self.background_tab.setLayout(tab_v_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactForm()
    sys.exit(app.exec())