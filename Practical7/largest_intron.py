import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'(GT.+AG)',seq) # find the largest possible introns using greedy matching
# Output the largest possible intron and its length
print(f"The largest intron that can be possibly generated from this sequence is '{str(largest_intron)[2:-2]}'.")
print(f"The length of this intron is {len(str(largest_intron)[2:-2])}")