# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/window_pytemplate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1231, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listWidgetDataColumns = QtWidgets.QListWidget(self.groupBox)
        self.listWidgetDataColumns.setAlternatingRowColors(True)
        self.listWidgetDataColumns.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidgetDataColumns.setObjectName("listWidgetDataColumns")
        self.verticalLayout_2.addWidget(self.listWidgetDataColumns)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButtonGroupBySingleColumn = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonGroupBySingleColumn.setMaximumSize(QtCore.QSize(16, 16777215))
        self.radioButtonGroupBySingleColumn.setText("")
        self.radioButtonGroupBySingleColumn.setChecked(True)
        self.radioButtonGroupBySingleColumn.setObjectName("radioButtonGroupBySingleColumn")
        self.horizontalLayout_3.addWidget(self.radioButtonGroupBySingleColumn)
        self.comboBoxGrouping = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxGrouping.setObjectName("comboBoxGrouping")
        self.horizontalLayout_3.addWidget(self.comboBoxGrouping)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButtonGroupByTransmissions = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonGroupByTransmissions.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.radioButtonGroupByTransmissions.setObjectName("radioButtonGroupByTransmissions")
        self.horizontalLayout_4.addWidget(self.radioButtonGroupByTransmissions)
        self.btnSetIncomingTransmissionsNames = QtWidgets.QPushButton(self.groupBox)
        self.btnSetIncomingTransmissionsNames.setObjectName("btnSetIncomingTransmissionsNames")
        self.horizontalLayout_4.addWidget(self.btnSetIncomingTransmissionsNames)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.btnEditColor = QtWidgets.QPushButton(self.groupBox)
        self.btnEditColor.setObjectName("btnEditColor")
        self.verticalLayout_2.addWidget(self.btnEditColor)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBoxUUIDColumn = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxUUIDColumn.setObjectName("comboBoxUUIDColumn")
        self.verticalLayout_2.addWidget(self.comboBoxUUIDColumn)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBoxSpecific = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBoxSpecific.sizePolicy().hasHeightForWidth())
        self.groupBoxSpecific.setSizePolicy(sizePolicy)
        self.groupBoxSpecific.setObjectName("groupBoxSpecific")
        self.verticalLayout_3.addWidget(self.groupBoxSpecific)
        self.btnApplyAll = QtWidgets.QPushButton(self.widget)
        self.btnApplyAll.setObjectName("btnApplyAll")
        self.verticalLayout_3.addWidget(self.btnApplyAll)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout_4.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1231, 23))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockConsole = QtWidgets.QDockWidget(MainWindow)
        self.dockConsole.setObjectName("dockConsole")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockConsole.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockConsole)
        self.actionConsole = QtWidgets.QAction(MainWindow)
        self.actionConsole.setCheckable(True)
        self.actionConsole.setObjectName("actionConsole")
        self.actionLive_datapoint_tracer = QtWidgets.QAction(MainWindow)
        self.actionLive_datapoint_tracer.setCheckable(False)
        self.actionLive_datapoint_tracer.setObjectName("actionLive_datapoint_tracer")
        self.menuView.addAction(self.actionConsole)
        self.menuView.addAction(self.actionLive_datapoint_tracer)
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        self.actionConsole.toggled['bool'].connect(self.dockConsole.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Plot controls"))
        self.label.setText(_translate("MainWindow", "Data columns"))
        self.label_2.setText(_translate("MainWindow", "Group based on:"))
        self.radioButtonGroupByTransmissions.setText(_translate("MainWindow", "Incoming transmissions"))
        self.btnSetIncomingTransmissionsNames.setText(_translate("MainWindow", "Set Names"))
        self.btnEditColor.setText(_translate("MainWindow", "Edit colors"))
        self.label_3.setText(_translate("MainWindow", "UUID column:"))
        self.groupBoxSpecific.setTitle(_translate("MainWindow", "More controls"))
        self.btnApplyAll.setText(_translate("MainWindow", "Apply All"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.dockConsole.setWindowTitle(_translate("MainWindow", "Console: Plot Window"))
        self.actionConsole.setText(_translate("MainWindow", "Console"))
        self.actionLive_datapoint_tracer.setText(_translate("MainWindow", "Live datapoint tracer"))

