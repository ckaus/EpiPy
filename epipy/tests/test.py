# -*- coding: utf-8 -*-

from epipy.utils import csvmanager
from epipy.model.sir import SIR
import numpy as np
import matplotlib.pyplot as plt

# normlize a vector
def normalize(vector):
	return [v*1.0/sum(vector) for v in vector]

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
# # Example 1 - infected data + curve fit
data_set_1 = read(file_name="data1.csv", seperator=";", column=["Time", "I"])
ydata = np.array(data_set_1["I"], dtype=float)
xdata = np.array(data_set_1["Time"], dtype=float)
sir = SIR(xdata, ydata)
result = sir.fit()
plot(xdata, ydata, result)
# ======================================
# Example 2 - infected data - with beta=0.20559662 , gamma = 0.11329991 for best fit
xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161],dtype=float)
ydata_2 = np.array(normalize([ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ]), dtype=float)
sir = SIR(xdata_2, ydata_2)
result = sir.fit(beta=0.20559662, gamma=0.11329991)
plot(xdata_2, ydata_2, result)