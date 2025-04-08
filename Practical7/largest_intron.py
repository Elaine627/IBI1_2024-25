import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'(GT.+AG)',seq)[0] # find the largest possible introns using greedy matching
print(largest_intron)
# Output the largest possible intron and its length
print(f"The largest intron that can be possibly generated from this sequence is '{largest_intron}'.")
print(f"The length of this intron is {len(largest_intron)}.")