# BMI Calculator
weight = float(input("Please give us your weight(in kg):")) # Store the person's weight
height = float(input("Please give us your height(in m):")) # Store the person's height
bmi = weight/height**2 # Calculate the person's BMI
# Decide which category they can be placed into
if bmi < 18.5:
    category = "underweight"
elif bmi > 30:
    category = "obese"
else:
    category = "normal weight"

print(f"Your BMI is {bmi}, this is considered {category}") # Output the person's BMI and category

