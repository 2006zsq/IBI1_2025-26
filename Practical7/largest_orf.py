# =============================================================================
# Practical 7 Task 1: Longest Open Reading Frame (ORF)
#
# Code Logic:
# 1. Define the given mRNA sequence.
# 2. Scan every position to find the start codon AUG.
# 3. From each AUG, read codons in frame until a stop codon (UAA, UAG, UGA).
# 4. Record all valid ORF sequences and their lengths.
# 5. Select and print the longest ORF and its nucleotide length.
# =============================================================================

# Define the given mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# Initialize a list to store valid ORFs (sequence, length)
orfs = []

# Define start and stop codons
start_codon = 'AUG'
stop_codons = {'UAA', 'UAG', 'UGA'}

# Iterate over every possible starting index for a 3-nucleotide codon
for i in range(len(seq) - 2):
    # Check if current position is a start codon
    if seq[i:i+3] == start_codon:
        # Traverse in frame until stop codon
        for j in range(i, len(seq) - 2, 3):
            current_codon = seq[j:j+3]
            # Stop when encountering a stop codon
            if current_codon in stop_codons:
                # Extract the complete ORF sequence
                orf_sequence = seq[i:j+3]
                orfs.append((orf_sequence, len(orf_sequence)))
                break

# Find the longest ORF
if orfs:
    longest_orf = max(orfs, key=lambda x: x[1])
    # Output results
    print("Longest ORF sequence:", longest_orf[0])
    print("Length of longest ORF (nt):", longest_orf[1])
else:
    print("No valid ORF detected.")