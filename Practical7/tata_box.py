# import necessary libraries
# I will be using biopython to cope with the fasta file, then re to identify TATA genes
from Bio import SeqIO
import re

# read the file
fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
# output the results in tata_genes.fa
out_file = open('tata_genes.fa','w')

# use biopython to sort out all genes and their sequences
for record in SeqIO.parse(fasta_file, "fasta"):
    gene_name = record.id
    sequence = str(record.seq)
    
# look for TATA genes    
    if re.findall('(TATA[AT]A[AT])',sequence):
        out_file.write(f">{gene_name.split('_')[0]}\n")
        out_file.write(f"{sequence}\n")
