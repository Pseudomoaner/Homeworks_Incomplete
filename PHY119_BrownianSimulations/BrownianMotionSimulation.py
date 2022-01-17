# -*- coding: utf-8 -*-
"""
BROWNIANMOTIONSIMULATION1

Use this script to check your implementation of the moveBrownianParticle
function in BrownianMotionFunctions. It should produce a plot in the console of
the motion of a single particle undergoing Brownian motion.

Author: Oliver J. Meacock, 2020
"""

import numpy as np
import BrownianMotionFunctions as BMF

#Settings of simulation
tMax = 100                #The maximum time in the simulation
dt = 0.1                  #The timestep size
tSteps = round(tMax/dt)   #The number of timesteps taken to reach tMax
T = 1                     #The temperature of the particle
x0 = 0                    #The starting coordinates of the particle
y0 = 0

#Running the simulation itself
x = x0
y = y0
ts = np.multiply(np.arange(0,tSteps),dt)        #Create a sequence of numbers indicating the times at which you are sampling the system
xs = np.zeros((tSteps,1))                       #Initialise data storage: xs (an array that will contain the x-coordinates of our particle at each timepoint)
ys = np.zeros((tSteps,1))                       #And ys (an array that will contain the y-coordinates of our particle at each timepoint)

for t in range(1,tSteps):                       #For each timepoint in the simulation...
    (x,y) = BMF.moveBrownianParticle(x,y,T,dt)  #Move the particle
    xs[t] = x                                   #And store its new position
    ys[t] = y
    
BMF.plotTracks(xs,ys)