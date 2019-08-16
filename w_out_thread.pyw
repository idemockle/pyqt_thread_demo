import time, sys

from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout(self)

        self.textlabel = QLabel(self)
        mainLayout.addWidget(self.textlabel)

        button = QPushButton('Count down', self)
        button.clicked.connect(self.ready_set_go)
        mainLayout.addWidget(button)

    def ready_set_go(self):
        self.textlabel.setText('READY')
        self.textlabel.setStyleSheet('color: red; font-size: 80pt; text-align: center;')
        time.sleep(1)
        self.textlabel.setText('SET')
        self.textlabel.setStyleSheet('color: yellow; font-size: 80pt; text-align: center;')
        time.sleep(1)
        self.textlabel.setText('GO!!!')
        self.textlabel.setStyleSheet('color: green; font-size: 80pt; text-align: center;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())