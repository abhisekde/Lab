#! /usr/bin/env python
# @program: to find out if a string has unique characters
# @author: A. De
from sys import argv
__version__ = 1.0

# if no input is provided, just exit
if len(argv) == 1:
	exit(1)

map = {}
unique = True

for alpha in argv[1]:
	if map.has_key(alpha):
		unique = False
		break
	else:
		map[alpha]=alpha

if True == unique:
	print 'String is unique'
else:
	print 'Not a unique string'
