#!/usr/bin/env python
# @program: to rotate a NxN matrix by 90 degree using temp space
# @author: A. De

from sys import argv
from string import letters
from random import choice

if len(argv) != 2:
	exit(1)

mat = []
m = int(argv[1])
for i in range(0, m):
	line = []
	for j in range(0, m):
		line.append(choice(letters))
	mat.append(line)
	del(line)
print 'Initial Matrix'
for r in mat:
	print r

print 'Rotated right'
mat2 = []
for i in range(0,m):
	row = []
	for j in range(m-1,-1,-1):
		row.append(mat[j][i])
	mat2.append(row)
	del(row)

for r in mat2:
	print r

print 'Rotated left'
mat3=[]
for i in range(m-1,-1,-1):
	row = []
	for j in range(0,m):
		row.append(mat[j][i])
	mat3.append(row)
	del(row)

for r in mat3:
	print r
