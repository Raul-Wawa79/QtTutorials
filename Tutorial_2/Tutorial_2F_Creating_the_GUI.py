import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox,
QPushButton, QLabel, QLineEdit)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class CreateNewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Create New User GUI')
        self.displayWidgetsToCollectInfo()
        self.show()

    def displayWidgetsToCollectInfo(self):
        new_user_image = "user.png"
        try:
            with open(new_user_image):
                new_user = QLabel(self)
                pixmap = QPixmap(new_user_image)
                new_user.setPixmap(pixmap)
                new_user.move(150, 60)
                new_user.setPixmap(pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))

        except FileNotFoundError:
            print("Image not found.")

        login_label = QLabel(self)
        login_label.setText("Create New Account")
        login_label.move(78, 20)
        login_label.setFont(QFont('Arial', 20))
        name_label = QLabel("Username:", self)
        name_label.move(50, 180)
        self.name_entry = QLineEdit(self)
        self.name_entry.move(130, 180)
        self.name_entry.resize(200, 20)
        name_label = QLabel("Full Name:", self)
        name_label.move(50, 210)
        name_entry = QLineEdit(self)
        name_entry.move(130, 210)
        name_entry.resize(200, 20)
        pswd_label = QLabel("Password:", self)
        pswd_label.move(50, 240)
        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.pswd_entry.move(130, 240)
        self.pswd_entry.resize(200, 20)
        confirm_label = QLabel("Confirm:", self)
        confirm_label.move(50, 270)
        self.confirm_entry = QLineEdit(self)
        self.confirm_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_entry.move(130, 270)
        self.confirm_entry.resize(200, 20)
        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.move(100, 310)
        sign_up_button.resize(200, 40)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        pswd_text = self.pswd_entry.text()
        confirm_text = self.confirm_entry.text()
        if pswd_text != confirm_text:
            QMessageBox.warning(self, "Error Message",
                        " The passwords you entered do not match. Please try again.", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else:
            with open("users.txt", 'a+') as f:
                f.write(self.name_entry.text() + " ")
                f.write(pswd_text + "\n")
                self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateNewUser()
    sys.exit(app.exec())