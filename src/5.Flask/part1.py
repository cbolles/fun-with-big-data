"""
Now what if we wanted to make our data available on the web? Lets see how we can use Flask to run a web server
in python. Flask is one of MANY ways to run backend web development. Its a relatively easy tool for back end web
development. Lets look at a hello world example
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/goodbye')
def goodbye():
    return 'Goodbye'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

"""
In your console you should be able to see a URL that was spit out. Go to that URL and you should be able
to see "Hello World". Now go to your_url/goodbye you should be able to see "Goodbye".

Lets walk through the code line by line
8) This is creating a Flask object from the Flask class with the value __name__ based in. This is letting Flask now
what file is running it for some behind the scenes setup. This will be more important later

11 and 16) @app.route(<value>) is telling flask that when ever the user types in the url <our url>/<value> have the
following function control what happens. So when a user types goes to the main page ('/') they will see "Hello World"
when they go to "/goodbye" they will see "Goodbye". Try adding some routes yourself

13 and 18) The functions return what will eventually be seen by the user right now it is just text, but it can be 
JSON, HTML, or other things as well
"""
