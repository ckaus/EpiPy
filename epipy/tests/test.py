# -*- coding: utf-8 -*-

from epipy.utils import csvmanager
from epipy.model import SIR, SIRwbad, SIS, SISwbad, SIRS
import numpy as np
import matplotlib.pyplot as plt


# normalize a vector
def normalize(vector):
    return [v * 1.0 / sum(vector) for v in vector]


def plot(xdata, ydata_origin, ydata_result):
    plt.plot(xdata, ydata_origin, 'o')
    plt.plot(xdata, ydata_result)
    plt.show()


# read a csv file
def read(file_name, seperator, column):
    return csvmanager.CSVManager().read(file_name=file_name, seperator=seperator, column=column)


xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154,
                    161], dtype=float)
ydata_2 = np.array(normalize([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200,
                              1700, 1170, 830, 750, 770, 520, 550, 380]), dtype=float)


def fit_test(class_instance, **param ):
    res = class_instance.fit(xdata_2, ydata_2, **param)
    plot(xdata_2, ydata_2, res)


def base_model_test(class_instance, **param):
    I0 = 0.3
    time = np.arange(1, 120 + 1, 1)
    N = 5
    res = class_instance.base_model(I0, N, time, **param)
    plt.plot(res)
    plt.show()


sir = SIR()  # simple
sirwbad = SIRwbad()  # with births and deaths
sis = SIS()  # simple
siswbad = SISwbad()  # with births and deaths
sirs = SIRS()  # simple

# get base model
# ------------------------------
# base_model_test(sir, beta=0.5, gamma=0.1)
# base_model_test(sirwbad, beta=0.5, gamma=0.1, mu=0)
# ------------------------------

# find optimize parameters
# ------------------------------
# fit_test(sir)
# fit_test(sirwbad)
# fit_test(sis)
# fit_test(siswbad) # looks weird
# fit_test(sirs) # looks weird
# ------------------------------

# use manuall parameters for fitting
# ------------------------------
# fit_test(sir, beta=0.20559692 , gamma=0.11330003)
# fit_test(sirwbad, beta=0.20559692 , gamma=0.11330003, mu=0)
# fit_test(sis, beta=0.20559639, gamma=0.11329984)
# fit_test(siswbad, beta=0.20559639, gamma=0.11329984, mu=0.01)  # looks weird
# fit_test(sirs, beta=0.22931856, gamma=0.12404895, mu=0.00879889, f=0.0)
# ------------------------------

# ======================================
# DO NOT USE THIS CODE !
# SIR 
# data_set_1 = read(file_name="data1.csv", seperator=";", column=["Time", "I"])
# ydata = np.array(data_set_1["I"], dtype=float)
# xdata = np.array(data_set_1["Time"], dtype=float)
# sir = SIR(xdata, ydata)
# plot(xdata, ydata, sir.fit())
# ======================================
