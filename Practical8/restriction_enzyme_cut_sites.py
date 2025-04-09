def restriction_enzyme_cut_sites(DNA_sequence, recognition_sequence):
    """
    Input: the DNA sequence to be cut, the sequence recognised by the restirction enzyme
    Return: positions within the DNA sequence where the restriction enzyme cuts
    """
    import re
    # Check that both sequences contain only canonical nucleotides
    if re.search(r'[^AGCT]',DNA_sequence):
        return("Error: Both sequence should contain only canonical nucleotides")
    else:
        restriction_enzyme_cut_sites = []
        i = 0
        for i in range(0,(len(DNA_sequence)+1)):
            current_seq = DNA_sequence[i:i+len(recognition_sequence)]
            if current_seq == recognition_sequence:
                restriction_enzyme_cut_sites.append(i)
            i = i+1
        return(restriction_enzyme_cut_sites)
    
# Example function call
example = restriction_enzyme_cut_sites('ATCGGAATTCGCTAGCTAGCTGGATCCTATCGATCGATAGGCCTTAGCCTAGAATTC','GAATTC')
print(example)

# This result follows python's 0-based indexing