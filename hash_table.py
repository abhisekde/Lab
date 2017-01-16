#! /usr/bin/env python
# Hash table implementation in Python
# @abhisekde
#1. Create empty hash table (dictionary)
hash_table = {}
#2. Add item to it
hash_table['hello'] =  'hola'
hash_table['bye'] = 'adios'
#3. Access table item by index
print hash_table['bye']
#4. Update values
hash_table['hello'] = 'bonjour'
print hash_table['hello']
#5. Invalid index access
#rint hash_table['say']
