"""
So far we have seen the basics for how to pull json from the internet. REST APIs are incredibly more powerful then
just pulling JSON off of internet. REST APIs can also be used to interact with just about anything. Below I have
some examples

Sending/Receiving Text Messages
    https://www.twilio.com/

Youtube Analytics
    https://developers.google.com/youtube/analytics/

Machine Learning
    https://cloud.google.com/ml-engine/

Music
    https://developer.spotify.com/
    https://6xq.net/pandora-apidoc/rest/

Sports Stats
    http://nbasense.com/nba-api/

If you want more, look up what you want to interact with and "REST API" to see all of the options.

Next we will look at how we can interact more directly with REST APIs using different HTTP Methods

GET - Get me information to this url
POST - Send information to this url
"""
import requests

"""
Section 1

GET Requests
REST APIs use different HTTP methods. GET is telling the REST API that you want to "get information". We saw this
in part 1 with requests.get This translated to "Ask <url> to give me information"
"""
print('Section 1')

json_data = requests.get('https://api.coinlore.com/api/tickers/').json()
print(json_data['data'][0])

"""
Section 2

GET Parameters
What if we want to get more specific information? How about information about a virtual currency with a specific id?
We can supply parameters through a url

https://api.coinlore.com/api/ticker/?id=90
the "?" represents the beginning of the parameters id is the name with value 90. If you want to have multiple
parameters, separate them with an "&"
https://api.coinlore.com/api/ticker/?id=90&name=bitcoin

Requests makes it easy to send parameters. We set them with a dictionary!. Below is how we can make a get request
with a given parameter
"""
print('\nSection 2')

request_parameters = {'id': 90}  # Note if we wanted to add more parameters, we could keep adding to the dictionary

json_data = requests.get('https://api.coinlore.com/api/ticker/', request_parameters).json()
print(json_data)

"""
Section 3

POST Parameters
When we are making POST requests we need to send more information. We are telling the REST API to do something based on
the post data. For example say we want to use Google Drive's API to upload a file. We need to let the API know what file
is being uploaded, the kind of file, where to put the file etc. We use POST requests to let the REST API that we are
asking it to accomplish a more complicated task

NOTE:
This section doesn't have completed code since to make POST requests you generally need some for of authentication
so that the REST API knows that you have permission to upload information to the server. 

For now we will concentrating on making GET requests to read data 
"""

# post_data = {'filename': 'example.txt', 'file_contents': 'text' ...}
# request.post('https://www.googleapis.com/drive/v2/files', post_data)

