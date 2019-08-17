import time, sys

from PyQt5.QtWidgets import *
from PyQt5.Qt import QThread, QObject


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout(self)
        self.textlabel = QLabel(self)
        self.mainLayout.addWidget(self.textlabel)

        self.gothread = QThread()
        self.gothread.start()
        self.countdownworker = CountdownWorker(self.textlabel)
        self.countdownworker.moveToThread(self.gothread)

        self.button = QPushButton('Count down', self)
        self.button.clicked.connect(self.countdownworker.countdown)
        self.mainLayout.addWidget(self.button)


class CountdownWorker(QObject):
    def __init__(self, qlabel):
        super().__init__()
        self.qlabel = qlabel

    def countdown(self):
        self.qlabel.setText('READY')
        self.qlabel.setStyleSheet('color: red; font-size: 80pt; text-align: center;')
        time.sleep(1)
        self.qlabel.setText('SET')
        self.qlabel.setStyleSheet('color: yellow; font-size: 80pt; text-align: center;')
        time.sleep(1)
        self.qlabel.setText('GO!!!')
        self.qlabel.setStyleSheet('color: green; font-size: 80pt; text-align: center;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())