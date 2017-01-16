#!/usr/bin/env python
# @program: Class CharMap, maps character to it's count
# @author: A. De

class CharMap:
	def __init__(self, data):
		self.data = data
		self.c_data = ''
		self.c_map = {}
		self.k_list = []
		for c in self.data:
			if self.c_map.has_key(c):
				self.c_map[c] = (self.c_map[c] + 1)
			else:
				self.c_map[c] = 1
				self.k_list.append(c)
	
	def to_string(self):
		for k in self.k_list:
			self.c_data = self.c_data + k + str(self.c_map[k])
		if len(self.data) > len(self.c_data):
			return self.c_data
		else:
			return self.data
