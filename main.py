import sys
from random import randint
from PyQt5 import uic
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            self.do_paint = False
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        qp.setPen(QColor(235, 235, 0))
        for i in range(randint(2, 15)):
            x, y, r = randint(0, 350), randint(0, 200), randint(30, 50)
            qp.drawEllipse(x, y, r, r)

    def draw(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec())