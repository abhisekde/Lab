#!/usr/bin/env python
# @program: to check if string 2 is the reverse of string 1
# @author: abhisek.de@live.com

from sys import argv

def isSubString(haystack, niddle):
	is_present = haystack.find(niddle, 0, len(haystack))
	if is_present > -1:
		return True
	else:
		return False

def is_reverse(str1, str2):
	if len(str1) != len(str2):
		return False
	# assuming len(str1) >= len(str2)
	rev_str1 = ''.join(reversed(str1)) #reverse the string
	is_sub = isSubString(str2, rev_str1)
	return is_sub

# Main
if len(argv) != 3:
	print 'usage: ', argv[0], ' first_string second_string'
	exit(1)

str1 = argv[1]
str2 = argv[2]

print is_reverse(str1, str2)
