#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 1 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from pyqtgraphCore.Qt import QtCore, QtGui, QtWidgets
from pyqtgraphCore import LineSegmentROI, ROI
import numpy as np
from .resize import ResizeDialogBox
from ..modules.common import ViewerInterface
from math import sqrt


class ImageMenu:
    def __init__(self, viewer_interface):
        assert isinstance(viewer_interface, ViewerInterface)
        self.vi = viewer_interface

        self.measure_line = None
        self.measure_line_ = None
        self.crop_roi = None

    def reset_scale(self):
        self.vi.update_workEnv()

    def resize(self):
        if not hasattr(self, 'resize_dialog'):
            self.resize_dialog = ResizeDialogBox(self.vi)
        self.resize_dialog.show()

    def crop(self):
        if self.crop_roi is None:
            self.vi.viewer_ref.status_bar_label.setText('Create your crop region and then click on "Crop" again in the '
                                                      '"Image" menu to crop to the selected region')
            self.crop_roi = ROI(pos=[0, 0], size=(0.5 * np.mean([self.vi.viewer_ref.image.shape[1],
                                                                 self.vi.viewer_ref.image.shape[2]])), removable=True)
            self.crop_roi.sigRemoveRequested.connect(self.remove_crop_roi)
            self.crop_roi.addScaleHandle([1, 1], [0, 0])
            self.crop_roi.addScaleHandle([0, 0], [0, 0])
            self.vi.viewer_ref.view.addItem(self.crop_roi)
        else:
            self.vi.viewer_ref.status_bar_label.setText('Cropping to your selection, please wait...')
            point_l = self.vi.viewer_ref.getImageItem().mapFromScene(self.crop_roi.getSceneHandlePositions()[1][1])
            point_r = self.vi.viewer_ref.getImageItem().mapFromScene(self.crop_roi.getSceneHandlePositions()[0][1])

            pl = (int(point_l.x()), int(point_l.y()))
            pr = (int(point_r.x()), int(point_r.y()))
            self.remove_crop_roi()

            seq = self.vi.viewer_ref.image[:, pl[1]:pr[1], pl[0]:pr[0]]
            self.vi.viewer_ref.workEnv.imgdata.seq = seq.T
            self.vi.update_workEnv()
            self.vi.viewer_ref.status_bar_label.setText('Cropping completed!')

    def remove_crop_roi(self):
        self.vi.viewer_ref.view.removeItem(self.crop_roi)
        self.crop_roi = None
        self.vi.viewer_ref.status_bar_label.clear()

    def draw_measure_line(self, ev):
        if self.measure_line_ is None:
            self.measure_line_ = self.vi.viewer_ref.view.mapSceneToView(ev.pos())
            self.vi.viewer_ref.status_bar_label.setText('Click on a second point in the image to '
                                                      'finish drawing the line')

        else:
            self.measure_line = LineSegmentROI(positions=(self.measure_line_,
                                                         self.vi.viewer_ref.view.mapSceneToView(ev.pos())))
            self.vi.viewer_ref.view.addItem(self.measure_line)

            self.vi.viewer_ref.scene.sigMouseClicked.disconnect(self.draw_measure_line)
            self.vi.viewer_ref.status_bar_label.setText('Now click "Measure" in the "Image" menu once again to get '
                                                      'your measurements')

    def measure_tool(self, ev=False):
        if self.measure_line is None:
            self.vi.viewer_ref.status_bar_label.setText('Click on a point in the image to draw the first point of a line')
            self.vi.viewer_ref.scene.sigMouseClicked.connect(self.draw_measure_line)
            return False

        elif self.measure_line is not None:
            dx = abs(self.measure_line.listPoints()[0][0] - self.measure_line.listPoints()[1][0])
            dy = abs(self.measure_line.listPoints()[0][1] - self.measure_line.listPoints()[1][1])
            dist = sqrt((dx**2 + dy**2))
            self.vi.viewer_ref.scene.removeItem(self.measure_line)
            self.measure_line = None
            self.measure_line_ = None
            QtWidgets.QMessageBox.information(None, 'Measurements',
                                              '\ndx = ' + str(dx) +\
                                              '\ndy = ' + str(dy) +\
                                              '\ndistance = ' + str(dist))
            return True