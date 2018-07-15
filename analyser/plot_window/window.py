#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 14 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from .pytemplates.window_pytemplate import *
import pandas as pd
from .. import DataTypes
import pickle
import scipy
from pyqtgraphCore import GraphicsLayoutWidget, mkColor
from pyqtgraphCore.console import ConsoleWidget
from matplotlib import cm as matplotlib_color_map
import numpy as np
import os


class PlotWindow(QtWidgets.QMainWindow):
    # __metaclass__ = abc.ABCMeta
    signal_params_updated = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(PlotWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.transmissions = None
        self.dataframe = pd.DataFrame()
        self.data_columns = []
        self.groups = []
        self.group_dataframes = []
        self.uuid_column = ''

        self.graphicsViews = {}

        self.ui.btnApplyAll.clicked.connect(self.update_params)

        ns = {'np': np,
              'pickle': pickle,
              'scipy': scipy,
              'pd': pd,
              'DataTypes': DataTypes,
              'graphicsViews': self.graphicsViews,
              'main': self,
              }

        txt = "Namespaces:\n" \
              "pickle as pickle\n" \
              "numpy as 'np'\n" \
              "scipy as 'scipy'\n" \
              "pd as pandas\n" \
              "graphicsViews (plot tabs) as graphicsViews\n" \
              "self as 'main'\n\n" \

        # if not os.path.exists(configuration.sys_cfg_path + '/console_history/'):
        #     os.makedirs(configuration.sys_cfg_path + '/console_history')
        #
        # cmd_history_file = configuration.sys_cfg_path + '/console_history/plot_window.pik'

        self.ui.dockConsole.setWidget(ConsoleWidget(namespace=ns, text=txt)) #,historyFile=cmd_history_file))

        self.ui.dockConsole.hide()

    @property
    def status_bar(self) -> QtWidgets.QStatusBar:
        return self.statusBar()

    def update_input_transmissions(self, transmissions: list):
        self.transmissions = transmissions

        dfs = [t.df for t in self.transmissions]

        self.dataframe = pd.concat(dfs)#, axis=1)
        self.dataframe.reset_index(inplace=True)
        self.dataframe.drop(columns=['index'], inplace=True)
        self.dataframe = self.dataframe.sample(n=100, axis=0)

        columns = self.dataframe.columns.tolist()

        self.ui.listWidgetDataColumns.addItems(columns)

        self.ui.comboBoxGrouping.clear()
        self.ui.comboBoxGrouping.addItems(columns)

        self.ui.comboBoxUUIDColumn.clear()
        self.ui.comboBoxUUIDColumn.addItems(columns)
        self.ui.comboBoxUUIDColumn.setCurrentIndex(columns.index(next(column for column in columns if 'uuid' in column)))

    def add_plot_tab(self, title: str):
        self.graphicsViews.update({title: GraphicsLayoutWidget(parent=self.ui.tabWidget)})
        self.ui.tabWidget.addTab(self.graphicsViews[title], title)
        i = self.ui.tabWidget.count() - 1
        self.ui.tabWidget.widget(i).setLayout(QtWidgets.QVBoxLayout())

    def update_params(self):
        self.data_columns = [item.text() for item in self.ui.listWidgetDataColumns.selectedItems()]
        if self.ui.radioButtonGroupBySingleColumn.isChecked():
            grouping_column = self.ui.comboBoxGrouping.currentText()
            self.groups = list(set(self.dataframe[grouping_column].tolist()))
        else:
            return
        self.group_dataframes = [self.dataframe[self.dataframe[grouping_column] == group] for group in self.groups]

        self.uuid_column = self.ui.comboBoxUUIDColumn.currentText()

    def auto_colormap(self, number_of_colors: int, color_map: str = 'hsv') -> list:
        cm = matplotlib_color_map.get_cmap(color_map)
        cm._init()
        lut = (cm._lut * 255).view(np.ndarray)
        cm_ixs = np.linspace(0, 210, number_of_colors, dtype=int)

        colors = []
        for ix in range(number_of_colors):
            c = lut[cm_ixs[ix]]
            colors.append(mkColor(c))
        return colors
