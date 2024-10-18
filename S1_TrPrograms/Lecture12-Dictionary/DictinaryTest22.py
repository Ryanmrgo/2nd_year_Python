dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()
print(keys)
print(values)

# iteration
n = 0
for val in values:
    n += val
    print(n)
# keys and values are iterated over in the same order (insertion order)
print(list(keys))
print(list(values))

# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
print(list(keys))
['bacon', 'spam']
# set operations

keys & {'eggs', 'bacon', 'salad'}
#{'bacon'}
#print(list(keys))

keys ^ {'sausage', 'juice'}
#{'juice', 'sausage', 'bacon', 'spam'}

# get back a read-only proxy for the original dictionary
#values.mapping
mappingproxy({'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500})
values.mapping['spam']
#500

