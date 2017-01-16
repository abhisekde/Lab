#! /usr/bin/env python
# @program: to find out if a string is unique or not
# @author: a. de
from sys import argv
__version__ = 2.0

if 1 == len(argv):
	exit(1)

size = len(argv[1])
unique = True

for i in range(0, size-1):
	if argv[1].find(argv[1][i])  != argv[1].rfind(argv[1][i]):
		unique = False
		break

if True == unique:
	print 'String is unique'
else:
	print 'Not a unique string'
