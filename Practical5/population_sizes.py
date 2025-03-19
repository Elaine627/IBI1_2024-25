uk_countries = [57.11, 3.13, 1.91, 5.45] # list of population sizes for UK countries
zhejiang_neighbouring_provinces = [65.77, 41.88, 45.28, 61.27, 85.15] # list of population sizes for Zhejiang-neighbouring provinces

# print two lists of sorted values
print(f"This is a list of sorted values for the populations of countries in the UK:{sorted(uk_countries)}")
print(f"This is a list of sorted values for the populations of Zhejiang-neighbouring provinces in China: {sorted(zhejiang_neighbouring_provinces)}")

# construct two charts displaying the distribution of population sizes
import matplotlib.pyplot as plt
# pie chart for UK countries
labels = "England", "Wales", "Northern Ireland", "Scotland"
sizes = uk_countries
explode = (0,0,0,0)
colors = "pink", "lightblue", "orange", "lightgreen"
plt.pie(sizes,explode=explode, labels = labels, colors = colors, autopct = "%1.1f%%", shadow = False, startangle = 90)
plt.axis("equal")
plt.show()
# pie chart for Zhejiang-neighbouring provinces
labels = "Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"
sizes = zhejiang_neighbouring_provinces
explode = (0,0,0,0,0)
colors = "pink", "lightyellow", "purple", "orange", "lightgreen"
plt.pie(sizes,explode=explode, labels = labels, colors = colors, autopct = "%1.1f%%", shadow = False, startangle = 90)
plt.axis("equal")
plt.show()