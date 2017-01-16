#!/usr/bin/env python
# @program: linked list implementation
# @author: abhisek.de@live.com

class Node:
	def __init__(self, data = None, link = None):
		self.data = data
		self.link = link

def __str__(self):
	return self.data

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = self.head # init condition, head is the tail
	
	def __str__(self):
		data_v = []
		pin = self.head
		while pin != None:
			data_v.append(pin.data)
			pin = pin.link
		return str(data_v)

	def append_data(self, data):
		new_node = Node(data)
		if self.head == None:
			self.tail = new_node
			self.head = self.tail # fist item becomes the head
		else:
			self.tail.link = new_node # add the new item to the end
			self.tail = new_node # new item is the tail

	def delete_val(self, value):
		lag = None
		pin = self.head
		while pin != None:
			if pin.data == value:
				if pin == self.head:
					self.head = self.head.link
					pin = pin.link
				elif pin == self.tail:
					self.tail = lag
				else:
					lag.link = pin.link # make lag to point to the next node
					pin = lag.link #update pointer
			else:
				lag = pin #just move fwd.
				pin = pin.link
# Main
def main():
	ll = LinkedList()
	print 'empty list'
	print ll
	print 'list'
	ll.append_data(6)
	ll.append_data(3)
	ll.append_data(5)
	ll.append_data(6)
	ll.append_data(7)
	ll.append_data(6)
	print ll
	print 'remove 6'
	ll.delete_val(6)
	print ll

if __name__ == '__main__':
	main()
