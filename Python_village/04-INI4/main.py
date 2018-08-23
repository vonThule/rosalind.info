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
        INI4: Given two positive integers 'a' and 'b', where 'a < b < 10000',
        return the sum of all odd integers from 'a' through 'b', inclusively.
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
        f.write(str(data) + "\n")
        
       
# Calculate sum of all odd integers
def sum_of_odd(a, b):
    sum_odd = 0
    for i in range(a, b + 1, 1):
        if(i % 2 == 1):
            sum_odd += i
    return sum_odd


def main():
    values = read_file("rosalind_ini4.txt")[0]
    a, b = values
    result = sum_of_odd(int(a), int(b))
    write_file("ini4_output.txt", str(result))


if __name__ == "__main__":
    main()
    
