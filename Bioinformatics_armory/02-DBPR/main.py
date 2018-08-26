#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: main.py
    Location: Bioinformatics armory
    Project: Rosalind.info
    Author: Alexander Popp
    Date created: 08/26/2018
    Date last modified: 8/26/2018
    Python version: 3.6.5
    Description:
        DBPR: Given the uniprot ID of a protein, return a list of biological
        processes in which the protein is involved (biological processes are
        found in a subsection of the protein's 'Gene Ontology' (GO) section).
"""


from Bio import ExPASy
from Bio import SwissProt


# Read input file
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readline()


# Write output file
def write_file(file_name, data):
    with open(file_name, 'w') as f:
        for item in data:
            f.write(str(item) + "\n")


# Returns list of biological processes
def get_processes(prot_id):
    handle = ExPASy.get_sprot_raw(prot_id)
    record = SwissProt.read(handle)
    repos = record.cross_references
    result = []

    for i in range(len(repos)):
        if 'GO' in repos[i]:
            if 'P:' in repos[i][2]:
                result.append(repos[i][2][2::])
    result = map(str, result)
    return list(result)


def main():
    result = get_processes(read_file('rosalind_dbpr.txt'))
    write_file('output_dbpr.txt', result)


if __name__ == "__main__":
    main()
    
