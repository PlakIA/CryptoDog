from PyQt6.QtWidgets import QMessageBox


def show_msg(title: str, text: str, additional_text: str = '', detailed_text: str = '',
             icon=QMessageBox.Icon.Information):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setInformativeText(additional_text)
    msg.setDetailedText(detailed_text)
    msg.exec()
