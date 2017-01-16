#!/usr/bin/env python
# @program: to rotate a NxN matrix by 90 degree using temp space
# @author: A. De

from sys import argv
from string import letters
from random import choice

def print_mat(matrix):
	for row in matrix:
		print row

# initialize matrix with random values
def init_mat():
	mat = []
	m = int(argv[1])
	for i in range(0, m):
		line = []
		for j in range(0, m):
			line.append(choice(letters))
		mat.append(line)
		del(line)
	return mat

def rotate_right(matrix):
	size = len(matrix)
	layer_count = size / 2 # travel half way in any direction and we reach the center
	# for each layers
	for layer in range(0, layer_count):
		first = layer              # first element
		last = (size - 1) - layer  # last element
		# In each layer, loop from first lo the second last element as these are the quadrants that we swap
		for element in range(first, last):
			offset = element - first # to travel backwards, subtract this to the last elemet index

			# Order of operation
			# 1 2
			# 3 4
			
			# store values for swap in temp location
			# top left
			top = matrix[first][element]
			# top right
			right = matrix[element][last]
			# botom right
			bottom = matrix[last][last-offset]
			#bottom left
			left = matrix[last-offset][first]
			
			# DEBUG
			# print 'Layer ', layer, 'Element ', element, 'Top ', top
			# print top,'     ',right
			# print left,'     ',bottom
			# print

			# swap values 
			# top left <- bottom left
			matrix[first][element] = left
			# top right <- top left
			matrix[element][last] = top
			# bottom right <- top right
			matrix[last][last-offset] = right
			# bottom left <- bottom right
			matrix[last-offset][first] = bottom
# Main
if len(argv) != 2:
	exit(1)
mat = init_mat()
print 'Initial Matrix'
print_mat(mat)
print 'Rotated right'
rotate_right(mat)
print_mat(mat)
