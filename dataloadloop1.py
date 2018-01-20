import numpy as np
import matplotlib.pyplot as pl
import glob

daysdata = []
days =['tuesday.csv', 'monday.csv', 'thursday.csv', 'sunday.csv', 'wednesday.csv', 'friday.csv', 'saturday.csv']
 #glob.glob("*day.csv")

for day in days:
	daysdata.append(np.loadtxt(day,delimiter=",",skiprows=1,usecols=(1,2)))
	#print(days)
#d=0
#for d in range(0,len(daysdata)):
#pl.plot(daysdata[0][1,2],daysdata[0][1,2],"r--*")


pl.plot(daysdata[0][:,1]),daysdata[0][:,1])
