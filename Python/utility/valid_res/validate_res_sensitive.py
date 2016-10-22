# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:54:37 2016

@author: aying
"""
from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

fPath1 = '../data/validate_resolution_sensitive/Status380_210.csv'
fPath2 = '../data/validate_resolution_sensitive/Status760_420.csv'
fPath3 = '../data/validate_resolution_sensitive/Status1140_630.csv'
fPath4 = '../data/validate_resolution_sensitive/Status1520_840.csv'
fPath5 = '../data/validate_resolution_sensitive/Status1900_1050.csv'
fPath6 = '../data/validate_resolution_sensitive/Status2280_1260.csv'
fPath7 = '../data/validate_resolution_sensitive/Status2660_1470.csv'
fPath8 = '../data/validate_resolution_sensitive/Status3040_1680.csv'
fPath9 = '../data/validate_resolution_sensitive/Status3420_1890.csv'
fPath10 = '../data/validate_resolution_sensitive/Status3800_2100.csv'

'''
380_210,(12659L, 310L)
760_420,(19934L, 310L)
1140_630,(13120L, 310L)
1520_840,(10524L, 310L)
1900_1050,(74067L, 310L)
2280_1260,(7213L, 310L)
2660_1470,(6852L, 310L)
3040_1680,(11326L, 310L)
3420_1890,(8336L, 310L)
3800_2100,(6691L, 310L)
'''
list_files = [fPath1,fPath2,fPath3,fPath4,fPath5,fPath6,fPath7,fPath8,fPath9,fPath10]



def avgTime():
    '''
    list_files = glob.glob(os.path.join(vPath,'*.csv'))
    avg_dict = dict()
    startPos = 100
    endPos = 6600
    for file_ in list_files:
        data = np.loadtxt(file_,delimiter=',')
        data = data[startPos:endPos][:,-1]
        avgTime = round(np.sum(data)/(endPos - startPos),2)
        key = data[0][0]*data[0][1]
        avg_dict[key] = avgTime
    return avg_dict
    '''
    global list_files
    all_avg = []
    startPos = 100
    endPos = 6600
    for file_ in list_files:
        data = np.loadtxt(file_,delimiter=',')
        data = data[startPos:endPos][:,-1]
        avgTime = round(np.sum(data)/(endPos - startPos),2)
        all_avg.append(avgTime)
    return all_avg
    
def draw_compare_line():
    x_axis = [38*21,76*42,114*63,152*84,190*105,228*126,
              226*147,304*168,342*189,380*210]
    y_axis = avgTime()
    plt.plot(x_axis,y_axis,'ro')
    plt.show()

draw_compare_line()