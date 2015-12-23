# -*- coding: utf-8 -*-

from utils import csvmanager
from model import SIR
import numpy as np
import matplotlib.pyplot as plt
import os, csv
# # read data
# content = csvmanager.CSV_Manager().read(
# 	file_name="data1.csv",
# 	seperator=";", column=["Time", "I"])

# ydata = np.array(content['I'], dtype=float)
# xdata = np.array(content['Time'], dtype=float)

# # fit sir model
# sir = SIR(xdata, ydata)
# fitted = sir.fit()

# # plot fitted sir model
# plt.plot(xdata, ydata, 'o')
# plt.plot(xdata, fitted)
# plt.show()


current_dir =  os.path.abspath(os.path.dirname(__file__))
path = os.path.abspath(current_dir + "/../resources/data")+"/"+"liberia-2014.csv"

file = open(path, "rb")
reader = csv.reader(file, delimiter=",")
header = reader.next()
hlen = len(header)
for row in reader:
	print len(row)
	# if len(row) != hlen:
		# print "o_O"