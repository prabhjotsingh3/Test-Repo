#!/usr/bin/python3

###############################################################################################################
#Python script to split a text file into  multiple files having m lines. m is passed as argument to the script
##############################################################################################################

import os
import sys


if len(sys.argv) < 3:
	print("Insufficient number of argumnets")
	exit()

fname = sys.argv[1]
max_lines = int(sys.argv[2])

print("Opening file - {}".format(fname))
if(os.path.exists(fname) == True):
	fo = open(fname,'r')
else:
	print("File - {} doesn't exist".format(fname))
	exit()


line_ctr = 0;
file_ctr = 1;

fo2 = open("file{}.txt".format(file_ctr),'w')

for line in fo:
	if line_ctr >= max_lines:
		fo2.close()
		line_ctr = 0
		file_ctr += 1
		fo2 = open("file{}.txt".format(file_ctr),'w')
	fo2.write(line)
	line_ctr += 1

fo2.close()

print("Created {} files to split file - {})".format(file_ctr,fname))



fo.close()
