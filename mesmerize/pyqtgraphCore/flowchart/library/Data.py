# -*- coding: utf-8 -*-
from ...Qt import QtGui, QtCore, QtWidgets
from spyder.widgets.variableexplorer.objecteditor import oedit
from .common import *
import traceback
from functools import partial
from ....analysis import Transmission
from ....common import get_project_manager
import os


class LoadProjDF(CtrlNode):
    """Load raw project DataFrames as Transmission"""
    nodeName = 'Load_Proj_DF'
    uiTemplate = [('DF_Name', 'combo'),
                  ('Update', 'button', {'text': 'Update', 'toolTip': 'When clicked this node will update'
                                                                     ' from the project DataFrame'}),
                  ('Apply', 'check', {'applyBox': True, 'checked': False}),
                  ('PinDF', 'check', {'text': 'Yes', 'toolTip': 'Pin the DataFrame to the flowchart, this way\n'
                                                                'you can open another project and still propogate\n'
                                                                'the data from this node.'})]

    def __init__(self, name):
        CtrlNode.__init__(self, name, terminals={'Out': {'io': 'out'}})
        self._loadNode = True
        self.t = None
        child_df_names = ['root'] + list(get_project_manager().child_dataframes.keys())
        self.ctrls['DF_Name'].addItems(child_df_names)
        self.ctrls['Update'].clicked.connect(self.changed)
        # print('Node Refs:')
        # print(configuration.df_refs)

    def process(self):
        if self.ctrls['Apply'].isChecked() is False:
            return self.t

        # print('#######Weak Refs Dict########')
        # print(configuration.df_refs)

        if self.ctrls['PinDF'].isEnabled():
            if self.ctrls['PinDF'].isChecked():
                # self.t = self.t.copy()
                self.ctrls['PinDF'].setDisabled(True)
                self.ctrls['Update'].setDisabled(True)
                return {'Out': self.t}

            if self.ctrls['DF_Name'].currentText() == '':
                return
            child_df_name = self.ctrls['DF_Name'].currentText()
            if child_df_name == 'root':
                df = get_project_manager().dataframe
                filter_history = None
            else:
                df = get_project_manager().child_dataframes[child_df_name]['dataframe']
                filter_history = get_project_manager().child_dataframes[child_df_name]['filter_history']
            proj_path = get_project_manager().root_dir
            # print('*****************config df ref hex ID:*****************')
            # print(hex(id(df)))
            self.t = Transmission.from_proj(proj_path, df, sub_dataframe_name=child_df_name,
                                            dataframe_filter_history={'dataframe_filter_history': filter_history})

            # print('Tranmission dataframe hexID:')
            # print(hex(id(self.t.df)))

        return {'Out': self.t}


class LoadFile(CtrlNode):
    """Load Transmission data object from pickled file"""
    nodeName = 'LoadFile'
    uiTemplate = [('load_trn', 'button', {'text': 'Open .trn File'}),
                  ('fname', 'label', {'text': ''}),
                  ('proj_path', 'button', {'text': 'Project Path'}),
                  ('proj_path_label', 'label', {'text': ''})
                  ]

    def __init__(self, name):
        CtrlNode.__init__(self, name, terminals={'Out': {'io': 'out'}})
        self.ctrls['load_trn'].clicked.connect(self.file_dialog_trn_file)
        self.ctrls['proj_path'].clicked.connect(self.dir_dialog_proj_path)

        self.t = None
        self._loadNode = True

    def file_dialog_trn_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(None, 'Import Transmission object', '', '(*.trn)')
        if path == '':
            return
        try:
            self.t = Transmission.from_hdf5(path[0])
        except:
            QtWidgets.QMessageBox.warning(None, 'File open Error!', 'Could not open the chosen file.\n' + traceback.format_exc())
            return

        self.ctrls['fname'].setText(os.path.basename(path[0]))

        proj_path = get_project_manager().root_dir
        if proj_path is not None:
            self._set_proj_path(proj_path)

        # print(self.transmission)
        # self.update()
        self.changed()

    def _set_proj_path(self, path: str):
        self.ctrls['proj_path_label'].setText(os.path.basename(path))
        self.t.set_proj_path(path)
        self.t.set_proj_config()

    def dir_dialog_proj_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Project Folder')

        if path == '':
            return

        try:
            self._set_proj_path(path)
            self.changed()
        except (FileNotFoundError, NotADirectoryError) as e:
            QtWidgets.QMessageBox.warning(None, 'Invalid Project Folder', 'This is not a valid Mesmerize project\n' + e)
            return

    def process(self):
        self.t.get_proj_path()
        return {'Out': self.t}


