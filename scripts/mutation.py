from Bio import AlignIO
import matplotlib.pyplot as plt

input = snakemake.input[0]
output = snakemake.output[0]

# Laden van de multiple sequence alignment
alignment = AlignIO.read(input, "fasta")

# Tellen van matches en mismatches per positie
num_sequences = len(alignment)
matches = [sum(1 for seq in alignment[:, i] if seq == alignment[0, i]) for i in range(alignment.get_alignment_length())]
mismatches = [num_sequences - m for m in matches]

# Plotting van de mutatie-hotspots
plt.figure(figsize=(10, 5))
plt.plot(range(1, alignment.get_alignment_length() + 1), mismatches, color='red', label='Mismatches')
plt.plot(range(1, alignment.get_alignment_length() + 1), matches, color='blue', label='Matches')
plt.xlabel('Position in Alignment')
plt.ylabel('Number of Matches/Mismatches')
plt.title('Mutation Hotspots')
plt.legend()
plt.savefig(output)
