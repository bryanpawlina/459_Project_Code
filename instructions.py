import numpy as np
import scipy

fallTime = .4
resolution = 1/50
numberOfTargets = fallTime/resolution

torqueList = #read torques from csv(?) file into size:<num_targs,2> array

for i in torqueList.shape(1):
    torqueVec1[i] = torqueList(i,1)
    torqueVec2[i] = torqueList(i,2)

x = linspace(0,fallTime,torqueList.shape(1))

func1 = scipy.interpolate.interp1d(x,torqueVec1,kind='cubic')
func2 = scipy.interpolate.interp1d(x,torqueVec2,kind='cubic')

for k in numberOfTargets:
    target1[k] = func1(k*resolution)
    target2[k] = func2(k*resolution)

