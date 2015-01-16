# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 21:03:55 2015

TO GENERATE PYTHON FILE:    <pyside-uic -o Fluoro4GUI.py Fluoro4GUI.ui>
TO RUN FROM TERMIAL:        <python Fluoro4_app.py>

@author: Dan
"""
import sys, os
import numpy as np
from PySide import QtGui, QtCore
import fluoro4 as mathyShit
import Fluoro4GUI as prettyShit      

# ===========================================================================
#   Setup main window & Make connections b/w GUI and back-end code
#   TUTORIAL: http://qt-project.org/wiki/QtCreator_and_PySide
#   TUTORIAL: http://qt-project.org/wiki/Signals_and_Slots_in_PySide
# ===========================================================================
class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui =  prettyShit.Ui_MainWindow()
        self.ui.setupUi(self)
        
        # CONSTANTS
        self.ALPHA = 100
        self.PLOTDIM_X = [300, 800]
        self.PLOTDIM_Y = [-10, 100]
        
        
        # Get plottable data
        self.getFilters()
        self.getDyes()
        self.colorDict = {'Blue': (31, 119, 180),
                           'Light Blue': (174, 199, 232),
                           'Orange': (255, 127, 14),
                           'Light Orange': (255, 187, 120),
                           'Green': (44, 160, 44),
                           'Light Green': (152, 223, 138),
                           'Red': (214, 39, 40),
                           'Light Red': (255, 152, 150),
                           'Purple': (148, 103, 189),
                           'Light Purple': (197, 176, 213),
                           'Brown': (140, 86, 75),
                           'Light Brown': (196, 156, 148),
                           'Pink': (227, 119, 194),
                           'Light Pink': (247, 182, 210),
                           'Gray': (127, 127, 127),
                           'Light Gray': (199, 199, 199),
                           'Light Olive': (188, 189, 34),
                           'Light Olive': (219, 219, 141),
                           'Aqua': (23, 190, 207),
                           'Light Aqua': (158, 218, 229)}
                       
        # Make External Connections
        self.setupSpectraUtils()
        self.setupFilterUtils()
        self.setupPlot()
        
    def getFilters(self, subfolder='/Filters/'):
        filter_path = os.getcwd()
        filepath = filter_path + subfolder
        filename = os.listdir(filepath)[0]
        filters = mathyShit.readFilters(filename, filepath)
        self.filterDict = {}
        for filt in filters:
            self.filterDict[filt[0]] = (filt[1], filt[2])
        return True
        
    def getDyes(self, subfolder='/Dyes/'):
        filter_path = os.getcwd()
        filepath = filter_path + subfolder
        dye_files = os.listdir(filepath)
        self.dyeDict = {}
        for dye in dye_files:
            dye_data = mathyShit.readData(dye, filepath)
            self.dyeDict[dye_data['name'][0]] = [dye_data['wavelength'], 
                                                 dye_data['excitation'],
                                                 dye_data['emission']]
        return True
        
    def setupSpectraUtils(self):
        # Setup toggle spectra options #1
        QtCore.QObject.connect(self.ui.checkBox, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox.addItems(self.dyeDict.keys())        
        QtCore.QObject.connect(self.ui.checkBox_6, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.checkBox_7, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_6, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_6.addItems(self.colorDict.keys())
        
        # Setup toggle spectra options #2
        QtCore.QObject.connect(self.ui.checkBox_2, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_2, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_2.addItems(self.dyeDict.keys())
        QtCore.QObject.connect(self.ui.checkBox_9, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.checkBox_8, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_7, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_7.addItems(self.colorDict.keys())
        
        # Setup toggle spectra options #3
        QtCore.QObject.connect(self.ui.checkBox_3, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_4, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_4.addItems(self.dyeDict.keys())
        QtCore.QObject.connect(self.ui.checkBox_11, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.checkBox_10, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_8, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_8.addItems(self.colorDict.keys())
        
        # Setup toggle spectra options #4
        QtCore.QObject.connect(self.ui.checkBox_4, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_3, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_3.addItems(self.dyeDict.keys())
        QtCore.QObject.connect(self.ui.checkBox_12, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.checkBox_13, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_9, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_9.addItems(self.colorDict.keys())
        
        # Setup toggle spectra options #5
        QtCore.QObject.connect(self.ui.checkBox_5, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_5, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_5.addItems(self.dyeDict.keys())
        QtCore.QObject.connect(self.ui.checkBox_14, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.checkBox_15, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_10, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_10.addItems(self.colorDict.keys())

        return True
        
    def setupFilterUtils(self):
        # Setup toggle filter options #1
        QtCore.QObject.connect(self.ui.checkBox_19, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_11, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_11.addItems(self.filterDict.keys())
        QtCore.QObject.connect(self.ui.comboBox_19, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_19.addItems(self.colorDict.keys())
        
        # Setup toggle filter options #2
        QtCore.QObject.connect(self.ui.checkBox_17, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_12, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_12.addItems(self.filterDict.keys())
        QtCore.QObject.connect(self.ui.comboBox_18, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_18.addItems(self.colorDict.keys())
        
        # Setup toggle filter options #3
        QtCore.QObject.connect(self.ui.checkBox_20, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_13, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_13.addItems(self.filterDict.keys())
        QtCore.QObject.connect(self.ui.comboBox_17, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_17.addItems(self.colorDict.keys())
        
        # Setup toggle filter options #4
        QtCore.QObject.connect(self.ui.checkBox_18, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_14, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_14.addItems(self.filterDict.keys())
        QtCore.QObject.connect(self.ui.comboBox_20, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_20.addItems(self.colorDict.keys())
        
        # Setup toggle filter options #5
        QtCore.QObject.connect(self.ui.checkBox_16, QtCore.SIGNAL("clicked(bool)"), self.updatePlot)
        QtCore.QObject.connect(self.ui.comboBox_15, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_15.addItems(self.filterDict.keys())
        QtCore.QObject.connect(self.ui.comboBox_16, QtCore.SIGNAL("currentIndexChanged(int)"), self.updatePlot)
        self.ui.comboBox_16.addItems(self.colorDict.keys())
        
        return True
        
    def setupPlot(self):
        self.ui.graphicsView.setMouseEnabled(x=True, y=False)
        self.ui.graphicsView.setRange(xRange=self.PLOTDIM_X, yRange=self.PLOTDIM_Y)
        self.ui.graphicsView.setBackground('w')
        self.ui.graphicsView.setLabel('bottom', text='Wavelength', units='nm')
        self.ui.graphicsView.setLabel('left', text='Relative Intensity', units='AU')
        return True
        
    def updatePlot(self):
        self.clearPlot()
        if self.ui.checkBox.isChecked():
            if self.ui.checkBox_6.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox.currentText()][0],
                                          self.dyeDict[self.ui.comboBox.currentText()][1],
                                          pen=self.colorDict[self.ui.comboBox_6.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_6.currentText()] + (self.ALPHA/3,),
                                          fillLevel=-0.3) 
            
            if self.ui.checkBox_7.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox.currentText()][0],
                                          self.dyeDict[self.ui.comboBox.currentText()][2],
                                          pen=self.colorDict[self.ui.comboBox_6.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_6.currentText()] + (self.ALPHA,),
                                          fillLevel=-0.3)
                
        if self.ui.checkBox_2.isChecked():
            if self.ui.checkBox_9.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_2.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_2.currentText()][1],
                                          pen=self.colorDict[self.ui.comboBox_7.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_7.currentText()] + (self.ALPHA/3,),
                                          fillLevel=-0.3)
            if self.ui.checkBox_8.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_2.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_2.currentText()][2],
                                          pen=self.colorDict[self.ui.comboBox_7.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_7.currentText()] + (self.ALPHA,),
                                          fillLevel=-0.3)
                                          
        if self.ui.checkBox_3.isChecked():
            if self.ui.checkBox_11.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_4.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_4.currentText()][1],
                                          pen=self.colorDict[self.ui.comboBox_8.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_8.currentText()] + (self.ALPHA/3,),
                                          fillLevel=-0.3)
            if self.ui.checkBox_10.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_4.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_4.currentText()][2],
                                          pen=self.colorDict[self.ui.comboBox_8.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_8.currentText()] + (self.ALPHA,),
                                          fillLevel=-0.3)
                                          
        if self.ui.checkBox_4.isChecked():
            if self.ui.checkBox_12.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_3.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_3.currentText()][1],
                                          pen=self.colorDict[self.ui.comboBox_9.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_9.currentText()] + (self.ALPHA/3,),
                                          fillLevel=-0.3)
            if self.ui.checkBox_13.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_3.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_3.currentText()][2],
                                          pen=self.colorDict[self.ui.comboBox_9.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_9.currentText()] + (self.ALPHA,),
                                          fillLevel=-0.3)
                                          
        if self.ui.checkBox_5.isChecked():
            if self.ui.checkBox_14.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_5.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_5.currentText()][1],
                                          pen=self.colorDict[self.ui.comboBox_10.currentText()],
                                          brush=self.colorDict[self.ui.comboBox_10.currentText()] + (self.ALPHA/3,),
                                          fillLevel=-0.3)
            if self.ui.checkBox_15.isChecked():
                self.ui.graphicsView.plot(self.dyeDict[self.ui.comboBox_5.currentText()][0],
                                          self.dyeDict[self.ui.comboBox_5.currentText()][2],
                                          pen=self.colorDict[self.ui.comboBox_10.currentText()])
                                          
        if self.ui.checkBox_19.isChecked():
            self.addFilterROI(self.filterDict[self.ui.comboBox_11.currentText()][0][0],
                              self.filterDict[self.ui.comboBox_11.currentText()][0][1], 
                              self.colorDict[self.ui.comboBox_19.currentText()])
            self.addFilterROI(self.filterDict[self.ui.comboBox_11.currentText()][1][0],
                              self.filterDict[self.ui.comboBox_11.currentText()][1][1],
                              self.colorDict[self.ui.comboBox_19.currentText()])
                              
        if self.ui.checkBox_17.isChecked():
            self.addFilterROI(self.filterDict[self.ui.comboBox_12.currentText()][0][0],
                              self.filterDict[self.ui.comboBox_12.currentText()][0][1], 
                              self.colorDict[self.ui.comboBox_18.currentText()])
            self.addFilterROI(self.filterDict[self.ui.comboBox_12.currentText()][1][0],
                              self.filterDict[self.ui.comboBox_12.currentText()][1][1],
                              self.colorDict[self.ui.comboBox_18.currentText()])
                              
        if self.ui.checkBox_20.isChecked():
            self.addFilterROI(self.filterDict[self.ui.comboBox_13.currentText()][0][0],
                              self.filterDict[self.ui.comboBox_13.currentText()][0][1], 
                              self.colorDict[self.ui.comboBox_17.currentText()])
            self.addFilterROI(self.filterDict[self.ui.comboBox_13.currentText()][1][0],
                              self.filterDict[self.ui.comboBox_13.currentText()][1][1],
                              self.colorDict[self.ui.comboBox_17.currentText()])
                              
        if self.ui.checkBox_18.isChecked():
            self.addFilterROI(self.filterDict[self.ui.comboBox_14.currentText()][0][0],
                              self.filterDict[self.ui.comboBox_14.currentText()][0][1], 
                              self.colorDict[self.ui.comboBox_20.currentText()])
            self.addFilterROI(self.filterDict[self.ui.comboBox_14.currentText()][1][0],
                              self.filterDict[self.ui.comboBox_14.currentText()][1][1],
                              self.colorDict[self.ui.comboBox_20.currentText()])
                              
        if self.ui.checkBox_16.isChecked():
            self.addFilterROI(self.filterDict[self.ui.comboBox_15.currentText()][0][0],
                              self.filterDict[self.ui.comboBox_15.currentText()][0][1], 
                              self.colorDict[self.ui.comboBox_16.currentText()])
            self.addFilterROI(self.filterDict[self.ui.comboBox_15.currentText()][1][0],
                              self.filterDict[self.ui.comboBox_15.currentText()][1][1],
                              self.colorDict[self.ui.comboBox_16.currentText()])
        return True
        
    def addFilterROI(self, leftBound, rightBound, colorOpt):
        self.ui.graphicsView.plot(np.linspace(leftBound, rightBound, 101), 
                                  [self.PLOTDIM_Y[1]]*np.ones(101),
                                   brush=colorOpt + (self.ALPHA,), 
                                   fillLevel=-0.3)
        
    def clearPlot(self):
        self.ui.graphicsView.clear()
        return True
        
        
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
