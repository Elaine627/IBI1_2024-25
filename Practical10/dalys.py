# import python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change the working directory
os.chdir("/home/elaine-huang/Desktop/yunshan/IBI1/1/IBI1_2024-25/Practical10")

# use pandas to read .csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("The third column for the first 10 rows is shown here:")
print(dalys_data.iloc[0:10,2]) 
print(f"The 10th year with DALYs data recorded in Afghanistan is {dalys_data.iloc[9,2]}.") # The 10th year with DALYs data recorded in Afghanistan is 1999.

dalys_interested = dalys_data.loc[dalys_data.Year==1990,"DALYs"] # This uses a Boolean to find every row where the year is 1990
print(f"\nDALYs reported in the year 1990 are shown below:")
print(dalys_interested)

# save data from uk and france in separate objects
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs","Year"]]
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs","Year"]]
# calculate mean DALYs
uk_mean_dalys = uk["DALYs"].mean()
france_mean_dalys = france["DALYs"].mean()
print(f"\nThe mean DALYs in the UK is {uk_mean_dalys}.")
print(f"The mean DALYs in France is {france_mean_dalys}.")
if uk_mean_dalys > france_mean_dalys:
    print(f"The mean DALYs in the UK is greater than that in France.")
if uk_mean_dalys < france_mean_dalys:
    print(f"The mean DALYs in the UK is smaller than that in the UK.")
if uk_mean_dalys == france_mean_dalys:
    print(f"The mean DALYs in the UK is the same as that in France.")

# plot the data for the UK over time
print(f"\nHere is a plot showing the DALYs over time in the UK.")
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.title("DALYs data for the UK over time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()

# Code for question.txt
china = dalys_data.loc[dalys_data.Entity == "China", ["DALYs","Year"]]
print(f"\nBelow is a plot showing how the relationship between the DALYs in China and the UK changed over time. They are becoming more similar.")
plt.plot(uk.Year, uk.DALYs, 'b+', label='UK')
plt.plot(china.Year,china.DALYs, 'r+', label='China')
plt.xticks(uk.Year,rotation=-60)
plt.title("DALYs in China and the UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.legend()
plt.show()