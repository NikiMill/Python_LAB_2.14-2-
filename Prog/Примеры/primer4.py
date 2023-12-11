#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# open the file2.txt in read mode. causes error if no such file exists.
with open("file2.txt", "r") as fileptr:
    # running a for loop
    for i in fileptr:
        print(i)  # i contains each line of the file
