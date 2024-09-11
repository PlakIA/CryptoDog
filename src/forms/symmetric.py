from PyQt6.QtWidgets import QMessageBox

from crypto.symmetric import BlockCrypto
from forms import msgbox


class SymmetricPage:
    def __init__(self, main_form):
        self.main_form = main_form

    def encrypt(self):
        input_text = self.main_form.symmetric_textEdit_input.toPlainText()
        key = self.main_form.symmetric_lineEdit_key.text()
        cipher = self.main_form.symmetric_comboBox_cipher.currentText()
        mode = self.main_form.symmetric_comboBox_mode.currentText()

        output_text = BlockCrypto(cipher, mode).encrypt(key, input_text)
        self.main_form.symmetric_textEdit_output.setPlainText(output_text)

    def decrypt(self):
        input_text = self.main_form.symmetric_textEdit_input.toPlainText()
        key = self.main_form.symmetric_lineEdit_key.text()
        cipher = self.main_form.symmetric_comboBox_cipher.currentText()
        mode = self.main_form.symmetric_comboBox_mode.currentText()

        try:
            self.main_form.symmetric_textEdit_output.setPlainText(
                BlockCrypto(cipher, mode).decrypt(key, input_text))
        except Exception as E:
            self.main_form.symmetric_textEdit_output.setPlainText('')
            msgbox.show_msg('Decoding Error', 'An error occurred during decoding',
                            detailed_text=f'Exception:\n{str(E)}', icon=QMessageBox.Icon.Warning)
