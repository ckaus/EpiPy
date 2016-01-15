# -*- coding: utf-8 -*-

import testutils
from epipy.model import SIR, SIRwbad, SIS, SISwbad, SIRS, SIRSwbad
import numpy as np

sir = SIR()  # simple
sirwbad = SIRwbad()  # with births and deaths
sis = SIS()  # simple
siswbad = SISwbad()  # with births and deaths
sirs = SIRS()  # simple
sirswbad = SIRSwbad()  # with births and deaths

xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154,
                    161], dtype=float)

ydata_2 = np.array(testutils.normalize([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300,
                                        1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380]), dtype=float)

# ======================================================================================================================
# get base model
# ======================================================================================================================
I0 = 0.3
time = np.arange(1, 120 + 1, 1)
N = 5
beta = 0.5
gamma = 0.1
mu = 0.001
f = 0.001
x0 = time

y0 = sir.base_model(I0, N, time, beta=beta, gamma=gamma)
y1 = sis.base_model(I0, N, time, beta=beta, gamma=gamma)
y2 = sirs.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu)
testutils.plot("Basemodel: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s" % (I0, N, beta, gamma, mu), x0, y0, y1, y2,
               'SIR(beta,gamma)', 'SIS(beta,gamma)', 'SIRS(beta,gamma,mu)')

y0 = sirwbad.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu)
y1 = siswbad.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu)
y2 = sirswbad.base_model(I0, N, time, beta=beta, gamma=gamma, mu=mu, f=f)
testutils.plot("Basemodel: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s, f=%s" % (I0, N, beta, gamma, mu, f), x0, y0, y1, y2,
               'SIRwbad(beta,gamma,mu)', 'SISwbad(beta,gamma,mu)', 'SIRSwbad(beta,gamma,mu,f)')
# ======================================================================================================================
# find optimize parameters
# ======================================================================================================================
y0 = sir.fit(xdata_2, ydata_2)
y1 = sis.fit(xdata_2, ydata_2)
y2 = sirs.fit(xdata_2, ydata_2)
testutils.plot_with_data("With optimize(): no parameters", xdata_2, ydata_2, y0, y1, y2,'SIR','SIS','SIRS')

y0 = sirwbad.fit(xdata_2, ydata_2)
y1 = siswbad.fit(xdata_2, ydata_2)
y2 = sirswbad.fit(xdata_2, ydata_2)
testutils.plot_with_data("With optimize(): no parameters", xdata_2, ydata_2, y0, y1, y2,'SIR','SIS','SIRS')
# ======================================================================================================================
# use manual parameters for fitting
# ======================================================================================================================
beta = 0.20559692
gamma = 0.11330003
mu = 0.001
f = 0.001

y0 = sir.fit(xdata_2, ydata_2, beta=beta, gamma=gamma)
y1 = sis.fit(xdata_2, ydata_2, beta=beta, gamma=gamma)
y2 = sirs.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu)
testutils.plot_with_data("Manual parameters: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s" % (I0, N, beta, gamma, mu),
                         xdata_2, ydata_2, y0, y1, y2, 'SIR(beta,gamma)', 'SIS(beta,gamma)', 'SIRS(beta,gamma,mu)')

y0 = sirwbad.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu)
y1 = siswbad.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu)
y2 = sirswbad.fit(xdata_2, ydata_2, beta=beta, gamma=gamma, mu=mu, f=f)
testutils.plot_with_data("Manual parameters: I0=%s, N=%s, beta=%s, gamma=%s, mu=%s, f=%s" % (I0, N, beta, gamma, mu, f),
                         xdata_2, ydata_2, y0, y1, y2, 'SIRwbad(beta,gamma, mu)', 'SISwbad(beta,gamma, mu)',
                         'SIRSwbad(beta,gamma, mu, f)')
# ======================================
# DO NOT USE THIS CODE !
# SIR
# data_set_1 = read(file_name="data1.csv", seperator=";", column=["Time", "I"])
# ydata = np.array(data_set_1["I"], dtype=float)
# xdata = np.array(data_set_1["Time"], dtype=float)
# sir = SIR(xdata, ydata)
# plot(xdata, ydata, sir.fit())
# ======================================
