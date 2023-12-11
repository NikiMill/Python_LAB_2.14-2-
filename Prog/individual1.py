#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("ind1.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()
    joinon = False
    k = 0
    str = []
    for sentence in sentences:
        for i in sentence:

            if i == '"':

                k += 1
                if k % 2 == 1:
                    joinon = True
                else:
                    del str[0]
                    print("".join(str))
                    joinon = False
                    str = []

            if joinon == True:
                str.append(i)
