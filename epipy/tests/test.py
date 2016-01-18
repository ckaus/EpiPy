# -*- coding: utf-8 -*-

import numpy as np

import testutils
from epipy.model import sir, sirs, seir
from epipy.utils import csvmanager

sir_simple = sir.Simple()
sir_vaccine = sir.Vaccine()
sir_wbad = sir.WithBirthsAndDeaths()
sirs_simple = sirs.Simple()
sirs_wbad = sirs.WithBirthsAndDeaths()
seir_simple = seir.Simple()
# ======================================================================================================================
# Data
# ======================================================================================================================
data_set_1 = csvmanager.read(file_name="data1.csv", seperator=";", column=["Time", "I"])
ydata = np.array(data_set_1["I"], dtype=float)
xdata = np.array(data_set_1["Time"], dtype=float)

xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154,
                    161], dtype=float)

ydata_2 = np.array([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300,
                    1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380], dtype=float)
# ======================================================================================================================
# get base model
# ======================================================================================================================
# Compare Simple, Vaccine
# http://www.public.asu.edu/~hnesse/classes/sir.html?Alpha=0.3&Beta=0.1&initialS=100&initialI=1&initialR=0&iters=100

# I0 = [0.3]
# beta = 0.5
# gamma = 0.1
# N = 5
# mu = 0
# nu = 0
# f = 0
# time = np.arange(1, 120 + 1, 1)
#
# res1 = sir_simple.fit(time, I0, N=N, beta=beta, gamma=gamma)
# res2 = sir_vaccine.fit(time, I0, N=N, beta=beta, gamma=gamma, nu=nu)
# res3 = sir_wbad.fit(time, I0, N=N, beta=beta, gamma=gamma, mu=mu)
#
# testutils.plot('SIR Base Model', xdata=time, ydata=[res1, res2, res3],
#                labels=['Simple', 'Vaccine', 'With Births And Deaths'])
# res4 = sirs_simple.fit(time, I0, N=N, beta=beta, gamma=gamma, mu=mu)
# res5 = sirs_wbad.fit(time, I0, N=N, beta=beta, gamma=gamma, mu=mu, f=f)
#
# testutils.plot('SIRS Base Model', xdata=time, ydata=[res4, res5],
#                labels=['Simple', 'With Births And Deaths'])

# -----------------------------------
# Compare: http://www.public.asu.edu/~hnesse/classes/seir.html?
# E0 = [1]
# beta = 0.9
# gamma = 0.1
# sigma = 0.1
# mu = 0
# nu = 0
# time = np.arange(1, 120 + 1, 1)
# N = 101
# res6 = seir_simple.fit(time, E0, N=101, beta=beta, gamma=gamma, sigma=sigma, mu=mu)
# testutils.plot('SEIR Base Model', xdata=time, ydata=[res6], labels=['Simple'])

# ======================================================================================================================
# find optimize parameters
# ======================================================================================================================
res1 = sir_simple.fit(xdata, ydata, N=1)
res2 = sir_vaccine.fit(xdata, ydata, N=1)
res3 = sir_wbad.fit(xdata, ydata, N=1)
testutils.plot_with_data('With Optimize()', xdata=xdata, ydata=ydata, results=[res1, res2, res3],
                         labels=['Simple', 'Vaccine', 'With Births And Deaths'])
#
# res4 = sirs_simple.fit(xdata, ydata, N=1)
# res5 = sirs_wbad.fit(xdata, ydata, N=1)
# testutils.plot_with_data('With Optimize() - SIRS', xdata=xdata, ydata=ydata, results=[res4, res5],
#                          labels=['Simple', 'With Births And Deaths'])
#
# res6 = seir_simple.fit(xdata_2, ydata_2, N=10000)
# testutils.plot_with_data('With Optimize() - SEIR', xdata=xdata_2, ydata=ydata_2, results=[res6],
#                          labels=['Simple'])

# ======================================================================================================================
# use manual parameters for fitting
# ======================================================================================================================
# N = 1
# beta = 0.50117819
# gamma = 0.10005569
# mu = 0.0007
# f = 0
# nu = 0
# res1 = sir_simple.fit(xdata, ydata, N=N, beta=beta, gamma=gamma)
# res2 = sir_vaccine.fit(xdata, ydata, N=N, beta=beta, gamma=gamma, nu=nu)
# res3 = sir_wbad.fit(xdata, ydata, N=N, beta=beta, gamma=gamma, mu=mu)
# res4 = sirs_simple.fit(xdata, ydata, N=N, beta=beta, gamma=gamma, mu=mu)
# res5 = sirs_wbad.fit(xdata, ydata, N=N, beta=beta, gamma=gamma, mu=mu, f=f)
#
# testutils.plot_with_data('N=%s, beta=%s, gamma=%s, mu=%s, nu=%s, f=%s' % (N, beta, gamma, mu, nu, f), xdata, ydata,
#                          results=[res1, res2, res3, res4, res5],
#                          labels=['SIR Simple(b,g)', 'SIR Vac(b,g,n)', 'SIR Wbad(b,g,m)',
#                                  'SIRS Simple(b,g,m)', 'SIRS Wbad(b,g,m,f)'])
#
# N = 10000
# beta = 0.9
# gamma = 0.1
# mu = 0.0
# sigma = 0.1
# res6 = seir_simple.fit(xdata_2, ydata_2, N=N, beta=beta, gamma=gamma, sigma=sigma, mu=mu)
# testutils.plot_with_data('SEIRS Simple', xdata_2, ydata_2, results=[res6], labels=['Simple'])
