import numpy as np

def createDict(id):
    return {
        'id': id,
        'foo': 'bar'
    }

def createDictByOtherOne(dict):
    return {
        'my_custom_id': dict['id'],
        'my_custom_name': dict['name']
    }

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('List of list:')
print(list_of_lists)
print()

array = np.array(list_of_lists)
print('Numpy array of list of list:')
print(array)
print()

flat = np.array(list_of_lists).flatten()
print('Numpy flatten of list of list:')
print(flat)
print()

flat_list = np.array(list_of_lists).flatten().tolist()
print('Numpy flatten to list of list of list:')
print(flat_list)
print()

dicts = list(map(createDict, flat_list))
print('List of dictionaries:')
print(dicts)
print()

list_of_lists_of_dict = [[{'id': 1, 'name': 'gabriel'}], [{'id': 2, 'name': 'john'}], [{'id': 3, 'name': 'mike'}]]
flat_dicts = np.array(list_of_lists_of_dict).flatten().tolist()
result = list(map(createDictByOtherOne, flat_dicts))
print(result)