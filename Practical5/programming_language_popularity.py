# Create and print a dictionary
programming_language_popularity = {'javascript': 62.3, 'html': 52.9, 'python': 51, 'sql': 51, 'typescript': 38.5}
print(programming_language_popularity)

# Construct a bar plot
# This part is adapted from lecture 5.1 slides by Professor Chi Ying.
import numpy as np
import matplotlib.pyplot as plt
N = 5
Users_percentage = (62.3, 52.9, 51, 51, 38.5)
ind = np.arange(N)
width = 0.4
p1 = plt.bar(ind, Users_percentage, width)
plt.ylabel("Users(percentage)")
plt.title("Percentage of developers who use the top 5 programming languages globally as of February 2024")
plt.xticks(ind,("JavaScript","HTML","Python","SQL","TypeScript"))
plt.yticks(np.arange(0,101,10))
plt.show()

# Return the percentage of developers who use one language taken from the input list
input_language = input("Language:").lower() # This prevents errors when the input has unexpected uppercase letters, for example "PYthOn"
print(f"The percentage of developers who use {input_language} is {programming_language_popularity[input_language]}.")
