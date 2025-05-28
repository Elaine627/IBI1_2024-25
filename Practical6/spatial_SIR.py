# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
population = np.zeros((100,100))

# start with one randomly infected person
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1

# set up model parameters
beta = 0.3 # infection probability upon contact
gamma = 0.05 # recovery probability

# heat map at time 0
plt.figure(figsize = (6,4), dpi = 150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title(f"Spatial SIR Model at time 0")
plt.xticks(np.arange(0, 101, 20))
plt.yticks(np.arange(0, 101, 20))
plt.show()

# loop through 100 time points
time_points = [10,50] # We care about the state of the population at these time points


for t in range(100):
    # find infected points
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])): # loop through all infected points
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
     # infect each neighbour with probability beta
        # loop through all 8 neighbours
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y): # Excluding yourself
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100: # check that all neighbour points are within bounds
                        if population[xNeighbour,yNeighbour]==0: # only infect neighbours that are not already infected
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    
    # recover
    for j in range(len(infectedIndex[0])): # loop through all infected points
        x = infectedIndex[0][j]
        y = infectedIndex[1][j]
        population[x,y] = np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
    if t in time_points:    
    # plot heat map at times 0, 10, 50, and 100
        plt.figure(figsize = (6,4), dpi = 150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Spatial SIR Model at time {t}")
        plt.xticks(np.arange(0, 101, 20))
        plt.yticks(np.arange(0, 101, 20))
        plt.show()
    elif t == 99:  
        # Plot the final state of the population at time 100
        plt.figure(figsize = (6,4), dpi = 150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Spatial SIR Model at time {t+1}")
        plt.xticks(np.arange(0, 101, 20))
        plt.yticks(np.arange(0, 101, 20))
        plt.show()