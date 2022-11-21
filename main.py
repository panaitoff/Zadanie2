from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)


if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.show()

    app.exec()
    sys.exit(app.exec())
