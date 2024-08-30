"""
flatten_hpos.py

This script reads lines from stdin and prints flattened lines to stdout.

Input lines should be comma-separated lists of HPO terms.

We want to merge sequential runs of requests from the same user for more accurate term frequencies.

This script uses the following algorithm to remove as many duplicates as possible:
1. Find runs that start with the same N terms (N=1 or 2)
2. For the lines in the run:
  a. Merge all lines into one line with the unique HPO terms used


E.g. given input:
HP:0000347,HP:0009381,HP:0000204
HP:0000347,HP:0009381,HP:0000204
HP:0000347,HP:0009381,HP:0000204
HP:0000347,HP:0009381,HP:0000204
HP:0000347,HP:0003022,HP:0009381,HP:0000204
HP:0000347,HP:0003022,HP:0009381
HP:0000347,HP:0003022
HP:0000347,HP:0003022
HP:0000347,HP:0009381,HP:0000204
HP:0000347,HP:0003022
HP:0000347,HP:0003022,HP:0009381,HP:0000204
HP:0000347,HP:0003022
HP:0000347,HP:0003022,HP:0009381,HP:0000204
HP:0000347,HP:0003022,HP:0009381,HP:0000204
HP:0000347,HP:0003022,HP:0009381,HP:0000204
HP:0000347,HP:0003022,HP:0009381,HP:0000204,HP:0000625
HP:0000347,HP:0003022,HP:0009381,HP:0000204,HP:0000625
HP:0000347,HP:0003020,HP:0009381,HP:0000204,HP:0000625
HP:0000347,HP:0003021,HP:0009381,HP:0000204,HP:0000625
HP:0000347,HP:0009381,HP:0000204,HP:0000625
HP:0000347,HP:0009381,HP:0000204,HP:0000625
HP:0000347,HP:0003022,HP:0009381,HP:0000204,HP:0000625

The following would be output:
HP:0000204,HP:0000347,HP:0000625,HP:0003020,HP:0003021,HP:0003022,HP:0009381
"""

import sys

def get_terms_from_line(line):
    line = line.strip()
    if not line:
        return []

    terms = line.strip().split(',')

    for term in terms:
        if not term.startswith('HP:'):
            print('Invalid term: {}'.format(term), file=sys.stderr)
            terms.remove(term)

    return terms


def flatten_lines(lines):
    terms = set()
    for line in lines:
        terms.update(line)

    return [sorted(terms)]


def print_lines(lines):
    for line in lines:
        print(','.join(line))

def process(ifp, n_prefix_terms=1):

    current_prefix = None
    redundant_lines = []
    n_total = 0
    n_dedup = 0

    for line in ifp:
        terms = get_terms_from_line(line)
        if not terms:
            continue

        if current_prefix != terms[:n_prefix_terms]:
            # Line is start of new set
            # Process current set
            if redundant_lines:
                reduced_lines = flatten_lines(redundant_lines)
                n_total += len(redundant_lines)
                n_dedup += len(reduced_lines)
                print_lines(reduced_lines)

            # Start new set
            current_prefix = terms[:n_prefix_terms]
            redundant_lines = [terms]
        else:
            # Line is part of current redundant set
            redundant_lines.append(terms)

    if redundant_lines:
        reduced_lines = flatten_lines(redundant_lines)
        n_total += len(redundant_lines)
        n_dedup += len(reduced_lines)
        print_lines(reduced_lines)

    print('{} lines in, {} lines out'.format(n_total, n_dedup), file=sys.stderr)


if __name__ == '__main__':
    process(sys.stdin)