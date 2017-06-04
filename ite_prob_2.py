#!/usr/bin/python3

##############################################################################################################
#Program that takes one or more filenames as arguments and prints all the lines with more than 40 characrters.
##############################################################################################################

#lines = []

#def read_and_add_lines(fo_:
#	for line in fo:
#		lines.append(line if len(line) > 40))


#Currently we take only one default file
file_list = ["file.txt"]
lines = []
for file_name in file_list:
	with open(file_name,'r') as fo:
		for line in fo:
			if(len(line) > 40):
				print(line,end = '')
