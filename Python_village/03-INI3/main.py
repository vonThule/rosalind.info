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
        INI3: Given a string 's' of length at most 200 letters and four,
        integers 'a', 'b', 'c' and 'd', return the slice of this string
        from indices 'a' through 'b' and 'c' through 'd' (with space in
        between), inclusively. In other words, we should include elements
        s[b] and s[d] in our slice.
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
        f.write(str(data))


# Slice a string in given position
def string_slice(string, x, y):
    substring = ""
    for i in range(x, x + (y - x) + 1, 1):
        substring += string[i]
    return substring


# Slice a string in given position using string comprehension
def string_slice_lc(string, x, y):
    return string[x:y+1]


def main():
    inputs = read_file("rosalind_ini3.txt")
    string = inputs[0][0]
    a, b, c, d = inputs[1]

    # Get result without using list comprehension
    result = string_slice(string, int(a), int(b)) + " " + string_slice(string, int(c), int(d)) + "\n"

    # Get result using list comprehension
    # result = string_slice_lc(string, int(a), int(b)) + " " + string_slice_lc(string, int(c), int(d)) + "\n"

    write_file("ini3_output.txt", result)


if __name__ == "__main__":
    main()
    
