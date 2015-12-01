import csv
import numpy as np
import fit_model_ls 

originaldata = np.loadtxt('../../resources/googleflugermany.csv', delimiter=',', skiprows=1)[0:50]
#print originaldata
timetotal = np.array(range(len(originaldata)))

model = "seir"
data = {"Time": timetotal,
            "I": originaldata}
    
fit_model_ls.LeastSquaresFit(model, data).run()