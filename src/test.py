# -*- coding: utf-8 -*-

from utils import csvmanager
from model import SIR
import numpy as np
import matplotlib.pyplot as plt

# read data
content = csvmanager.CSV_Manager().read(
	file_name="data1.csv",
	seperator=";", column=["Time", "I"])

ydata = np.array(content['I'], dtype=float)
xdata = np.array(content['Time'], dtype=float)

# fit sir model
sir = SIR(xdata, ydata)
fitted = sir.fit()

# plot fitted sir model
plt.plot(xdata, ydata, 'o')
plt.plot(xdata, fitted)
plt.show()