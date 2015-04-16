__author__ = 'Justin M'


import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10,italic = True))

        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QPushButton("Push Me",self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(100,25)
        btn.move(50,50)

        self.setGeometry(300,300,300,220)
        self.setWindowTitle("tool tips")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())