"""
This example will go over how we could use a REST API. Lets say we want to find the average price for the first 25
virtual currencies using the REST API that was used in the previous examples. We will start by calling the REST API,
getting the JSON, looping through the data, and calculating the average. Below is what the JSON looks like from the
documentation
https://www.coinlore.com/cryptocurrency-data-api

{
  "data": [
    {
      "id": "90",
      "symbol": "BTC",
      "name": "Bitcoin",
      "nameid": "bitcoin",
      "rank": 1,
      "price_usd": "6456.52",
      "percent_change_24h": "-1.47",
      "percent_change_1h": "0.05",
      "percent_change_7d": "-1.07",
      "price_btc": "1.00",
      "market_cap_usd": "111586042785.56",
      "volume24": 3997655362.9586277,
      "volume24a": 3657294860.710187,
      "csupply": "17282687.00",
      "tsupply": "17282687",
      "msupply": "21000000"
    },
    ...
    ],
  "info": {
    "coins_num": 1969,
    "time": 1538560355
  }
}

So we have a value "data" which is a list that contains some nested json objects (dictionaries). Inside this object
there is a "price_usd" key with a string value of its worth. If we loop through the "data" array and convert the value
associated with "price_usd" we can get the price of each virtual currency.
"""
import requests

"""
Step 1 
First we need to get the response from the REST API. We needs to make parameters that will limit the output to be just
25 virtual currencies. Then we get the data back by calling .json() on the get result
"""
get_parameters = {'limit': 25}  # The documentation shows how we can request for a limited data as response
response_data = requests.get('https://api.coinlore.com/api/tickers/', get_parameters).json()

"""
Step 2
We need to sift out the data we care about. Im going to make an array that will hold all the information we care about.
In it will be the names and the prices of the currency in the format
[ [name, price], [name, price], [name, price] ]
"""
useful_data = []
for coin in response_data['data']:
    currency_name = coin['name']
    currency_value = float(coin['price_usd'])
    useful_data.append([currency_name, currency_value])

"""
Step 2.5
Lets look at what the data we just collected looks like.
"""
print('\nStep 2.5')
for coin in useful_data:
    print(coin[0], coin[1])  # Name is the first value in the array, price is the second value

"""
Step 3
Calculating the average is straight forward from here, you can get fancy with python wizardry, but lets keep it simple
for now
"""
total = 0.0
for coin in useful_data:
    total += coin[1]
average = total / len(useful_data)
print('\nThe average is', average)

"""
Try below to get the total value accross 13 results of the volumn24 value
"""
