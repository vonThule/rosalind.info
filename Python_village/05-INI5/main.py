#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: main.py
    Location: Python village
    Project: Rosalind.info
    Author: Alexander Popp
    Date created: 08/23/2018
    Date last modified: 8/23/2018
    Python version: 3.6.5
    Description:
        INI5: Given a file containing at most 1000 lines, return a file
        containing all the even-numbered lines from the original file.
        Assume 1-based numbering of lines.
"""


# Read input file
def read_file(file_name):
    values = []
    with open(file_name, 'r') as f:
        for line in f:
            values.append(line.strip())
    return values


# Write output file
def write_file(file_name, data):
    with open(file_name, 'w') as f:
        for line in data:
            f.write(str(line) + "\n")
        

# Return every even number line, assume line 0 is line 1
def get_even_number_lines(lines):
    even_lines = []
    for i in range(1, len(lines), 1):
        if i % 2 == 1:
            even_lines.append(lines[i])
    return even_lines


def main():
    lines = read_file("rosalind_ini5.txt")
    result = get_even_number_lines(lines)
    write_file("ini5_output.txt", result)


if __name__ == "__main__":
    main()
    
