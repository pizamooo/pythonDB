from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login_form import Ui_MainWindow
from db_manager import DBManager

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = DBManager()
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.register)

    def login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        user = self.db.check_user(username, password)
        if user:
            QMessageBox.information(self, "Success", "Logged in successfully")
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")

        

    def register(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        if self.db.register_user(username, password):
            QMessageBox.information(self, "Success", "Registered successfully")
        else:
            QMessageBox.warning(self, "Error", "Registration failed")



if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()