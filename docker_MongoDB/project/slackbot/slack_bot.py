
import sqlalchemy
import psycopg2
#import requests

webhook_url = "webhook goes here but you also need the slack api key and secret details!"

joke = pyjokes.get_joke()

# We take some data and store in a dictionary (tweet / joke / series of tweets)
data = {'text': joke}

# We post that data to the slack channel via an http request
requests.post(url=webhook_url, json = data)
