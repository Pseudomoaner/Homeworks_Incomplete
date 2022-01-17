# -*- coding: utf-8 -*-
"""
BROWNIANMOTIONFUNCTIONS

Module containing function definitions for the Phys119 

Please fill out function definitions for:
    -moveBrownianParticle (Exercise 1)

Author: Oliver J. Meacock, 2020
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def moveBrownianParticle(x_0,y_0,T,dt):
    #Your code goes here. x_0, y_0 = initial particle position, T = temperature, dt = timestep size

#This function calculates the RMSD of the given input data. It should not need editing.
def RMSD(x,y):
    Sums = np.zeros((x.shape[0],1))
    Counts = np.zeros((x.shape[0],1))
    for i in range(0,x.shape[1]): #For each track
        for j in range(0,x.shape[0]): #Treat each sub-track as a separate track
            currXs = x[j:,i]
            currYs = y[j:,i]
            currTimes = range(0,x.shape[0] - j)
            
            currXDisps = currXs - currXs[0]
            currYDisps = currYs - currYs[0]
            
            np.put(Sums,currTimes,np.take(Sums,currTimes) + np.power(currXDisps,2) + np.power(currYDisps,2))
            np.put(Counts,currTimes,np.take(Counts,currTimes) + np.ones(len(currXDisps)))
            
    return np.sqrt(np.true_divide(Sums,Counts))

#This function will plot a given set of tracks. It should not need editing.
def plotTracks(xs,ys):
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    
    for s in range(0,xs.shape[1]):
        axes.plot(xs[:,s], ys[:,s])
    
    axes.set_aspect('equal')
    
#This function will plot the output of the RMSD function on log-log axes. It should not need editing.
def plotRMSD(r,ts):
    logRs = np.log(r[1:])
    logTs = np.log(ts[1:])

    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axes.plot(logTs,logRs)
    axes.plot(np.arange(-2,3.1,1),np.arange(-1.5,1.1,0.5),color='black')
    axes.set_xlabel(r'$\log(t)$')
    axes.set_ylabel(r'$\log(r(t))$');