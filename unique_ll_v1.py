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
	n_list = LinkedList()
	v_map = {}
	i_pin = l_list.head
	while i_pin != None:
		if v_map.has_key(i_pin.data) == False:
			n_list.append_data(i_pin.data)
			v_map[i_pin.data] = 'X' 
		else:
			None
		i_pin = i_pin.link
	
	return n_list

# main
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
