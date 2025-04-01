# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Basic variables of the model & arrays to record the changes of the variables over time
Population = 10000
Susceptible = 9999
Infected = 1 
Recovered = 0

beta = 0.3 # infection probability upon contact
gamma = 0.05 # recovery probability

array_for_susceptible = np.array([])
array_for_infected = np.array([])
array_for_recovered = np.array([])

plt.figure(figsize=(10,6))

# The time course
time_points = range(1001)
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
    Recovered = Recovered + newly_recovered
    Infected = Infected - newly_recovered + newly_infected
    Susceptible = Susceptible - newly_infected 
    
    # Record the updates via the arrays
    array_for_susceptible = np.append(array_for_susceptible, [Susceptible])
    array_for_infected = np.append(array_for_infected, [Infected])
    array_for_recovered = np.append(array_for_recovered, [Recovered])

# Plot the results 
plt.plot(time_points, np.array(array_for_susceptible), "r-", label="Susceptible")
plt.plot(time_points, np.array(array_for_infected), "b-", label="Infected")
plt.plot(time_points, np.array(array_for_recovered), "g", label="Recovered")
plt.xticks(np.arange(0,1001,200))
plt.yticks(np.arange(0,10001,2000))
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("A simple SIR model")
plt.legend()
plt.show()