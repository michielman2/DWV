from ete3 import Tree

input = snakemake.input[0]
output = snakemake.output[1]

# Load the tree from the Newick format file
tree = Tree(input)

# Visualize the tree
tree.render(output)