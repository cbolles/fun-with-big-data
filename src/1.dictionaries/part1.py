"""
Python dictionaries are incredibly powerful. They can handle getting just about any kind of data. This file will
walk you through how flexible 1.dictionaries can be and what they "look like"
"""

"""
Section 1
Creating dictionaries is pretty easy and there are two main ways to do it, they work just about the same. If you
want to learn more about the differences checkout 
`Link <https://medium.com/@jodylecompte/dict-vs-in-python-whats-the-big-deal-anyway-73e251df8398>`
"""
print('Section 1')
dict_1 = dict()  # Explicitly create an empty dictionary
dict_2 = {}  # Another way to create an empty dictionary

print('dict_1', dict_1)
print('dict_2', dict_2)

"""
Section 2
Adding to dictionaries is pretty straight forward. Dictionaries contain "key-value" pairs that are used to represent
all data. This is similar to how classes work in Python. The example below shows how dictionaries and classes can
work in similar ways
"""
print('\nSection 2')


class ExampleClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'a: ' + str(self.a) + ' b: ' + str(self.b)


class_example = ExampleClass(8, 9)
dict_1['a'] = 8
dict_1['b'] = 9

print('class_example', class_example)
print('dict_1', dict_1)


"""
Section 3
The big difference is that dictionaries are not limited in the values they can hold. We can keep adding values to
dictionaries as we want
"""
print('\nSection 3')

dict_1['some'] = 'more'
dict_1['examples'] = 'are here'

print('dict_1', dict_1)

"""
Sections 4
Dictionaries can also hold multiple time at once, lists, ints, strings can all be possible values
"""
print('\nSection 4')

dict_1[9] = 'hey'
dict_1['there'] = 11
print('dict_1', dict_1)


"""
Section 5
One of the most powerful features is that dictionaries can also store dictionaries in them! Having nested dictionaries
means that we can store more complicated structures. Below we will make a Person which has a name and an age.
"""
name = dict()
person = dict()

name['first'] = 'Jimmothy'
name['last'] = 'Bob'

person['name'] = name
person['age'] = 19
print('person', person)

"""
That covers the very basics of dictionaries, there are a lot of other powerful features so will be covered in part2,
but play around with this file to make sure everything makes sense. Try updating the person dictionary to have
an address key with a dictionary to store information on the address something like below
person {'name': {'first': 'Jimmothy', 'last': 'Bob'}, 'age': 19, 'address': {'street': 'first', 'number': 13}}
"""
