# Create initial gene expression dictionary
gene_exp = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}
print("=== 1. Gene Expression Analysis ===")
print("Initial gene expression dictionary:", gene_exp)

# Add new gene MYC to the dictionary
gene_exp['MYC'] = 11.6
print("Gene expression dictionary after adding MYC:", gene_exp)

# Create bar chart for gene expression levels
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
genes = list(gene_exp.keys())
expressions = list(gene_exp.values())
plt.bar(genes, expressions, color='skyblue')

# Add chart title and axis labels
plt.title('Gene Expression Levels', fontsize=14)
plt.xlabel('Gene Name', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.tight_layout()
plt.show()

# Query expression level of a target gene
gene_interest = 'EGFR'
if gene_interest in gene_exp:
    print(f"The expression level of gene {gene_interest} is: {gene_exp[gene_interest]}")
else:
    print(f"Error: Gene {gene_interest} is not found in the dataset!")

# Calculate and print average expression level
avg_exp = sum(expressions) / len(expressions)
print(f"Average expression level of all genes: {avg_exp:.2f}\n")


