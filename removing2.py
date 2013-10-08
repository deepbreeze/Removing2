#!/usr/bin/env python
import os
import glob
#Get the txt file's name from the directory
list1 = glob.glob('*.txt')
str1 = ''.join(list1)


#Open the txt file which you want to deal with
lines = open(str1,'r').readlines()

#Remove the duplicates
line_set = set(lines)

#Write the results to a new txt file
out = open('Newfile.txt','w')
for line in line_set:
    out.write(line)
out.close()


