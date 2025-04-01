import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
introns = re.findall(r'(?=(GT.+?AG))',seq)
largest_length = 0
for intron in introns:
    length = len(intron)
    if length > largest_length:
        largest_length = length
        largest_intron = intron
    else:
        continue
print(f"The largest intron that can be possibly generated from this sequence is '{largest_intron}'.")
print(f"The length of this intron is {largest_length}.")