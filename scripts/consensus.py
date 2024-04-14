from Bio import AlignIO
from collections import Counter

input = snakemake.input[0]
output = snakemake.output[0]


# Load the alignment
alignment = AlignIO.read(input, "fasta")

# Calculate the consensus sequence
consensus_seq = ""
for i in range(len(alignment[0])):
    column = alignment[:, i]
    counts = Counter(column)
    consensus_base = counts.most_common(1)[0][0]
    base_count = column.count(consensus_base)
    base_percentage = base_count / len(column)
    if base_percentage > 0.5 :
        if consensus_base != '-':
            consensus_seq += consensus_base
    else:
        consensus_seq += '-'

# Write the consensus sequence to a file
with open(output, "w") as output_file:
    output_file.write(">Consensus\n")
    output_file.write(consensus_seq + "\n")
