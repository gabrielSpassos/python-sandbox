#!/usr/bin/python

list = ['1b4f49b0cdad4fc5bdec2f44f52dba67', 'eb24bf4b4b164644b9e1d8858fad8c55', 'e76e0c06de5545fd9e1afbfa323911da']
empty_list = []

print("Original list", list)
print("Empty list", empty_list)

# Join the list with comma
comma_separated = ','.join(list)

print("Transformation", comma_separated)
print('Ternary with list', True if list else False)
print('Ternary with empty list', True if empty_list else False)

