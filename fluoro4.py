# -*- coding: utf-8 -*-
"""
EXCITATION:EMISSION.py

Data from: https://www.lifetechnologies.com/us/en/home/life-science/cell-analysis/labeling-chemistry/fluorescence-spectraviewer.html?ICID=svtool&UID=Di-4-ANEPPS
Created on Tue Jan  6 11:16:47 2015

@author: Dan
"""
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg

def readData(filename, filepath, delimiter=','):
    f = open(filepath + filename)
    fline = f.readlines()
    f.close()
    if len(fline) == 1:
        fline = fline[0].split('\r')    
    data = []
    for line in fline:
        if line[0] != ';':
            [wavelength, excitation, emission] = line.split(delimiter)
            data.append([wavelength, excitation, emission])
    data = np.array(data)
    data = {'data': data, 
            'wavelength': [float(i) for i in data[:, 0]], 
            'excitation': [float(i) for i in data[:, 1]], 
            'emission': [float(i) for i in data[:, 2]], 
            'name': filename.split('.csv')}
    return data
    
def readFilters(filename, filepath='', delimiter =','):
    f = open(filepath + filename)
    fline = f.readlines()
    f.close()
    if len(fline) == 1:
        fline = fline[0].split('\r')    
    filters = []
    for line in fline:
        if line[0] != ';':
            [position, name, excitation_center, excitation_width, dichroic, emission_center, emission_width] = line.split(delimiter)
            filters.append([name, 
                         (np.float(excitation_center)-np.float(excitation_width)/2, np.float(excitation_center)+np.float(excitation_width)/2), 
                         (np.float(emission_center)-np.float(emission_width)/2, np.float(emission_center)+np.float(emission_width)/2)])
    return filters  
    
def ExEmGraph(filter_list, fluorophore_list, color_code, filepath):
    delimiter = ','
    color_counter = 0
    for fluoro in fluorophore_list:
        data = readData(fluoro + '.csv', filepath, delimiter)
        plt.plot(data['wavelength'], data['excitation'], '--', 
                              color=color_code[color_counter],
                              label = fluoro + ' excitation')
        plt.plot(data['wavelength'], data['emission'], 
                            color=color_code[color_counter],
                            label = fluoro + ' emission')
        plt.fill_between(data['wavelength'].astype(float), data['emission'].astype(float), 
                         0, 
                         alpha=0.25, 
                         color=color_code[color_counter])
        color_counter = color_counter + 1
    plt.legend(fontsize=10, loc=3, ncol=len(fluorophore_list))
#    filters = readFilters(filter_list, filepath, delimiter)
#    for i in filters:
#        plt.axvspan(i[1][0], i[1][1], facecolor='gray', alpha=0.5)
    plt.xlim([300, 850])
    plt.ylim([-20, 100])
    return True
    
def pgExEmGraph(fluorophore_list, filepath):
    delimiter = ','
    i = 0
    win1 = pg.GraphicsWindow(title='Bulk Data')
    win1.resize(1200,300)
    win1.setWindowTitle('Fluorophore Intensity vs. Wavelength')
    tot_plot = win1.addPlot(title='Region Selection')
    for i in range(len(fluorophore_list)):
        data = readData(fluorophore_list[i] + '.csv', filepath, delimiter)
        tot_plot.plot(data['wavelength'].astype(float), data['excitation'].astype(float), pen = (i, len(fluorophore_list)), brush = '--')
        tot_plot.plot(data['wavelength'].astype(float), data['emission'].astype(float), pen = (i, len(fluorophore_list)))
    lr = pg.LinearRegionItem([50,100])
    lr.setZValue(-10)
    tot_plot.addItem(lr)
    tot_plot.setLabel('left', 'Intensity', units='AU')
    tot_plot.setLabel('bottom', 'Wavelength', units='nm')
    pg.show(tot_plot)
    return True
    
if __name__ == '__main__':
    filepath = '/Users/Dan/Documents/Grad School/Lab/Fluorophore Excitation:Emission/Dyes/'
    filter_list = 'Filters.csv' 
    fluorophore_list = ['mCherry', 'YFP', 'DAPI', 'GFP (emerald GFP)', 'Di-4-ANEPPS']
    color_code = ['r', 'y', 'b', 'g', 'gray'] 
    fluorophore_list = ['Di-4-ANEPPS']  
    ExEmGraph(filter_list, fluorophore_list, color_code, filepath)
#    pgExEmGraph(fluorophore_list, filepath)
    exit