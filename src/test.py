# -*- coding: utf-8 -*-

from utils import csvmanager
from model import SIR
import numpy as np
import matplotlib.pyplot as plt

# normlize a vector
def normalize(vector):
	return [v*1.0/sum(vector) for v in vector]

# plot the fitted sir model 
def plot(xdata, ydata):
	sir = SIR(xdata, ydata)
	fitted = sir.fit()
	plt.plot(xdata, ydata, 'o')
	plt.plot(xdata, fitted)
	plt.show()

# read a csv file
def read(file_name, seperator, column):
	return csvmanager.CSV_Manager().read(
		file_name=file_name,
		seperator=seperator, column=column)

# ======================================
# Example 1
data_set_1 = read(file_name="data1.csv", seperator=";", column=["Time", "I"])

ydata = np.array(data_set_1["I"], dtype=float)
xdata = np.array(data_set_1["Time"], dtype=float)
plot(xdata,ydata)
# ======================================
# Example 2
xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161])
ydata_2 = np.array([ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ])
ydata_2 = normalize(ydata_2)
xdata = np.array(xdata_2, dtype=float)
ydata = np.array(ydata_2, dtype=float)
plot(xdata,ydata)
# ======================================