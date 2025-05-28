Practical 3: I received full marks for this task
Practical 4: I received full marks for this task
Practical 5: I made two mistakes in this task. 
The first one is that when plotting the bar chart I used hardcoded values instead of reading from the dictionary. This was not an efficient approach, and made my code seem less organised.
The second one is that the bar chart was missing title and axis label, so it could not be clearly understood.
I have fixed these problems in the subsequent weeks.
I changed the lines:
Users_percentage = (62.3, 52.9, 51, 51, 38.5)
plt.xticks(ind,("JavaScript","HTML","Python","SQL","TypeScript"))
and read from the dictionary using:
languages = list(programming_language_popularity.keys())
popularity = list(programming_language_popularity.values())
I have included the title, and used clearer axis labels in the revised version.