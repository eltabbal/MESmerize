# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './preferences_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(663, 450)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.plainTextEditOtherCommands = QtWidgets.QPlainTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEditOtherCommands.sizePolicy().hasHeightForWidth())
        self.plainTextEditOtherCommands.setSizePolicy(sizePolicy)
        self.plainTextEditOtherCommands.setPlainText("")
        self.plainTextEditOtherCommands.setObjectName("plainTextEditOtherCommands")
        self.gridLayout.addWidget(self.plainTextEditOtherCommands, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxCores = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxCores.sizePolicy().hasHeightForWidth())
        self.spinBoxCores.setSizePolicy(sizePolicy)
        self.spinBoxCores.setMinimum(1)
        self.spinBoxCores.setMaximum(999)
        self.spinBoxCores.setObjectName("spinBoxCores")
        self.horizontalLayout.addWidget(self.spinBoxCores)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditCaimanPath = QtWidgets.QLineEdit(Form)
        self.lineEditCaimanPath.setReadOnly(True)
        self.lineEditCaimanPath.setObjectName("lineEditCaimanPath")
        self.horizontalLayout_2.addWidget(self.lineEditCaimanPath)
        self.btnCaimanPath = QtWidgets.QPushButton(Form)
        self.btnCaimanPath.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btnCaimanPath.setObjectName("btnCaimanPath")
        self.horizontalLayout_2.addWidget(self.btnCaimanPath)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEditAnacondaPath = QtWidgets.QLineEdit(Form)
        self.lineEditAnacondaPath.setReadOnly(True)
        self.lineEditAnacondaPath.setObjectName("lineEditAnacondaPath")
        self.horizontalLayout_3.addWidget(self.lineEditAnacondaPath)
        self.btnAnacondaPath = QtWidgets.QPushButton(Form)
        self.btnAnacondaPath.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btnAnacondaPath.setObjectName("btnAnacondaPath")
        self.horizontalLayout_3.addWidget(self.btnAnacondaPath)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEditAnacondaEnvName = QtWidgets.QLineEdit(Form)
        self.lineEditAnacondaEnvName.setObjectName("lineEditAnacondaEnvName")
        self.horizontalLayout_4.addWidget(self.lineEditAnacondaEnvName)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnReloadConfigFile = QtWidgets.QPushButton(Form)
        self.btnReloadConfigFile.setObjectName("btnReloadConfigFile")
        self.horizontalLayout_5.addWidget(self.btnReloadConfigFile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnClose = QtWidgets.QPushButton(Form)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_5.addWidget(self.btnClose)
        self.btnApply = QtWidgets.QPushButton(Form)
        self.btnApply.setObjectName("btnApply")
        self.horizontalLayout_5.addWidget(self.btnApply)
        self.gridLayout.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)
        self.plainTextEditEnvironmentVariables = QtWidgets.QPlainTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEditEnvironmentVariables.sizePolicy().hasHeightForWidth())
        self.plainTextEditEnvironmentVariables.setSizePolicy(sizePolicy)
        self.plainTextEditEnvironmentVariables.setPlainText("")
        self.plainTextEditEnvironmentVariables.setObjectName("plainTextEditEnvironmentVariables")
        self.gridLayout.addWidget(self.plainTextEditEnvironmentVariables, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.spinBoxCores, self.lineEditCaimanPath)
        Form.setTabOrder(self.lineEditCaimanPath, self.btnCaimanPath)
        Form.setTabOrder(self.btnCaimanPath, self.lineEditAnacondaPath)
        Form.setTabOrder(self.lineEditAnacondaPath, self.btnAnacondaPath)
        Form.setTabOrder(self.btnAnacondaPath, self.lineEditAnacondaEnvName)
        Form.setTabOrder(self.lineEditAnacondaEnvName, self.btnReloadConfigFile)
        Form.setTabOrder(self.btnReloadConfigFile, self.btnClose)
        Form.setTabOrder(self.btnClose, self.btnApply)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Environment variables, one per line"))
        self.label.setText(_translate("Form", "Maximum number of cores to use:"))
        self.label_2.setText(_translate("Form", "CaImAn directory path"))
        self.btnCaimanPath.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "anaconda3 directory path"))
        self.btnAnacondaPath.setText(_translate("Form", "..."))
        self.label_4.setText(_translate("Form", "anaconda3 environment name"))
        self.btnReloadConfigFile.setText(_translate("Form", "Reload Config File"))
        self.btnClose.setText(_translate("Form", "Close"))
        self.btnApply.setText(_translate("Form", "Apply"))
        self.label_5.setText(_translate("Form", "Environment variables, one per line"))
        self.label_7.setText(_translate("Form", "Other commands to run before lauching batch items"))
