# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Basic variables of the model & arrays to record the changes of the variables over time
Population = 10000
percentage_vaccinated = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
beta = 0.3 # infection probability upon contact
gamma = 0.05 # recovery probability

plt.figure(figsize=(10,6))

# The time course
time_points = list(range(1001))
for percentage in percentage_vaccinated :
    Infected = 1
    Recovered = 0
    Vaccinated = int(Population * percentage)
    Susceptible = int(Population - Infected - Recovered - Vaccinated)
    array_for_infected = np.array([])
    
    for time_point in time_points: # Loop over 1000 time points
        p_contact = Infected/Population # probability of contact
        p_infected = beta * p_contact

        # Calculate the numbers of newly-recovered and newly-infected people
        newly_recovered = np.sum(np.random.choice(range(2), Infected, p=[(1-gamma), gamma])) 
        if Susceptible > 0 and p_infected > 0:
            newly_infected = np.sum(np.random.choice(range(2), Susceptible, p=[(1-p_infected), p_infected]))
        else:
            newly_infected = 0
        # Update the numbers of recovered, infected and susceptible people
        Recovered = min(Population, Recovered + newly_recovered)
        Infected = max(0, Infected - newly_recovered + newly_infected)
        Susceptible = max(0, Susceptible - newly_infected) 
    
        array_for_infected = np.append(array_for_infected, [Infected])
        
    plt.plot(time_points, array_for_infected, color=cm.viridis(30), label=percentage)

plt.xticks(np.arange(0,1001,200))
plt.yticks(np.arange(0,10001,2000))
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with differnet vaccination rates")
plt.legend()
plt.show()