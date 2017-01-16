#!/usr/bin/env python 
# @program: to remove duplicates from an unsorted LL
# @author: abhisek.de@live.com

from linked_list import LinkedList
from random import randint

# global vars
l_list = None;

def init():
	global l_list 
	l_list =  LinkedList()

	for i in range(0, 15):
		data = randint(1, 10)
		l_list.append_data(data)

def del_dup_ll(l_list):
	pin = l_list.head
	while pin != None:
		chk = pin.link
		while chk != None:
			if chk.data == pin.data:
				chk.data = None #Mark the occurance for deletion
			chk = chk.link
		pin = pin.link
	l_list.delete_val(None)
	return l_list

#main
def main():
	init()
	global l_list
	print 'initial list:'
	print l_list
	l_list = del_dup_ll(l_list)
	print 'after removing duplicates:'
	print l_list

if __name__ == '__main__':
	main()
