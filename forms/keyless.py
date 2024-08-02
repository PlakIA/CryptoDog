from PyQt6.QtGui import QPixmap

from crypto.keyless import LetsHash, B64, EasterEgg
from forms import msgbox
from PyQt6.QtWidgets import QMessageBox


class KeylessPage:
    def __init__(self, main_form):
        self.main_form = main_form

    def clear_output(self):
        self.main_form.keyless_textEdit_output.setPlainText('')
        self.main_form.keyless_textEdit_output.setStyleSheet('')
        self.main_form.keyless_label_warn.resize(160, 60)
        self.main_form.keyless_label_warn.setPixmap(QPixmap(''))
        self.main_form.keyless_label_warn.setText('')

    def combobox_update(self):
        self.clear_output()
        if self.main_form.keyless_comboBox.currentText() == 'Base64':
            self.main_form.keyless_btn_decode.setVisible(True)
            self.main_form.keyless_btn_decode.setEnabled(True)
            self.main_form.keyless_btn_encode.setText('Encode')
            self.main_form.keyless_btn_decode.setText('Decode')
        else:
            self.main_form.keyless_btn_encode.setText('Hash')
            self.main_form.keyless_btn_decode.setVisible(False)
            self.main_form.keyless_btn_decode.setDisabled(True)

    def encode_func(self):
        self.clear_output()
        input_text = self.main_form.keyless_textEdit_input.toPlainText()
        if self.main_form.keyless_comboBox.currentText() == 'Base64':
            self.main_form.keyless_textEdit_output.setPlainText(B64.encode64(input_text))
        else:
            hash_algo = self.main_form.keyless_comboBox.currentText().lower()
            self.main_form.keyless_textEdit_output.setPlainText(LetsHash(hash_algo).hash(input_text))

    def decode_func(self):
        try:
            self.clear_output()
            input_text = self.main_form.keyless_textEdit_input.toPlainText()
            self.main_form.keyless_textEdit_output.setPlainText(B64.decode64(input_text))
        except EasterEgg:
            self.main_form.keyless_label_warn.setStyleSheet('font-size: 36pt; color: #d54653;')
            self.main_form.keyless_label_warn.setText(u'\u2665')
            self.main_form.keyless_textEdit_output.setStyleSheet('font-size: 36pt; color: #1e1e1e')
            self.main_form.keyless_textEdit_output.setPlainText(u'\u2665')
            msgbox.show_msg('Easter Egg', u'\u2665', detailed_text=u'\u2665', icon=QMessageBox.Icon.NoIcon)
        except Exception as E:
            self.main_form.keyless_textEdit_output.setPlainText('')
            msgbox.show_msg('Decoding Error', 'An error occurred during decoding',
                            detailed_text=f'Exception:\n{str(E)}', icon=QMessageBox.Icon.Warning)
