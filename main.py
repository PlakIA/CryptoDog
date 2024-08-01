import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from interface import main
from interface.resources import resources


class MainForm(QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        # with open('interface/resources/stylesheet.qss', 'r', encoding='utf8') as f:
        #     self.setStyleSheet(f.read())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
