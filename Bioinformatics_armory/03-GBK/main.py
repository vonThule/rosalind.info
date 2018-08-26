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
        GBK: Given a genus name, followed by two dates in YYYY/M/D format,
        return the number of Nucleotide GenBank entries for the given genus
        that were published between the dates specified.
"""


from Bio import Entrez
import sys


# Read input file
def read_file(file_name):
    with open(file_name, 'r') as f:
        genus = f.readline().strip()
        b_date = f.readline().strip()
        e_date = f.readline().strip()
    return genus, b_date, e_date


# Write output file
def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(str(data) + "\n")


# Get number of nucleotide entries
def get_number_entries(email, genus, b_date, e_date):
    Entrez.email = email
    handle = Entrez.esearch(
        db='nucleotide',
        term=genus + '[Organism]',
        datetype='pdat',
        mindate=b_date,
        maxdate=e_date)
    record = Entrez.read(handle)
    return int(record['Count'])


def main():
    email = sys.argv[1]
    genus, b_date, e_date = read_file('rosalind_gbk.txt')
    result = get_number_entries(email, genus, b_date, e_date)
    write_file('output_gbk.txt', result)


if __name__ == "__main__":
    main()
    
