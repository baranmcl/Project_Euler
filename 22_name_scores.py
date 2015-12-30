#!/usr/bin/python
# -*- coding: utf-8 -*-

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#begin by sorting it into alphabetical order.
#Then working out the alphabetical value for each name, multiply this value by
#its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN,
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

#Credit for this solution goes to Zach Denton. (https://zach.se/project-euler-solutions/22/)
import os
import string

def nameScore(name, index):
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in name) * index

def scoreTotal(name_file):
    opened_file = open(os.path.join(os.path.dirname(__file__), name_file))
    names_string = opened_file.read()
    names = [name.strip('"') for name in names_string.split(',')]
    names.sort()
    return sum(nameScore(name, index + 1) for index, name in enumerate(names))


if __name__ == '__main__':
    print(scoreTotal('names.txt'))
