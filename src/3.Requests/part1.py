"""
I mentioned before that JSON is used A LOT to communicate over the web. Now that we know we can take JSON that is in
a string and convert it into a dictionary, lets look at how we can get actually pull JSON from the web. We will
be using requests, a python library for interacting with websites.
"""
import requests

"""
Section 1
REST APIs are like libraries you might use in python, except instead of method calls you use different URLs. Below
I have a comparision between what that looks like with a python class vs a REST API
"""


class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a


example = Example(4, 5)
example.get_a()
# https://www.example.com/get_a

"""
Section 2
At this point you are probably thinking "ok thanks that clarifies exactly 0%" and to that I saw fair, but I wrote
this at 12:30am and I had finals yesterday and haven't written in python for about 6 months. 

Lets look more at what a REST API is, the first link below is a great example of a REST API. The REST API is made up of
"end-points" which are similar to method calls. "End-points" can return JSON! We can use these end-points to collect
data we want. 

After clicking the link on the left hand side you will notice different options "Global, Coins, Coin, etc" if
you click on one it will show you information about the end point and sample output. If you click on one of the
links you will see unformatted JSON. 

If you want to see what the data has easier, copy the unformatted JSON and past it into the left hand box located at the
second link, press "Make Pretty" and you will see the JSON formatted. 

https://www.coinlore.com/cryptocurrency-data-api
https://jsonformatter.org/json-pretty-print
"""

"""
Section 3
Since end-points of REST APIs can return JSON, we can convert the result of the end-points into python dictionaries! 
We just need a way to get the string values of the JSON from the REST APIs

The python library Requests can be used to talk to a website. First lets look at requests talking to google
"""
print('Section 3')
response = requests.get("https://www.google.com")
print(response)

# Well that was anti-climactic

# A 200 response means that it worked!, but lets see what actually is returned
print(response.content)

# All of the HTML!

"""
Section 4
We see that we can use requests to communicate with a website. Now lets see what happens when we use requests on a
RESTFUL API
"""
print('\nSection 4')
response = requests.get("https://api.coinlore.com/api/global/")
print(response.content)

"""
Section 5
Now that we know we can get JSON from a website, we can put it in a dictionary! Notice below that I first
call data[0], if you look at the return of the website you see its a list, I am getting the first value
in the list which is a dictionary (json object)
"""
print('\nSection 5')
response = requests.get('https://api.coinlore.com/api/global/')
data = response.json()
print("Number of coins ", data[0]['coins_count'])


"""
That covers the basics of pulling information from a REST API and using the data in python. Try changing the url
and changing the print statement to show different information from the API
"""