import csv
import numpy as np
import fit_model_ls 

originaldata = np.loadtxt('../../resources/data1.csv', delimiter=';', skiprows=1)[:,2]
print originaldata
timetotal = np.array(range(len(originaldata)))

model = "sir"
data = {"Time": timetotal,
            "I": originaldata}

fit_model_ls.LeastSquaresFit(model, data).run()