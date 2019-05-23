from modul_mnk import *
#import matplotlib as mat
import matplotlib.pyplot as plt
import pylab
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
yy = []
xx = []

with open ("windmil.txt","r") as file:
    dane = file.readlines()
    for line in dane:
        yy.append(float(line.split()[1]))
        xx.append(float(line.split()[0]))
    dane.append(yy)
    dane.append(xx)

print(xx)
print(yy)

res = []
bsr =[]

for n in range(1,5):
    aa, bb = gen_ur_mnk(xx, yy, n)

    print(aa)
    print(bb)


    wsp = np.linalg.solve(aa, bb) # a0,a1,a2
    print('wsp:', wsp)

    def prawdziwe():
        li = []
        for i in xx:
            wielomian1(i,wsp)
            li.append(wielomian1(i,wsp))
        return li

    prawdziwe()
    r_kwadrat(yy,prawdziwe())

    res.append(r_kwadrat(yy,prawdziwe()))
    bsr.append(blad(yy,prawdziwe()))

print(res)
print(bsr)









