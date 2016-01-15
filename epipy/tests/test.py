# -*- coding: utf-8 -*-

# from epipy.utils import csvmanager
from epipy.model import SIR, SIRwbad, SIS, SISwbad, SIRS, SIRSwbad
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec


# normalize a vector
def normalize(vector):
    return [v * 1.0 / sum(vector) for v in vector]

# read a csv file
def read(file_name, seperator, column):
    return csvmanager.CSVManager().read(file_name=file_name, seperator=seperator, column=column)


xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154,
                    161], dtype=float)
ydata_2 = np.array(normalize([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200,
                              1700, 1170, 830, 750, 770, 520, 550, 380]), dtype=float)


def fit_test(class_instance, **param):
    return class_instance.fit(xdata_2, ydata_2, **param)


def plot(title, x, y1, y2, y3, l1, l2, l3):
    fig = plt.figure()
    fig.suptitle(title) # figure title
    gs = gridspec.GridSpec(3, 3)
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(x, y1, label=l1)
    ax1.legend(loc='best')
    ax2 = fig.add_subplot(gs[1, :])
    ax2.plot(x, y2, label=l2)
    ax2.legend(loc='best')
    ax3 = fig.add_subplot(gs[2, :])
    ax3.plot(x, y3, label=l3)
    ax3.legend(loc='best')


sir = SIR()  # simple
sirwbad = SIRwbad()  # with births and deaths
sis = SIS()  # simple
siswbad = SISwbad()  # with births and deaths
sirs = SIRS()  # simple
sirswbad = SIRSwbad() # with births and deaths

# ======================================================================================================================
# get base model
# ======================================================================================================================
# I0 = 0.3
# time = np.arange(1, 120 + 1, 1)
# N = 5
# beta = 0.5
# gamma = 0.1
# mu = 0.001
# f = 0.001
# x = time
#
# y1 = sir.base_model(I0, N, time, beta=beta, gamma=gamma)
# y2 = sis.base_model(I0, N, time, beta=beta, gamma=gamma)
# y3 = sirs.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu)
# plot("Basemodel: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s" % (I0, N, beta, gamma, mu),
#      x, y1, y2, y3, 'SIR(beta,gamma)', 'SIS(beta,gamma)', 'SIRS(beta,gamma,mu)')
#
# y1 = sirwbad.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu)
# y2 = siswbad.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu)
# y3 = sirswbad.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu, f=f)
# plot("Basemodel: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s, f=%s" % (I0, N, beta, gamma, mu, f),
#      x, y1, y2, y3, 'SIRwbad(beta,gamma,mu)', 'SISwbad(beta,gamma,mu)', 'SIRSwbad(beta,gamma,mu,f)')
#
# plt.show()
# ======================================================================================================================
# find optimize parameters
# ======================================================================================================================
# fig = plt.figure()
# fig.suptitle("With optimize(): no parameters")
# gs = gridspec.GridSpec(3, 3)
#
# ax1 = fig.add_subplot(gs[0, :])
# ax1.plot(xdata_2, ydata_2, 'o-', label='Data')
# ax1.plot(xdata_2, fit_test(sir), label='SIR')
# ax1.legend(loc='best')
#
# ax2 = fig.add_subplot(gs[1, :])
# ax2.plot(xdata_2, ydata_2, 'o-', label='Data')
# ax2.plot(xdata_2, fit_test(sis), label='SIS')
# ax2.legend(loc='best')
#
# ax3 = fig.add_subplot(gs[2, :])
# ax3.plot(xdata_2, ydata_2, 'o-', label='Data')
# ax3.plot(xdata_2, fit_test(sirs), label='SIRS')
# ax3.legend(loc='best')
#
# fig = plt.figure()
# fig.suptitle("With optimize(): no parameters")
# gs = gridspec.GridSpec(3, 3)
#
# ax4 = fig.add_subplot(gs[0, :])
# ax4.plot(xdata_2, ydata_2, 'o-', label='Data')
# ax4.plot(xdata_2, fit_test(sirwbad), label='SIRwbad')
# ax4.legend(loc='best')
#
# ax5 = fig.add_subplot(gs[1, :])
# ax5.plot(xdata_2, ydata_2, 'o-', label='Data')
# ax5.plot(xdata_2, fit_test(siswbad), label='SISwbad')
# ax5.legend(loc='best')
#
# ax6 = fig.add_subplot(gs[2, :])
# ax6.plot(xdata_2, ydata_2, 'o-', label='Data')
# ax6.plot(xdata_2, fit_test(sirswbad), label='SIRSwbad')
# ax6.legend(loc='best')
#
# plt.show()
# ======================================================================================================================
# use manual parameters for fitting
# ======================================================================================================================
# beta = 0.20559692
# gamma = 0.11330003
# mu = 0
# f = 0.01
# x = xdata_2
#
# y1 = sir.fit(xdata_2, ydata_2, beta=beta, gamma=gamma)
# y2 = sis.fit(xdata_2, ydata_2, beta=beta, gamma=gamma)
# y3 = sirs.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu)
# plot("Manual parameters: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s" % (I0, N, beta, gamma, mu),
#      x, y1, y2, y3, 'SIR(beta,gamma)', 'SIS(beta,gamma)', 'SIRS(beta,gamma,mu)')
#
# y1 = sirwbad.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu)
# y2 = siswbad.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu)
# y3 = sirswbad.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu, f=f)
# plot("Manual parameters: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s, f=%s" % (I0, N, beta, gamma, mu, f),
#      x, y1, y2, y3, 'SIRwbad(beta,gamma, mu)', 'SISwbad(beta,gamma, mu)', 'SIRSwbad(beta,gamma, mu, f)')
#
# plt.show()

# ======================================
# DO NOT USE THIS CODE !
# SIR
# data_set_1 = read(file_name="data1.csv", seperator=";", column=["Time", "I"])
# ydata = np.array(data_set_1["I"], dtype=float)
# xdata = np.array(data_set_1["Time"], dtype=float)
# sir = SIR(xdata, ydata)
# plot(xdata, ydata, sir.fit())
# ======================================
