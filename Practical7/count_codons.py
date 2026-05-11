# =============================================================================
# Practical 7 Task 3: Codon Frequency Analysis and Pie Chart
#
# Code Logic:
# 1. Accept user input of one stop codon (TAA/TAG/TGA).
# 2. Read FASTA and extract full gene sequences.
# 3. For each gene, find the longest ORF ending with the given stop codon.
# 4. Count all in‑frame codons upstream of that stop codon.
# 5. Generate a labeled pie chart and save it as an image file.
# =============================================================================

import matplotlib.pyplot as plt
from collections import defaultdict

# Get and validate user input
target_stop = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()
if target_stop not in {"TAA", "TAG", "TGA"}:
    print("Error: Only TAA / TAG / TGA are valid.")
    exit()

# Dictionary to accumulate codon counts
codon_counter = defaultdict(int)

# Read FASTA file
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    lines = f.readlines()

current_seq = ""

# Process each gene
for line in lines:
    line = line.strip()
    if line.startswith(">"):
        # Analyze the previous sequence
        if current_seq:
            max_orf_length = 0
            best_codon_list = []
            # Find all ATG start positions
            for i in range(len(current_seq) - 2):
                if current_seq[i:i+3] == "ATG":
                    temp_codons = []
                    # Read in frame until target stop codon
                    for j in range(i, len(current_seq) - 2, 3):
                        cod = current_seq[j:j+3]
                        temp_codons.append(cod)
                        # Stop at target codon
                        if cod == target_stop:
                            # Keep the longest ORF
                            if len(temp_codons) > max_orf_length:
                                max_orf_length = len(temp_codons)
                                best_codon_list = temp_codons[:-1]
                            break
            # Count codons from the longest ORF
            for c in best_codon_list:
                codon_counter[c] += 1
        # Reset sequence for next gene
        current_seq = ""
    else:
        current_seq += line

# Print codon counts
print("\nCodon frequencies:")
for codon, count in sorted(codon_counter.items()):
    print(f"{codon}: {count}")

# Generate and save pie chart
if codon_counter:
    plt.figure(figsize=(10, 10))
    plt.pie(codon_counter.values(),
            labels=codon_counter.keys(),
            autopct='%1.1f%%',
            textprops={'fontsize': 8})
    plt.title(f"Codon Distribution Upstream of {target_stop}")
    plt.savefig(f"codon_pie_{target_stop}.png", dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nPie chart saved as codon_pie_{target_stop}.png")
else:
    print("\nNo codons available for plotting.")