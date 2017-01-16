#!/usr/bin/env python
# @program: StringBuffer implementation in Python
# @description: stores all the worlds as array and converts it into words only when necessary
# @author: A. De
class StringBuffer:
	def __init__(self):
		self.list = []
		self.text = ''
	
	def toString(self):
		for word in self.list:
			self.text += word
		return self.text

	def append(self, word):
		self.list.append(word)
	__version__ = 1.0
