import sys
import webbrowser

import pyperclip
from PyQt6.QtWidgets import QMainWindow, QApplication

from forms import msgbox
from forms.keyless import KeylessPage
from forms.symmetric import SymmetricPage
from interface import main


class MainForm(QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # with open('interface/resources/stylesheet.qss', 'r', encoding='utf8') as f:
        #     self.setStyleSheet(f.read())

        self.actionGitHub_Page.triggered.connect(lambda: webbrowser.open('https://github.com/PlakIA/CryptoDog'))
        self.actionAbout.triggered.connect(lambda: msgbox.show_msg('About', 'CryptoDog\nv0.3-alpha'))

        self.keyless_page = KeylessPage(self)
        self.keyless_comboBox.textActivated.connect(self.keyless_page.combobox_update)
        self.keyless_btn_encode.clicked.connect(self.keyless_page.encode_func)
        self.keyless_btn_decode.clicked.connect(self.keyless_page.decode_func)
        self.keyless_btn_copy.clicked.connect(lambda: pyperclip.copy(self.keyless_textEdit_output.toPlainText()))

        self.symmetric_page = SymmetricPage(self)
        self.symmetric_btn_encrypt.clicked.connect(self.symmetric_page.encrypt)
        self.symmetric_btn_decrypt.clicked.connect(self.symmetric_page.decrypt)
        self.symmetric_btn_copy.clicked.connect(lambda: pyperclip.copy(self.symmetric_textEdit_output.toPlainText()))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
