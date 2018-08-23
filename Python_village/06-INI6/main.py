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
        INI6: Given a string 's' of length at most 10000 letters, return
        the number of occurrences of each word in 's', where words are
        separated by spaces. Words are case-sensitive, and the lines in
        the output can be in any order.
"""


# Read input file
def read_file(file_name):
    values = []
    with open(file_name, 'r') as f:
        for line in f:
            values.append(line.strip().split())
    return values


# Write output file
def write_file(file_name, data):
    with open(file_name, 'w') as f:
        for key in data:
            string = str(key) + " " + str(data[key])
            f.write(str(string) + "\n")


# Count occurrence of each word in a string
def count_occurrences(words):
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
    return counter


def main():
    string = read_file("rosalind_ini6.txt")[0]
    result = count_occurrences(string)
    write_file("ini6_output.txt", result)


if __name__ == "__main__":
    main()
    
