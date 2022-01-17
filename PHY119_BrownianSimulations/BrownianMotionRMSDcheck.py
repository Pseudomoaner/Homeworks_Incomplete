# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:46:21 2020

@author: ph1ojm
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import BrownianMotionFunctions as BMF

#Settings of simulation
noSims = 10               #The number of simulations you wish to perform
tMax = 100                #The maximum time in the simulation
dt = 0.1                  #The timestep size
tSteps = round(tMax/dt)   #The number of timesteps taken to reach tMax
T = 1                     #The temperature of the particle
x0 = 0                    #The starting coordinates of the particle
y0 = 0

#Running the simulation itself
ts = np.multiply(np.arange(0,tSteps),dt)           #Create a sequence of numbers indicating the times at which you are sampling the system
ys = np.zeros((tSteps,noSims))                     #Storage matrices (note that these are indexed with time along the first dimension and simulation number along the second dimension)
xs = np.zeros((tSteps,noSims))

for s in range(0,noSims):
    #Your code goes here (hint: writing X[a,b] will allow you to access element (a,b) of matrix X)
    
BMF.plotTracks(xs,ys) #Optional - allows you to view all the simulations you've just performed

r = BMF.RMSD(xs,ys)
BMF.plotRMSD(r,ts)