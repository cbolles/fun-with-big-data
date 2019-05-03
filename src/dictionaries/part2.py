"""
Python dictionaries have a lot more features, this file shows off a couple of them and their uses. Playing around with
these features can make your project more advances
"""

"""
Section 1
Sometimes you might want to go through all the keys in a dictionary, this is pretty easy in python
"""
print('Section 1')

dict_1 = {'name': 'Bob', 'age': 10}  # Notice now you can make a dictionary filled with data

# Here we are saying 'loop through each key in dict_1 and print the key
print('Loop method 1:', end=' ')
for key in dict_1:
    print(key, end=' ')

# We can also explicitly tell python to go through the keys calling dict's keys method
print('\nLoop method 2:', end=' ')
for key in dict_1.keys():
    print(key, end=' ')


"""
Section 2
Being able to loop through the keys means that we can interact with the values in a dictionary by using
the keys of the dictionary. Below we loop through the keys again, but we also print the value associated with it
"""
print('\n\nSection 2')

for key in dict_1:
    print('dict_1[' + key + '] = ' + str(dict_1[key]))


"""
Section 3
We can also loop through just the values if we wanted to. Below we print out only the values stored in the dictionary
"""
print('\nSection 3')

for value in dict_1.values():
    print(value, end=' ')


"""
Section 4
Another useful feature is the ability to quickly check if a key is in the dictionary. Below we see examples of checking
if a dictionary has a specific key
"""
print('\n\nSection 4')

print('Key "hey" in dict_1:', 'hey' in dict_1)
print('Key "name" in dict_1:', 'name' in dict_1)


"""
The above features only start to scratch the surface of what dictionaries can do. Their flexibility opens up a wide
range of possibilities with python. The project will rely on using dictionaries and being able to loop through them
"""