__author__ = 'Justin M'

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Message Box")
        self.show()

    def closeEvent(self,event):
        box = QMessageBox()
        reply = box.question(
            self,"Message","Are you sure you want to Quit?",
            box.Yes | box.No,box.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())