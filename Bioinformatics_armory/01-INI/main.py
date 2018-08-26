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
        INI: Given a DNA string 's', of length at most 1000bp, return
        four integers, separated by spaces, representing the respective
        number of times that the symbols 'A', 'C', 'G' and 'T' occur
        in 's'.
"""


from Bio.Seq import Seq


# Read input file
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readline()


# Write output file
def write_file(file_name, data):
    with open(file_name, 'w') as f:
        for base in data:
            f.write(str(data[base]) + " ")
        f.write("\n")


# Count base pair occurence
def count_occurence(sequence, base):
    return sequence.count(base)


def main():
    result = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    sequence = Seq(read_file('rosalind_ini.txt'))
    for base in result:
        result[base] = count_occurence(sequence, base)
    write_file('output_ini.txt', result)


if __name__ == "__main__":
    main()
    
