# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exporter_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_exporter_template(object):
    def setupUi(self, exporter_template):
        exporter_template.setObjectName("exporter_template")
        exporter_template.resize(302, 469)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(exporter_template)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(exporter_template)
        self.label.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBoxFormat = QtWidgets.QComboBox(exporter_template)
        self.comboBoxFormat.setObjectName("comboBoxFormat")
        self.comboBoxFormat.addItem("")
        self.comboBoxFormat.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxFormat)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(exporter_template)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.sliderFPS_Scaling = QtWidgets.QSlider(exporter_template)
        self.sliderFPS_Scaling.setEnabled(True)
        self.sliderFPS_Scaling.setMinimum(1)
        self.sliderFPS_Scaling.setMaximum(100)
        self.sliderFPS_Scaling.setSingleStep(10)
        self.sliderFPS_Scaling.setPageStep(50)
        self.sliderFPS_Scaling.setProperty("value", 10)
        self.sliderFPS_Scaling.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFPS_Scaling.setObjectName("sliderFPS_Scaling")
        self.horizontalLayout_2.addWidget(self.sliderFPS_Scaling)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(exporter_template)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setMaximum(50.0)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(exporter_template)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioAuto = QtWidgets.QRadioButton(exporter_template)
        self.radioAuto.setEnabled(True)
        self.radioAuto.setChecked(True)
        self.radioAuto.setObjectName("radioAuto")
        self.verticalLayout.addWidget(self.radioAuto)
        self.radioFromViewer = QtWidgets.QRadioButton(exporter_template)
        self.radioFromViewer.setEnabled(True)
        self.radioFromViewer.setObjectName("radioFromViewer")
        self.verticalLayout.addWidget(self.radioFromViewer)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(exporter_template)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget = ColormapListWidget(exporter_template)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdPath = QtWidgets.QLineEdit(exporter_template)
        self.lineEdPath.setObjectName("lineEdPath")
        self.horizontalLayout_4.addWidget(self.lineEdPath)
        self.btnChoosePath = QtWidgets.QPushButton(exporter_template)
        self.btnChoosePath.setMaximumSize(QtCore.QSize(31, 16777215))
        self.btnChoosePath.setObjectName("btnChoosePath")
        self.horizontalLayout_4.addWidget(self.btnChoosePath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.btnExport = QtWidgets.QPushButton(exporter_template)
        self.btnExport.setObjectName("btnExport")
        self.verticalLayout_2.addWidget(self.btnExport)

        self.retranslateUi(exporter_template)
        QtCore.QMetaObject.connectSlotsByName(exporter_template)
        exporter_template.setTabOrder(self.comboBoxFormat, self.sliderFPS_Scaling)
        exporter_template.setTabOrder(self.sliderFPS_Scaling, self.doubleSpinBox)
        exporter_template.setTabOrder(self.doubleSpinBox, self.radioAuto)
        exporter_template.setTabOrder(self.radioAuto, self.radioFromViewer)
        exporter_template.setTabOrder(self.radioFromViewer, self.listWidget)
        exporter_template.setTabOrder(self.listWidget, self.lineEdPath)
        exporter_template.setTabOrder(self.lineEdPath, self.btnChoosePath)
        exporter_template.setTabOrder(self.btnChoosePath, self.btnExport)

    def retranslateUi(self, exporter_template):
        _translate = QtCore.QCoreApplication.translate
        exporter_template.setWindowTitle(_translate("exporter_template", "Form"))
        self.label.setText(_translate("exporter_template", "Format"))
        self.comboBoxFormat.setItemText(0, _translate("exporter_template", "libx264"))
        self.comboBoxFormat.setItemText(1, _translate("exporter_template", "wmv2"))
        self.label_4.setText(_translate("exporter_template", "fps scaling"))
        self.sliderFPS_Scaling.setToolTip(_translate("exporter_template", "Speed up or slow down the framerate (only for video and gifs)"))
        self.label_3.setToolTip(_translate("exporter_template", "Lookup table min & max, only for non-tiff files."))
        self.label_3.setText(_translate("exporter_template", "LUT limits:"))
        self.radioAuto.setToolTip(_translate("exporter_template", "From meta-data (if any)"))
        self.radioAuto.setText(_translate("exporter_template", "Auto"))
        self.radioFromViewer.setToolTip(_translate("exporter_template", "From the current min & max as set in the viewer window"))
        self.radioFromViewer.setText(_translate("exporter_template", "From &viewer"))
        self.label_2.setText(_translate("exporter_template", "cmap:"))
        self.lineEdPath.setPlaceholderText(_translate("exporter_template", "path"))
        self.btnChoosePath.setText(_translate("exporter_template", "..."))
        self.btnExport.setText(_translate("exporter_template", "Export"))

from ....plotting.utils import ColormapListWidget
