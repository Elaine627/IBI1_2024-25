# Create and print a dictionary
programming_language_popularity = {'javascript': 62.3, 'html': 52.9, 'python': 51, 'sql': 51, 'typescript': 38.5}
print(programming_language_popularity)

# Construct a bar plot
# This part is adapted from lecture 5.1 slides by Professor Chi Ying.
import numpy as np
import matplotlib.pyplot as plt

# Get data from dictionary instead of hard-coded values
languages = list(programming_language_popularity.keys())
popularity = list(programming_language_popularity.values())

N = len(languages)
ind = np.arange(N)
width = 0.4
p1 = plt.bar(ind, popularity, width)
plt.xlabel("Programming Languages")
plt.ylabel("Users (percentage)")
plt.title("Percentage of developers who use the top 5 programming languages globally as of February 2024")
plt.xticks(ind, languages)  # Capitalize language names
plt.yticks(np.arange(0, 101, 10))
plt.show()

# Return the percentage of developers who use one language taken from the input list
input_language = input("Language:").lower() # This prevents errors when the input has unexpected uppercase letters, for example "PYthOn"
print(f"The percentage of developers who use {input_language} is {programming_language_popularity[input_language]}.")