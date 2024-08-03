from PyQt6.QtWidgets import QMessageBox

from crypto.symmetric import BlockCrypto, RC4
from forms import msgbox


class SymmetricPage:
    def __init__(self, main_form):
        self.main_form = main_form

    def combobox_update(self):
        self.main_form.symmetric_label_warn.setText('')
        self.main_form.symmetric_comboBox_mode.setEnabled(True)
        self.main_form.symmetric_comboBox_mode.setVisible(True)
        self.main_form.symmetric_label_4.setVisible(True)

        if self.main_form.symmetric_comboBox_cipher.currentText() in ('DES', '3DES', 'RC4'):
            self.main_form.symmetric_label_warn.setStyleSheet('color: #e7816a; font-size: 11pt;')
            self.main_form.symmetric_label_warn.setText('Attention!\nThe encryption method\nyou selected is outdated.'
                                                        '\nIts use may not be safe.')

            if self.main_form.symmetric_comboBox_cipher.currentText() == 'RC4':
                self.main_form.symmetric_comboBox_mode.setDisabled(True)
                self.main_form.symmetric_comboBox_mode.setVisible(False)
                self.main_form.symmetric_label_4.setVisible(False)

    def encrypt(self):
        input_text = self.main_form.symmetric_textEdit_input.toPlainText()
        key = self.main_form.symmetric_lineEdit_key.text()

        if self.main_form.symmetric_comboBox_cipher.currentText() == 'RC4':
            output_text = RC4.encrypt(key, input_text)
        else:
            cipher = self.main_form.symmetric_comboBox_cipher.currentText()
            mode = self.main_form.symmetric_comboBox_mode.currentText()
        output_text = BlockCrypto(cipher, mode).encrypt(key, input_text)
        self.main_form.symmetric_textEdit_output.setPlainText(output_text)

    def decrypt(self):
        input_text = self.main_form.symmetric_textEdit_input.toPlainText()
        key = self.main_form.symmetric_lineEdit_key.text()

        try:
            if self.main_form.symmetric_comboBox_cipher.currentText() == 'RC4':
                self.main_form.symmetric_textEdit_output.setPlainText(RC4.decrypt(key, input_text))
            else:
                cipher = self.main_form.symmetric_comboBox_cipher.currentText()
                mode = self.main_form.symmetric_comboBox_mode.currentText()
                self.main_form.symmetric_textEdit_output.setPlainText(
                    BlockCrypto(cipher, mode).decrypt(key, input_text))

        except Exception as E:
            self.main_form.symmetric_textEdit_output.setPlainText('')
            msgbox.show_msg('Decoding Error', 'An error occurred during decoding',
                            detailed_text=f'Exception:\n{str(E)}', icon=QMessageBox.Icon.Warning)
