# import necessary libraries
from Bio import SeqIO
import re

# Ask user for splice donor/acceptor combination
valid_combinations = ['GTAG', 'GCAG', 'ATAC']
while True:
    user_input = input("Enter splice donor/acceptor combination (GTAG, GCAG, or ATAC): ").upper()
    if user_input in valid_combinations:
        break
    print("Invalid input. Please enter GTAG, GCAG, or ATAC.")

# Define input and output files
input_fasta = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_fasta = f'{user_input}_spliced_genes.fa'

# Process the genes
with open(output_fasta, 'w') as out_file:
    for record in SeqIO.parse(input_fasta, "fasta"):
        gene_name = record.id.split('_')[0]  # Get just the gene name
        sequence = str(record.seq)
        
        # Find all TATA boxes (using your pattern)
        tata_matches = re.findall('(TATA[AT]A[AT])', sequence, re.IGNORECASE)
        tata_count = len(tata_matches)
        
        # Check if both splice signal is present and has TATA boxes
        if user_input in sequence and tata_count > 0:
            # Write to output file with gene name and TATA count
            out_file.write(f">{gene_name}|Number of instances of the TATA box within the sequence: {tata_count}\n")
            out_file.write(f"{sequence}\n")

print(f"Filtered genes written to {output_fasta}")