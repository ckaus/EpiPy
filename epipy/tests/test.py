# -*- coding: utf-8 -*-

from epipy.utils import csvmanager
from epipy.model import SIR, SISwbad, SIS, SIRwbad, SIRS, SEIR
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


xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161],dtype=float)
ydata_2 = np.array(normalize([ 113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380 ]), dtype=float)
# ======================================
# SIR
# data_set_1 = read(file_name="data1.csv", seperator=";", column=["Time", "I"])
# ydata = np.array(data_set_1["I"], dtype=float)
# xdata = np.array(data_set_1["Time"], dtype=float)
# sir = SIR(xdata, ydata)
# plot(xdata, ydata, sir.fit())
# ==================================
# SIR
# sir = SIR(xdata_2, ydata_2)
# plot(xdata_2, ydata_2, sir.fit())
# plot(xdata_2, ydata_2, sir.fit(beta=0.20559679, gamma=0.11329998))
# ==================================
# SIRwbad - with births and deaths
# sirwbad = SIRwbad(xdata_2, ydata_2)
# plot(xdata_2, ydata_2, sirwbad.fit())
# plot(xdata_2, ydata_2, sirwbad.fit(beta=0.22931843, gamma=0.12404889, mu=0.00879885))
# ==================================
# SIS
# sis = SIS(xdata_2, ydata_2)
# plot(xdata_2, ydata_2, sis.fit())
# plot(xdata_2, ydata_2, sis.fit(beta=0.20559639, gamma=0.11329984))
# ==================================
# SIS - with births and deaths
# siswbad = SISwbad(xdata_2, ydata_2)
# plot(xdata_2, ydata_2, siswbad.fit())
# plot(xdata_2, ydata_2, siswbad.fit(beta=0.20559639, gamma=0.11329984, mu=0.045))
# ==================================
# SIRS
# sirs = SIRS(xdata_2, ydata_2)
# plot(xdata_2, ydata_2, sirs.fit())
# plot(xdata_2, ydata_2, sirs.fit( beta=0.22931856, gamma=0.12404895, mu=0.00879889, f=0.0)) 
# ==================================