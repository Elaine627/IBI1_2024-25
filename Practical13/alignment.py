# Length and subcellular localisation of the human SOD2 protein
# Length: 222 amino acids
# Subcellular localisation: mitochondrion matrix
# Range of percentage identities in the reported online BLAST results: 58.1-100%

# Import necessary libraries
from Bio import SeqIO
import blosum as bl

matrix = bl.BLOSUM(62)

# Read fasta files
human_fasta = 'P04179.fasta'
mouse_fasta = 'P09671.fasta'
random_fasta = 'random.fasta'
for record in SeqIO.parse(human_fasta, "fasta"):
    human_seq = str(record.seq) # Extract sequence as string
for record in SeqIO.parse(mouse_fasta, "fasta"):
    mouse_seq = str(record.seq) 
for record in SeqIO.parse(random_fasta, "fasta"):
    random_seq = str(record.seq)

# Run all three pairwise combinations of sequences
#human-mouse
i = 0
hmscore = 0
for i in range(222):
    score = matrix[human_seq[i]][mouse_seq[i]]
    hmscore += score
    i += 1
# human-random
j = 0
hrscore = 0
for j in range(222):
    score = matrix[human_seq[j]][random_seq[j]]
    hrscore += score
    j += 1
# mouse-random
k = 0
mrscore = 0
for k in range(222):
    score = matrix[mouse_seq[k]][random_seq[k]]
    mrscore += score
    k += 1

# Calculate Hamming/edit distance
# human-mouse
hm_distance = 0
for i in range(222):
    if human_seq[i] != mouse_seq[i]:
        hm_distance += 1
hm_idpercentage = (222 - hm_distance) / 222 * 100
# human-random
hr_distance = 0
for j in range(222):
    if human_seq[j] != random_seq[j]:
        hr_distance += 1
hr_idpercentage = (222 - hr_distance) / 222 * 100
# mouse-random
mr_distance = 0
for k in range(222):
    if mouse_seq[k] != random_seq[k]:
        mr_distance += 1
mr_idpercentage = (222 - mr_distance) / 222 * 100

# Show results
print(f"human-mouse:")
print(f"alignment score = {hmscore}")
print(f"percentage of identical amino acids = {hm_idpercentage:.2f}%\n")
print(f"human-random:")
print(f"alignment score = {hrscore}")
print(f"percentage of identical amino acids = {hr_idpercentage:.2f}%\n")
print(f"mouse-random:")
print(f"alignment score = {mrscore}")
print(f"percentage of identical amino acids = {mr_idpercentage:.2f}%\n")

print("Human sequence and mouse sequence are most closely related")

# Expected output:
# human-mouse:
# alignment score = 1097.0
# percentage of identical amino acids = 90.09%
# human-random:
# alignment score = -265.0
# percentage of identical amino acids = 4.50%
# mouse-random:
# alignment score = -268.0
# percentage of identical amino acids = 4.05%

# Human sequence and mouse sequence are most closely related