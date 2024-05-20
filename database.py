import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

db_name = sqlite3.connect('databases/mydb.db')
cursor = db_name.cursor()
def on_click():
    print("hello")

app = QApplication([])
Form, Window = uic.loadUiType("MainForm.ui")
window = Window()
form = Form()
form.setupUi(window)
form.log_in.clicked.connect(on_click)
window.show()
db_name.close()
app.exec()