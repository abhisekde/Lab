#!/usr/bin/env python
from char_map import CharMap
from sys import argv

if len(argv) != 2:
	exit(1)

cmap = CharMap(argv[1])
compressed_data = cmap.to_string()
print compressed_data
