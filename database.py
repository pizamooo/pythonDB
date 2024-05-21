import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

db_name = sqlite3.connect('databases/mydb.db')
cursor = db_name.cursor()

app = QApplication([])
Form, Window = uic.loadUiType("MainForm.ui")
window = Window()
form = Form()
form.setupUi(window)
window.show()

db_name.commit()
db_name.close()
app.exec()