class Save(CtrlNode):
    """Save Transmission data object"""
    nodeName = 'Save'
    uiTemplate = [('saveBtn', 'button', {'text': 'OpenFileDialog'}),
                  ('path', 'label', {'text' : ''}),
                  ('Apply', 'check', {'checked': False, 'applyBox': True})
                  ]

    def __init__(self, name):
        # super(Save, self).__init__(name, terminals={'data': {'io': 'in'}})
        CtrlNode.__init__(self, name, terminals={'In': {'io': 'in'}})
        self._bypass = False
        self.bypassButton = None
        self.ctrls['saveBtn'].clicked.connect(self._fileDialog)
        self._saveNode = True
        self.saveValue = None

    def process(self, In, display=True):
        if In is not None:
            self._save(In)
        else:
            raise Exception('No incoming transmission to save!')

    def _fileDialog(self):
        path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save Transmission as', '', '(*.trn)')
        if path == '':
            return
        if path[0].endswith('.trn'):
            path = path[0]
        else:
            path = path[0] + '.trn'

        self.ctrls['path'].setText(path)

    def _save(self, transmission):
        # self.ctrls['saveBtn'].clicked.connect(self._fileDialog)
        if self.ctrls['Apply'].isChecked is False:
            return

        if self.ctrls['path'].text() != '':
            try:
                transmission.to_hdf5(self.ctrls['path'].text())
            except:
                QtWidgets.QMessageBox.warning(None, 'File save error', 'Could not save the transmission to file.\n' + traceback.format_exc())


class Merge(CtrlNode):
    """Merge transmissions"""
    nodeName = 'Merge'
    uiTemplate = [('Apply', 'check', {'checked': False, 'applyBox': True})]

    def __init__(self, name):
        CtrlNode.__init__(self, name, terminals={'In': {'io': 'in', 'multi': True}, 'Out': {'io': 'out'}})

    def process(self, **kwargs):
        self.transmissions = kwargs['In']
        self.transmissions_list = merge_transmissions(self.transmissions)

        self.t = Transmission.merge(self.transmissions_list)

        return {'Out': self.t}


class ViewTransmission(CtrlNode):
    """View/Edit transmission using the spyder object editor"""
    nodeName = 'ViewData'
    uiTemplate = [('No controls', 'label')]

    # def __init__(self, name):
    #     CtrlNode.__init__(self, name, terminals={'In':})

    def processData(self, transmission: Transmission):
        self.t = transmission.copy()
        edited = oedit({'dataframe': self.t.df, 'history_trace': self.t.history_trace})
        if edited is not None:
            self.t.df = edited['dataframe']
            self.t.history_trace.add_operation('all', 'object_editor', {})

        return self.t


class DropNa(CtrlNode):
    """Drop NaNs from the DataFrame"""
    nodeName = 'DropNaNs'
    uiTemplate = [('axis', 'combo', {'values': ['row', 'columns'], 'toolTip': 'Choose to drop NaNs from according to all '
                                                                              'rows, columns, or a specific column'}),
                  ('how', 'combo', {'values': ['any', 'all'], 'toolTip': 'any: drop from chosen axis if any element is NaN\n'
                                                                         'all: drop from chosen axis if all elements are NaN'}),
                  ('Apply', 'check', {'checked': False, 'applyBox': True})]

    def __init__(self, *args, **kwargs):
        super(DropNa, self).__init__(*args, **kwargs)

    def processData(self, transmission: Transmission):
        items = ['row', 'columns'] + ['---------'] + transmission.df.columns.to_list()
        self.ctrls['axis'].setItems(items)

        if not self.ctrls['Apply'].isChecked():
            return

        self.t = transmission.copy()

        axis = self.ctrls['axis'].currentText()

        if self.ctrls['axis'].currentIndex() < 2:
            if axis == 'row':
                axis = 0
            elif axis == 'columsn':
                axis = 1

            how = self.ctrls['how'].currentText()
            self.t.df.dropna(axis=axis, how=how, inplace=True)
        else:
            how = None
            self.t.df = self.t.df[~self.t.df[axis].isna()]

        self.t.history_trace.add_operation('all', 'dropna', parameters={'axis': axis, 'how': how})

        return self.t


