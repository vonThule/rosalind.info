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
        FRMT: Given a collection of n (n <= 10) GenBank entry IDs, return
        the shortest of the strings associated with the IDs in FASTA format.
"""


from Bio import Entrez
from Bio import SeqIO
import sys


# Read input file
def read_file(file_name):
    with open(file_name, 'r') as f:
        ids = f.readline().strip().split(' ')
    return ids


# Write output file
def write_file(file_name, res_id, data, size):
    with open(file_name, 'w') as f:
        f.write(res_id + '\n')
        counter = 0
        for letter in data:
            f.write(letter)
            counter += 1
            if counter % size == 0:
                f.write("\n")
        f.write("\n")


# Get the shortest sequence string and it's id
def get_shortest_string(email, ids):
    Entrez.email = email
    handle = Entrez.efetch(db='nucleotide', id=ids, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))
    len_recs = []
    for i in range(len(records)):
        len_recs.append(len(records[i].seq))

    shortest = len_recs.index(min(len_recs))
    res_id = '>' + str(records[shortest].description)
    res_seq = str(records[shortest].seq)

    return res_id, res_seq


def main():
    email = sys.argv[1]
    ids = read_file('rosalind_frmt.txt')
    res_id, res_seq = get_shortest_string(email, ids)
    write_file('output_frmt.txt', res_id, res_seq, 70)


if __name__ == "__main__":
    main()
    
