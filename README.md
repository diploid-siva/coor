# coor
This project provides a command-line tool and a Colab notebook for codon optimization. It allows users to generate a codon-optimized DNA sequence for a target protein by mimicking the codon usage of a highly expressed reference gene.
# COOR: Codon Optimization using Ordered Reshuffling

COOR (Codon Optimization using Ordered Reshuffling) is a simple and educational tool to optimize codon usage based on the codon patterns from highly translated proteins. It takes the coding DNA sequence of a well-translated protein (Protein 1), builds a codon usage database, and uses it to reconstruct an optimized DNA sequence from a new amino acid sequence (Protein 2).

### Biological Rationale

Not all coding sequences are under evolutionary pressure for high translation efficiency. In contrast, nuclear-encoded ribosomal or proteasome proteins are usually highly translated and exhibit optimized codon usage. This tool leverages that concept by using a highly expressed gene as a template for codon selection.

### Features

- Takes a coding DNA sequence (Protein 1) and builds a codon usage database by preserving the order of codons.
- Uses that database to convert a new amino acid sequence (Protein 2) into a codon-optimized DNA sequence.
- Outputs the codon database in a table format and the final optimized sequence.

### Requirements

- Python 3.8+
- Biopython
- Pandas


Install requirements via pip:

```bash
pip install biopython pandas
