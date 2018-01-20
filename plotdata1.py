import numpy as np
import matplotlib.pyplot as pl

data1 = np.loadtxt("testdata.csv",delimiter=",",skiprows=1)
#pl.figure(1)
pl.subplot(3,1,1)
pl.plot([data1 [0][:,0]],data1[:,1],"r--*")
pl.xlabel("time")
pl.ylabel("${}^0C$")
#plotsubplot(3,1,2)
xx = np.arange(0,100,0.5)
yy = np.sin(xx/100*np.pi)*20+10
pl.plot(xx,yy,"g-")
pl.legend(["temp","sinwave"])
pl.xlim(xmax=150,xmin=0)
pl.ylim(ymax=50,ymin=0)
pl.title("Graphs of Thangs")
#pl.figure(2)
pl.subplot(3,1,2)
pl.plot(data1[:,0],data1[:,3],"y.-")
#xx.np.arange(0,np.pi,0.1)*100
#yy=np.sin(xx/10)*
#pl.plot()
pl.show()













range(0,len(daysdata))
E=0

dataE = np.loadtxt("*days.csv",delimiter=",",skiprows=1)

pl.subplot(3,1,1)
pl.plotE([data [E][2,0]],data[E][2,0],"r--*")