class iloc(CtrlNode):
    """Pass only one or multiple DataFrame Indices"""
    nodeName = 'iloc'
    uiTemplate = [('Index', 'intSpin', {'min': 0, 'step': 1, 'value': 0}),
                  ('Indices', 'lineEdit', {'text': '0', 'toolTip': 'Index numbers separated by commas'})
                  ]

    def processData(self, transmission):
        self.ctrls['Index'].setMaximum(len(transmission.df.index) - 1)
        self.ctrls['Index'].valueChanged.connect(
            partial(self.ctrls['Indices'].setText, str(self.ctrls['Index'].value())))

        indices = [int(ix.strip()) for ix in self.ctrls['Indices'].text().split(',')]
        t = transmission.copy()
        t.df = t.df.iloc[indices, :]
        t.src.append({'DF_IDX': {'indices': indices}})
        return t


class SelectRows(CtrlNode):
    pass


class SelectColumns(CtrlNode):
    pass


class TextFilter(CtrlNode):
    nodeName = 'TextFilter'
    uiTemplate = [('Column', 'combo', {'toolTip': 'Filter according to this column'}),
                  ('filter', 'lineEdit', {'toolTip': 'Filter to apply in selected column'}),
                  ('Include', 'radioBtn', {'checked': True}),
                  ('Exclude', 'radioBtn', {'checked': False}),
                  ('Apply', 'check', {'checked': False, 'applyBox': True})]

    # def __init__(self, name):
    #     CtrlNode.__init__(self, name, terminals={'In': {'io': 'in'}, 'Out': {'io': 'out', 'bypass': 'In'}})
    #     self.ctrls['ROI_Type'].returnPressed.connect(self._setAvailTags)

    def processData(self, transmission):
        self.ctrls['Column'].setItems(transmission.df.columns.to_list())
        col = self.ctrls['Column'].currentText()
        completer = QtWidgets.QCompleter(list(map(str, transmission.df[col].unique())))
        self.ctrls['filter'].setCompleter(completer)

        if self.ctrls['Apply'].isChecked() is False:
            return

        filt = self.ctrls['filter'].text()

        self.t = transmission.copy()

        include = self.ctrls['Include'].isChecked()
        exclude = self.ctrls['Exclude'].isChecked()

        params = {'column': col,
                  'filter': filt,
                  'include': include,
                  'exclude': exclude
                  }

        if include:
            self.t.df = self.t.df[self.t.df[col].astype(str) == filt]
        elif exclude:
            self.t.df = self.t.df[self.t.df[col].astype(str) != filt]

        self.t.df = self.t.df.reset_index(drop=True)

        self.t.history_trace.add_operation('all', operation='text_filter', parameters=params)

        return self.t


class SpliceArrays(CtrlNode):
    """Splice 1-D numpy arrays in a particular column."""
    nodeName = 'SpliceArrays'
    uiTemplate = [('Apply', 'check', {'checked': True, 'applyBox': True}),
                  ('data_column', 'combo', {}),
                  ('indices', 'lineEdit', {'text': '', 'placeHolder': 'start_ix:end_ix'})]

    def processData(self, transmission: Transmission):
        self.t = transmission
        self.set_data_column_combo_box()

        if self.ctrls['Apply'].isChecked() is False:
            return

        self.t = transmission.copy()
        indices = self.ctrls['indices'].text()

        if indices == '':
            return
        if ':' not in indices:
            return
        else:
            indices = indices.split(':')

        start_ix = int(indices[0])
        end_ix = int(indices[1])

        data_column = self.ctrls['data_column'].currentText()
        output_column = '_SPLICE_ARRAYS'

        self.t.df[output_column] = self.t.df[data_column].apply(lambda a: a[start_ix:end_ix])

        params = {'data_column': data_column,
                  'start_ix': start_ix,
                  'end_ix': end_ix,
                  'units': self.t.last_unit
                  }

        self.t.history_trace.add_operation(data_block_id='all', operation='splice_arrays', parameters=params)
        self.t.last_output = output_column

        return self.t