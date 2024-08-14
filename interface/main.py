# Form implementation generated from reading ui file '..\interface\source\main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(650, 550))
        MainWindow.setMaximumSize(QtCore.QSize(650, 550))
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 521))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_certs = QtWidgets.QWidget()
        self.tab_certs.setObjectName("tab_certs")
        self.certs_table = QtWidgets.QTableWidget(parent=self.tab_certs)
        self.certs_table.setGeometry(QtCore.QRect(0, 0, 620, 510))
        self.certs_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.certs_table.setAlternatingRowColors(False)
        self.certs_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.certs_table.setShowGrid(True)
        self.certs_table.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.certs_table.setWordWrap(True)
        self.certs_table.setColumnCount(3)
        self.certs_table.setObjectName("certs_table")
        self.certs_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.certs_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.certs_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.certs_table.setHorizontalHeaderItem(2, item)
        self.certs_table.horizontalHeader().setVisible(True)
        self.certs_table.horizontalHeader().setCascadingSectionResizes(False)
        self.certs_table.horizontalHeader().setDefaultSectionSize(200)
        self.certs_table.horizontalHeader().setHighlightSections(True)
        self.certs_table.horizontalHeader().setSortIndicatorShown(False)
        self.certs_table.horizontalHeader().setStretchLastSection(False)
        self.certs_table.verticalHeader().setVisible(False)
        self.certs_table.verticalHeader().setSortIndicatorShown(False)
        self.certs_table.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_certs, "")
        self.tab_keyless = QtWidgets.QWidget()
        self.tab_keyless.setObjectName("tab_keyless")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_keyless)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 431, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.keyless_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.keyless_label.setObjectName("keyless_label")
        self.verticalLayout_3.addWidget(self.keyless_label)
        self.keyless_textEdit_input = QtWidgets.QPlainTextEdit(parent=self.verticalLayoutWidget_3)
        self.keyless_textEdit_input.setObjectName("keyless_textEdit_input")
        self.verticalLayout_3.addWidget(self.keyless_textEdit_input)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_keyless)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 260, 431, 241))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.keyless_label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.keyless_label_2.setObjectName("keyless_label_2")
        self.verticalLayout_4.addWidget(self.keyless_label_2)
        self.keyless_textEdit_output = QtWidgets.QPlainTextEdit(parent=self.verticalLayoutWidget_4)
        self.keyless_textEdit_output.setReadOnly(True)
        self.keyless_textEdit_output.setObjectName("keyless_textEdit_output")
        self.verticalLayout_4.addWidget(self.keyless_textEdit_output)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.keyless_btn_copy = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/edit-copy.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.keyless_btn_copy.setIcon(icon)
        self.keyless_btn_copy.setObjectName("keyless_btn_copy")
        self.horizontalLayout.addWidget(self.keyless_btn_copy)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.keyless_label_warn = QtWidgets.QLabel(parent=self.tab_keyless)
        self.keyless_label_warn.setGeometry(QtCore.QRect(460, 130, 151, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keyless_label_warn.setFont(font)
        self.keyless_label_warn.setObjectName("keyless_label_warn")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_keyless)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 30, 160, 88))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.keyless_comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.keyless_comboBox.setObjectName("keyless_comboBox")
        self.keyless_comboBox.addItem("")
        self.keyless_comboBox.addItem("")
        self.keyless_comboBox.addItem("")
        self.keyless_comboBox.addItem("")
        self.keyless_comboBox.addItem("")
        self.keyless_comboBox.addItem("")
        self.keyless_comboBox.addItem("")
        self.verticalLayout.addWidget(self.keyless_comboBox)
        self.keyless_btn_encode = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/document-encrypted.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.keyless_btn_encode.setIcon(icon1)
        self.keyless_btn_encode.setObjectName("keyless_btn_encode")
        self.verticalLayout.addWidget(self.keyless_btn_encode)
        self.keyless_btn_decode = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/document-decrypt.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.keyless_btn_decode.setIcon(icon2)
        self.keyless_btn_decode.setObjectName("keyless_btn_decode")
        self.verticalLayout.addWidget(self.keyless_btn_decode)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_keyless, "")
        self.tab_symmetric = QtWidgets.QWidget()
        self.tab_symmetric.setObjectName("tab_symmetric")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_symmetric)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 30, 161, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.symmetric_comboBox_cipher = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.symmetric_comboBox_cipher.setObjectName("symmetric_comboBox_cipher")
        self.symmetric_comboBox_cipher.addItem("")
        self.symmetric_comboBox_cipher.addItem("")
        self.symmetric_comboBox_cipher.addItem("")
        self.symmetric_comboBox_cipher.addItem("")
        self.symmetric_comboBox_cipher.addItem("")
        self.verticalLayout_2.addWidget(self.symmetric_comboBox_cipher)
        self.symmetric_btn_encrypt = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.symmetric_btn_encrypt.setIcon(icon1)
        self.symmetric_btn_encrypt.setObjectName("symmetric_btn_encrypt")
        self.verticalLayout_2.addWidget(self.symmetric_btn_encrypt)
        self.symmetric_btn_decrypt = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.symmetric_btn_decrypt.setIcon(icon2)
        self.symmetric_btn_decrypt.setObjectName("symmetric_btn_decrypt")
        self.verticalLayout_2.addWidget(self.symmetric_btn_decrypt)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.symmetric_label_warn = QtWidgets.QLabel(parent=self.tab_symmetric)
        self.symmetric_label_warn.setGeometry(QtCore.QRect(460, 130, 151, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.symmetric_label_warn.setFont(font)
        self.symmetric_label_warn.setObjectName("symmetric_label_warn")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.tab_symmetric)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 431, 201))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.symmetric_label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.symmetric_label_2.setObjectName("symmetric_label_2")
        self.verticalLayout_5.addWidget(self.symmetric_label_2)
        self.symmetric_textEdit_input = QtWidgets.QPlainTextEdit(parent=self.verticalLayoutWidget_5)
        self.symmetric_textEdit_input.setObjectName("symmetric_textEdit_input")
        self.verticalLayout_5.addWidget(self.symmetric_textEdit_input)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.tab_symmetric)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 220, 431, 45))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.symmetric_label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.symmetric_label_3.setObjectName("symmetric_label_3")
        self.verticalLayout_6.addWidget(self.symmetric_label_3)
        self.symmetric_lineEdit_key = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_6)
        self.symmetric_lineEdit_key.setObjectName("symmetric_lineEdit_key")
        self.verticalLayout_6.addWidget(self.symmetric_lineEdit_key)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(parent=self.tab_symmetric)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 280, 431, 221))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.symmetric_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_7)
        self.symmetric_label.setObjectName("symmetric_label")
        self.verticalLayout_7.addWidget(self.symmetric_label)
        self.symmetric_textEdit_output = QtWidgets.QPlainTextEdit(parent=self.verticalLayoutWidget_7)
        self.symmetric_textEdit_output.setReadOnly(True)
        self.symmetric_textEdit_output.setObjectName("symmetric_textEdit_output")
        self.verticalLayout_7.addWidget(self.symmetric_textEdit_output)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.symmetric_btn_copy = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_7)
        self.symmetric_btn_copy.setIcon(icon)
        self.symmetric_btn_copy.setObjectName("symmetric_btn_copy")
        self.horizontalLayout_2.addWidget(self.symmetric_btn_copy)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(parent=self.tab_symmetric)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(480, 410, 111, 51))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.symmetric_label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_8)
        self.symmetric_label_4.setObjectName("symmetric_label_4")
        self.verticalLayout_8.addWidget(self.symmetric_label_4)
        self.symmetric_comboBox_mode = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_8)
        self.symmetric_comboBox_mode.setObjectName("symmetric_comboBox_mode")
        self.symmetric_comboBox_mode.addItem("")
        self.symmetric_comboBox_mode.addItem("")
        self.verticalLayout_8.addWidget(self.symmetric_comboBox_mode)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_symmetric, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setToolTipsVisible(False)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(parent=self.menuFile)
        self.menuExport.setTearOffEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/view-certificate-export.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuExport.setIcon(icon3)
        self.menuExport.setSeparatorsCollapsible(False)
        self.menuExport.setToolTipsVisible(False)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuCertificate = QtWidgets.QMenu(parent=self.menubar)
        self.menuCertificate.setObjectName("menuCertificate")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_OpenPGP_key_pair = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/view-certificate-add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew_OpenPGP_key_pair.setIcon(icon4)
        self.actionNew_OpenPGP_key_pair.setObjectName("actionNew_OpenPGP_key_pair")
        self.actionImport = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/view-certificate-import.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionImport.setIcon(icon5)
        self.actionImport.setObjectName("actionImport")
        self.actionPublic_Key = QtGui.QAction(parent=MainWindow)
        self.actionPublic_Key.setObjectName("actionPublic_Key")
        self.actionSecret_Key = QtGui.QAction(parent=MainWindow)
        self.actionSecret_Key.setObjectName("actionSecret_Key")
        self.actionCreate_Checksum_File = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/view-financial-account-edit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_Checksum_File.setIcon(icon6)
        self.actionCreate_Checksum_File.setObjectName("actionCreate_Checksum_File")
        self.actionVerify_Checksum_File = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/view-financial-account-checking.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionVerify_Checksum_File.setIcon(icon7)
        self.actionVerify_Checksum_File.setObjectName("actionVerify_Checksum_File")
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/application-exit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQuit.setIcon(icon8)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/file_dialog_info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDelete = QtGui.QAction(parent=MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/edit-delete-shred.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDelete.setIcon(icon10)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDatabase_Update = QtGui.QAction(parent=MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/file_dialog_contents.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDatabase_Update.setIcon(icon11)
        self.actionDatabase_Update.setObjectName("actionDatabase_Update")
        self.actionGitHub_Page = QtGui.QAction(parent=MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/github.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionGitHub_Page.setIcon(icon12)
        self.actionGitHub_Page.setObjectName("actionGitHub_Page")
        self.actionEncrypt = QtGui.QAction(parent=MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/document-edit-sign-encrypt.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionEncrypt.setIcon(icon13)
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.actionDecrypt = QtGui.QAction(parent=MainWindow)
        self.actionDecrypt.setIcon(icon2)
        self.actionDecrypt.setObjectName("actionDecrypt")
        self.actionSign = QtGui.QAction(parent=MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/document-edit-sign.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSign.setIcon(icon14)
        self.actionSign.setObjectName("actionSign")
        self.actionVerify = QtGui.QAction(parent=MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/document-edit-decrypt-verify.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionVerify.setIcon(icon15)
        self.actionVerify.setObjectName("actionVerify")
        self.actionNotepad = QtGui.QAction(parent=MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/view-pim-notes.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNotepad.setIcon(icon16)
        self.actionNotepad.setObjectName("actionNotepad")
        self.actionInfo = QtGui.QAction(parent=MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/view-certificate.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionInfo.setIcon(icon17)
        self.actionInfo.setObjectName("actionInfo")
        self.menuExport.addAction(self.actionPublic_Key)
        self.menuExport.addAction(self.actionSecret_Key)
        self.menuFile.addAction(self.actionNew_OpenPGP_key_pair)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEncrypt)
        self.menuFile.addAction(self.actionDecrypt)
        self.menuFile.addAction(self.actionSign)
        self.menuFile.addAction(self.actionVerify)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_Checksum_File)
        self.menuFile.addAction(self.actionVerify_Checksum_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionGitHub_Page)
        self.menuCertificate.addAction(self.actionInfo)
        self.menuCertificate.addSeparator()
        self.menuCertificate.addAction(self.actionDelete)
        self.menuTools.addAction(self.actionDatabase_Update)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionNotepad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCertificate.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoDog"))
        item = self.certs_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type"))
        item = self.certs_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.certs_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fingerprint"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_certs), _translate("MainWindow", "Certificates"))
        self.keyless_label.setText(_translate("MainWindow", "Input text:"))
        self.keyless_label_2.setText(_translate("MainWindow", "Output text:"))
        self.keyless_btn_copy.setText(_translate("MainWindow", "Copy"))
        self.keyless_label_warn.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.keyless_comboBox.setItemText(0, _translate("MainWindow", "Base64"))
        self.keyless_comboBox.setItemText(1, _translate("MainWindow", "MD5"))
        self.keyless_comboBox.setItemText(2, _translate("MainWindow", "SHA1"))
        self.keyless_comboBox.setItemText(3, _translate("MainWindow", "SHA256"))
        self.keyless_comboBox.setItemText(4, _translate("MainWindow", "SHA512"))
        self.keyless_comboBox.setItemText(5, _translate("MainWindow", "BLAKE2s"))
        self.keyless_comboBox.setItemText(6, _translate("MainWindow", "BLAKE2b"))
        self.keyless_btn_encode.setText(_translate("MainWindow", "Encode"))
        self.keyless_btn_decode.setText(_translate("MainWindow", "Decode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_keyless), _translate("MainWindow", "No Key"))
        self.symmetric_comboBox_cipher.setItemText(0, _translate("MainWindow", "AES128"))
        self.symmetric_comboBox_cipher.setItemText(1, _translate("MainWindow", "AES192"))
        self.symmetric_comboBox_cipher.setItemText(2, _translate("MainWindow", "AES256"))
        self.symmetric_comboBox_cipher.setItemText(3, _translate("MainWindow", "Blowfish"))
        self.symmetric_comboBox_cipher.setItemText(4, _translate("MainWindow", "DES"))
        self.symmetric_btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.symmetric_btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.symmetric_label_warn.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.symmetric_label_2.setText(_translate("MainWindow", "Input text:"))
        self.symmetric_label_3.setText(_translate("MainWindow", "Key:"))
        self.symmetric_label.setText(_translate("MainWindow", "Output text:"))
        self.symmetric_btn_copy.setText(_translate("MainWindow", "Copy"))
        self.symmetric_label_4.setText(_translate("MainWindow", "Encryption mode:"))
        self.symmetric_comboBox_mode.setItemText(0, _translate("MainWindow", "CBC"))
        self.symmetric_comboBox_mode.setItemText(1, _translate("MainWindow", "ECB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_symmetric), _translate("MainWindow", "Symmetric"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export..."))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuCertificate.setTitle(_translate("MainWindow", "Certificate"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionNew_OpenPGP_key_pair.setText(_translate("MainWindow", "New OpenPGP Key Pair..."))
        self.actionImport.setText(_translate("MainWindow", "Import..."))
        self.actionPublic_Key.setText(_translate("MainWindow", "Export Public Key..."))
        self.actionSecret_Key.setText(_translate("MainWindow", "Backup Secret Key..."))
        self.actionCreate_Checksum_File.setText(_translate("MainWindow", "Create Checksum File..."))
        self.actionVerify_Checksum_File.setText(_translate("MainWindow", "Verify Checksum File..."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDatabase_Update.setText(_translate("MainWindow", "Database Update"))
        self.actionGitHub_Page.setText(_translate("MainWindow", "GitHub Page"))
        self.actionEncrypt.setText(_translate("MainWindow", "Encrypt..."))
        self.actionDecrypt.setText(_translate("MainWindow", "Decrypt..."))
        self.actionSign.setText(_translate("MainWindow", "Sign..."))
        self.actionVerify.setText(_translate("MainWindow", "Verify..."))
        self.actionNotepad.setText(_translate("MainWindow", "Notepad..."))
        self.actionInfo.setText(_translate("MainWindow", "Details"))
