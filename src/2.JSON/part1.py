"""
JSON stands for Javascript Object Notation and is one of the most used standards for sending information over the
internet. Websites will use it to send information between the client and the server side. Many mobile apps will
communicate with other services using JSON. This file will give you a look at how to get JSON and what it looks like
"""
import json
import os

"""
Section 1.
Open person.json to see the first example of JSON. It should look familiar. JSON objects and Python dictionaries
share a common structure. JSON also stored data as key-value pairs. Below I have created the same data in the form
of a python dictionary.
"""
print('Section 1')
name = dict()
person = dict()

name['first'] = 'Bob'
name['last'] = 'Smith'

person['name'] = name
person['age'] = 55
print('person', person)


"""
Section 2
JSON and python dictionaries are actually so similar that we can convert between the two very easily! This time instead
of creating person using python. Ill open the person.json file, put the value into a dictionary, then loop through the
keys of the dictionary and print out the data. I'll import json so that I can convert from json to a dictionary
"""
print('\nSection 2')
person_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'person.json')  # Make sure I get the right file

with open(person_file, 'r') as json_file:
    data = json.load(json_file)

for key in data:
    print('data[' + key + '] = ' + str(data[key]))


"""
Section 3
We can convert between JSON and dictionaries in many different ways. We can also convert from JSON in a string to a
python dictionary. Below we have JSON in a string which we convert to a dictionary. This time we call "loads" the extra
s stands for string
"""
print('\nSection 3')

txt = '{"example" : 5, "another" : 7}'
data = json.loads(txt)

for key in data:
    print('data[' + key + '] = ' + str(data[key]))


"""
Section 4
Its very similar going back in the other direction. Instead of calling load and loads, we call dump and dumps. Below
I take a dictionary and dump it as a string which is printed out
"""
print('\nSection 4')
out = {'hey': 5, 'there': 9}
print(json.dumps(out))

"""
Being able to convert to and from JSON is a powerful tool. Since we can convert from any file or text, if we can get
access to JSON as a string then we can directly convert to a dictionary. This opens the ways that you can use python
to interact with data. 

Create a new .json file called bank that has the attributes number of accounts, total money, and the name of the
manager. Load the .json file into a dictionary using json.load and print out the average amount of money in each
account
"""
