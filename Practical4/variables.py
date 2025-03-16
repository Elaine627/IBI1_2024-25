# Commute to office
# Walk to the bus stop and take the bus directly to their office
a = 15 # Walk to the bus stop
b = 75 # Bus
c = a + b # Total time for the bus-based commute

# Drive to a nearby car park and then walk the final stage
d = 90 # Drive
e = 5 # Walk
f = d + e # Total time for car-based commute

if c > f:
    print("c is longer. Car-based commute is quicker.")
else:
    print("f is longer. Bus-based commute is quicker.")

# Booleans
print("Here is the truth table for W:")
X = True
Y = False
W = X and Y # 'both X and Y"
print (f"When X = {X}, Y = {Y}, W = {W}")
X = True
Y = True
W = X and Y
print (f"When X = {X}, Y = {Y}, W = {W}")
X = False
Y = True
W = X and Y
print (f"When X = {X}, Y = {Y}, W = {W}")
X = False
Y = False
W = X and Y
print (f"When X = {X}, Y = {Y}, W = {W}")
