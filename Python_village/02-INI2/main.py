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
        INI2: Given two positive integers 'a' and 'b', each less than 1000,
        return the integer corresponding to the square of the hypotenuse
        of the right triangle whose legs have lengths 'a' and 'b'.
"""

# Read input file
def read_file(file_name):
    values = []
    with open(file_name, 'r') as f:
        for line in f:
            values.append(line.split())
    return values


# Write output file
def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data + "\n")


# Calculate the square of hypotenuse
def hypotenuse_square(a, b):
    cs = int(pow(a, 2) + pow(b, 2))
    return cs


def main():
    values = read_file('rosalind_ini2.txt')[0]
    a = int(values[0])
    b = int(values[1])
    write_file('ini2_output.txt', str(hypotenuse_square(a, b)))


if __name__ == "__main__":
    main()
    
