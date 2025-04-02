import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
introns = re.findall(r'(?=(GT.+?AG))',seq) # find all possible introns
largest_length = 0 # initialize the variable
# Loop through the list of possible introns and find the largest intron
for intron in introns:
    length = len(intron)
    if length > largest_length:
        largest_length = length
        largest_intron = intron
    else:
        continue
# Output the largest intron and its length
print(f"The largest intron that can be possibly generated from this sequence is '{largest_intron}'.")
print(f"The length of this intron is {largest_length}.")