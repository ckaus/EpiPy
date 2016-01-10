# -*- coding: utf-8 -*-

from epipy.utils import csvmanager
from epipy.model.sir import SIR
import numpy as np
import matplotlib.pyplot as plt

# normlize a vector
def normalize(vector):
	return [v*1.0/sum(vector) for v in vector]

def fit(xdata, ydata, model_class):
	sir = SIR(xdata,ydata)
	return sir.fit(model_class)
	
def plot(xdata, ydata_origin, ydata_result):
	plt.plot(xdata, ydata_origin, 'o')
	plt.plot(xdata, ydata_result)
	plt.show()

# read a csv file
def read(file_name, seperator, column):
	return csvmanager.CSV_Manager().read(
		file_name=file_name,
		seperator=seperator, column=column)

# ======================================
# SIR Model Classes: 1 - Susceptible, 2 - Infected, 3 - Recovered
# ======================================
# Example 1 - recovered data
data_set_1 = read(file_name="data1.csv", seperator=";", column=["Time", "S","I","R"])
ydata = np.array([data_set_1["S"],data_set_1["I"],data_set_1["R"]], dtype=float)
xdata = np.array(data_set_1["Time"], dtype=float)
result = fit(xdata,ydata, model_class=2)
plot(xdata, ydata[2,:], result)
# ======================================
# Example 2 - infected data
xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161])
ydata_2 = np.array([ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ])
ydata_2 = normalize(ydata_2)
xdata = np.array(xdata_2, dtype=float)
ydata = np.array(ydata_2, dtype=float)
result = fit(xdata,ydata, model_class=1)
plot(xdata_2, ydata_2, result)
