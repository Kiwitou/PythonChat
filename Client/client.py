import sys
import requests
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit


NAME = "your_name"
URL = "http://127.0.0.1:5000" # don't add the / at the end of the URL


def send(msg):
    try:
        r = requests.post(URL+"/push/"+NAME, json={"msg": msg})
    except:
        return False
    if r.content.decode("utf8") == "true":
        return True
    else:
        return False


def load():
    try:
        r = requests.get(URL+"/pull/"+NAME)
    except:
        return "Server is offline"
    return r.content.decode("utf8")


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Python Chat by Kiwitou'
        self.left = 30
        self.top = 40
        self.width = 640
        self.height = 480
        self.initUI()

    @pyqtSlot()
    def send_msg(self):
        textboxValue = self.textbox.text()
        send(textboxValue)

    def on_click(self):
        self.send_msg()
        self.update_msg()

    def update_msg(self):
        self.label.setText(load())

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(load(), self)
        self.label.resize(540, 300)
        self.label.move(50, 50)

        self.textbox = QLineEdit(self)
        self.textbox.move(10, 10)
        self.textbox.resize(280, 20)

        self.button = QPushButton("Send", self)
        self.button.move(300, 10)
        self.button.resize(50, 20)
        self.button.clicked.connect(self.on_click)

        self.button2 = QPushButton("Reload", self)
        self.button2.move(300, 40)
        self.button2.resize(50, 20)
        self.button2.clicked.connect(self.update_msg)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())
