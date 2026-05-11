# =============================================================================
# Practical 7 Task 2: Identify Genes with In‑Frame Stop Codons
#
# Code Logic:
# 1. Read the yeast cDNA FASTA file line by line.
# 2. Parse each gene: header + full sequence.
# 3. For each sequence, search for ATG start and in‑frame stop codons.
# 4. Keep only genes with at least one valid ORF containing stop codons.
# 5. Write filtered genes to a new FASTA with simplified headers.
# =============================================================================

# Define DNA stop codons
stop_codons = {'TAA', 'TAG', 'TGA'}
output_list = []

# Open and read input FASTA file
with open("IBI1_2025-26/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    lines = f.readlines()

# Variables to store current gene header and sequence
current_header = ""
current_seq = ""

# Process each line
for line in lines:
    line = line.strip()
    # Skip empty lines
    if not line:
        continue
    # Check if line is a FASTA header
    if line.startswith(">"):
        # Process the previous gene if exists
        if current_header and current_seq:
            detected_stops = set()
            is_valid = False
            # Search for ATG and in‑frame stop codons
            for i in range(len(current_seq) - 2):
                if current_seq[i:i+3] == "ATG":
                    # Scan codons in frame
                    for j in range(i, len(current_seq) - 2, 3):
                        codon = current_seq[j:j+3]
                        if codon in stop_codons:
                            detected_stops.add(codon)
                            is_valid = True
                    if is_valid:
                        break
            # If valid, prepare output record
            if is_valid:
                # Extract gene name
                gene_name = current_header.split()[0][1:]
                stop_str = ",".join(sorted(detected_stops))
                new_header = f">{gene_name} {stop_str}"
                output_list.append(new_header)
                output_list.append(current_seq)
        # Reset for next gene
        current_header = line
        current_seq = ""
    else:
        # Append sequence lines
        current_seq += line

# Write output FASTA file
with open("stop_genes.fa", "w") as out_file:
    out_file.write("\n".join(output_list) + "\n")

print("Successfully generated stop_genes.fa")