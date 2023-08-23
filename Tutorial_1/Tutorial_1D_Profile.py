import sys, os.path
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QFont, QPixmap

#Creating the UserProfile class
class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("My Work Profile")
        self.displayImages()
        self.displayUserInfo()
        self.show()

        #Creating the displayImages function
    def displayImages(self):
            background_image = 'raulito.jpg'
            try:
                with open(background_image):
                    background = QLabel(self)
                    pixmap = QPixmap(background_image)
                    background.setPixmap(pixmap)
            except FileNotFoundError:
                print("Image not found. Remember to add your beautiful pic to the project folder.")

        #Creating the displayUserInfo function.
    def displayUserInfo(self):
            user_name = QLabel(self)
            user_name.setText("Raul BG")
            user_name.move(65, 40)
            user_name.setFont(QFont('Helvetica', 20))
            bio_title = QLabel(self)
            bio_title.setText("Biography")
            bio_title.move(15, 95)
            bio_title.setFont(QFont('Arial', 17))
            about = QLabel(self)
            about.setText("QA trying to switch to Automation.")
            about.setWordWrap(True)
            about.move(15, 130)
            skills_title = QLabel(self)
            skills_title.setText("Skills")
            skills_title.move(15, 185)
            skills_title.setFont(QFont('Arial', 17))
            skills = QLabel(self)
            skills.setText("Python | Java | SQL | Release")
            skills.move(15, 220)
            experience_title = QLabel(self)
            experience_title.setText("Experience")
            experience_title.move(15, 265)
            experience_title.setFont(QFont('Arial', 17))
            experience = QLabel(self)
            experience.setText("Senior QA Analyst")
            experience.move(15, 300)
            dates = QLabel(self)
            dates.setText("Dec 2019 - Present")
            dates.move(15, 320)
            dates.setFont(QFont('Arial', 10))
            experience = QLabel(self)
            experience.setText("Kebab Testing")
            experience.move(15, 345)
            dates = QLabel(self)
            dates.setText("Jan 2018 - Dec 2019")
            dates.move(15, 365)
            dates.setFont(QFont('Arial', 10))

#Running the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfile()
    sys.exit(app.exec())