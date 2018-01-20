import numpy as np
import matplotlib.pyplot as pl

data1 = np.loadtxt("~/school_2018/Python/data/testdata.csv",delimiter=",",skiprows=1)
pl.plot(data1[:,0],data1[:,1])
pl.show()
