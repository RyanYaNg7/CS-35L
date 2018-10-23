#Each key is separated from its value by a colon (:), the items are separated by commas, 
#and the whole thing is enclosed in curly braces

# Declaration
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Access
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

# Update

dict['Age'] = 8; # update existing entry
dict['School'] = "UCLA"; # Add new entry


print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']


#Dictionary values have no restrictions. 
#They can be any arbitrary Python object, either standard objects or user-defined objects. 
#However, same is not true for the keys. No duplicate key is allowed. 
#When duplicate keys encountered during assignment, the last assignment wins. For example
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Sarah'}

print "dict['Name']: ", dict['Name']

# Deleting elements
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
print dict
del dict ;        # delete entire dictionary
# Other operations like cmp, len, str etc
