import time, sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import QThread


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout(self)
        self.gothread = GoThread(self)

        self.textlabel = QLabel(self)
        mainLayout.addWidget(self.textlabel)

        button = QPushButton('Count down', self)
        button.clicked.connect(self.gothread.start)
        mainLayout.addWidget(button)


class GoThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)

    def run(self):
        self.parent().textlabel.setText('READY')
        self.parent().textlabel.setStyleSheet('color: red; font-size: 80pt; text-align: center;')
        time.sleep(1)
        self.parent().textlabel.setText('SET')
        self.parent().textlabel.setStyleSheet('color: yellow; font-size: 80pt; text-align: center;')
        time.sleep(1)
        self.parent().textlabel.setText('GO!!!')
        self.parent().textlabel.setStyleSheet('color: green; font-size: 80pt; text-align: center;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())