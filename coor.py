#!/usr/bin/env python3

"""
COOR - Codon Optimization using Ordered Reshuffling
Author: Prakash Sivakumar
"""

import argparse
from collections import defaultdict
from Bio.Seq import Seq
from Bio.Data import CodonTable


def is_valid_dna(seq):
    return all(base in 'ATGC' for base in seq.upper()) and len(seq) % 3 == 0


def build_codon_database(dna_seq):
    standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
    protein_seq = str(Seq(dna_seq).translate(to_stop=False))
    codon_db = defaultdict(list)

    for i in range(0, len(dna_seq), 3):
        codon = dna_seq[i:i+3]
        aa = protein_seq[i // 3]
        codon_db[aa].append(codon)

    return codon_db


def format_codon_table(codon_db):
    amino_acids = sorted(codon_db.keys())
    max_len = max(len(codon_db[aa]) for aa in amino_acids)
    lines = []

    header = "AA  | " + " | ".join(f"{aa}" for aa in amino_acids)
    lines.append(header)
    lines.append("-" * len(header))

    for i in range(max_len):
        row = [f"{i+1:2} |"]
        for aa in amino_acids:
            codons = codon_db[aa]
            row.append(codons[i] if i < len(codons) else "   ")
        lines.append("   ".join(row))

    return "\n".join(lines)


def optimize_dna(protein2, codon_db):
    reconstructed_dna = []
    usage_tracker = defaultdict(int)

    for aa in protein2:
        if aa not in codon_db:
            raise ValueError(f"Amino acid '{aa}' not found in codon database.")
        codons = codon_db[aa]
        index = usage_tracker[aa] % len(codons)
        reconstructed_dna.append(codons[index])
        usage_tracker[aa] += 1

    return "".join(reconstructed_dna)


def main():
    parser = argparse.ArgumentParser(
        prog="coor",
        description="""
COOR (Codon Optimization using Ordered Reshuffling) is a tool to optimize codon usage
of a target protein (Protein 2) based on codon usage from a well-expressed reference gene (Protein 1).

It reads:
- A DNA sequence for Protein 1 (coding strand, reference).
- An amino acid sequence for Protein 2 (1-letter codes).

It outputs:
- A codon-optimized DNA sequence for Protein 2 using the codon usage pattern from Protein 1.
- A printed codon usage table mapping amino acids to codons.
- Optionally saves the optimized DNA to a file if --output is specified.
""",
        epilog="""
Example:
    python3 coor.py -r ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG -t MAIVMGR

Save output to file:
    python3 coor.py -r <reference_dna> -t <target_aa> -o optimized_output.txt
"""
    )

    parser.add_argument(
        "-r", "--reference",
        type=str,
        required=True,
        help="DNA sequence for Protein 1 (reference gene, must be A/T/G/C and length multiple of 3)."
    )
    parser.add_argument(
        "-t", "--target",
        type=str,
        required=True,
        help="Amino acid sequence (1-letter code) of Protein 2 to optimize."
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Optional file path to save the optimized DNA sequence."
    )

    args = parser.parse_args()
    ref_dna = args.reference.upper().replace(" ", "").replace("\n", "")
    target_aa = args.target.upper().replace(" ", "").replace("\n", "")

    if not is_valid_dna(ref_dna):
        print("Invalid DNA sequence: must contain only A/T/G/C and be a multiple of 3.")
        return

    try:
        codon_db = build_codon_database(ref_dna)
        codon_table_str = format_codon_table(codon_db)
        optimized_dna = optimize_dna(target_aa, codon_db)

        print("\nCodon Database (Amino Acids vs Codons):")
        print(codon_table_str)
        print("\nOptimized DNA Sequence:")
        print(optimized_dna)

        if args.output:
            with open(args.output, "w") as f:
                f.write(optimized_dna + "\n")
            print(f"\nOutput saved to: {args.output}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
