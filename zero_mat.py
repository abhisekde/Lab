#!/usr/bin/env python
# @program: to print the zero matrix of a given matrix
# @author: abhisek.de@live.com

from random import randint

def get_init_matrix():
	matrix = []

	for i in range(0,5):
		row = []
		for j in range(0, 5):
			row.append(randint(1,9))
		matrix.append(row)
		del(row)

	rand_i = randint(0, 4)
	rand_j = randint(0, 4)
	matrix[rand_i][rand_j] = 0

	return matrix

def print_mat(matrix):
	for i in range(0, len(matrix)):
		print matrix[i]

def get_zero_mat(matrix):
	rows = len(matrix)
	cols =  len(matrix[0])
	for i in range(0, rows):
		for j in range(0, cols):
			if matrix[i][j] == 0:
				for k in range(0, rows):
					matrix[k][j] = 0
				for k in range(0, cols):
					matrix[i][k] = 0
				return matrix  # that's it. exit here

# Main 
matrix = get_init_matrix()
print 'initial matrix'
print_mat(matrix)
print 'zero matrix'
print_mat(get_zero_mat(matrix))
