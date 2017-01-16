#! /usr/bin/env python
# @program: to check if 2 strings are permutation of each other
# @author: a.de
__version__ = 1.0
from sys import argv
if len(argv) != 3:
	exit(1)

hash_str_1 = {}
hash_str_2 = {}

for alpha in argv[1]:
	hash_str_1[alpha]=alpha

for alpha in argv[2]:
	hash_str_2[alpha]=alpha

if hash_str_1 == hash_str_2:
	print 'Permutation'
else:
	print 'Not permutation'
