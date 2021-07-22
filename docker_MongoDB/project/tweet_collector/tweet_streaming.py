from decouple import config
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import time
import pymongo
import logging
import traceback


logging.basicConfig(filename='debug.log', level=logging.INFO,
                    format='%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y.%m.%d. %H:%M:%S')
# start an engine
client = pymongo.MongoClient("mongodb://mongodb:27017/")
# create a table
db_tweets = client.tweetsdb


def authenticate():
    """Function for handling Twitter Authentication. Please note
       that this script assumes you have a file called config.py
       which stores the 4 required authentication tokens:

       1. API_KEY
       2. API_SECRET
       3. ACCESS_TOKEN
       4. ACCESS_TOKEN_SECRET

    See course material for instructions on getting your own Twitter credentials.
    """
    API_KEY = config('API_KEY')
    API_SECRET = config('API_SECRET')
    ACCESS_TOKEN = config('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')

    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth


class MaxTweetsListener(StreamListener):

    def __init__(self, max_tweets, *args, **kwargs):
        # initialize the StreamListener
        super().__init__(*args, **kwargs)
        # set the instance attributes
        self.max_tweets = max_tweets
        self.counter = 0

    def on_connect(self):
        logging.info('connected. listening for incoming tweets')

    def on_status(self, status):
        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""

        # increase the counter
        self.counter += 1

        tweet = {
            'text': status.text,
            'username': status.user.screen_name,
            'followers_count': status.user.followers_count,
            'location': status.user.location,
            'user_created': status.user.created_at,
            'bg_color': status.user.profile_background_color,
            'user_description': status.user.description,
            'retweets': status.retweet_count
        }

        logging.info('INCOMING NEW DATA!')
        logging.info(
            'New tweet arrived:', tweet["text"], tweet['username'], tweet['followers_count'])
        db_tweets.tweets.insert_one(tweet)
        logging.info('inserted into databse!')

        # check if we have enough tweets collected
        if self.max_tweets == self.counter:
            # reset the counter
            self.counter = 0
            # return False to stop the listener
            return False

    def on_error(self, status):
        if status == 420:
            print(f'Rate limit applies. Stop the stream.')
            return False


if __name__ == '__main__':
    while True:
        try:
            auth = authenticate()
            listener = MaxTweetsListener(max_tweets=100)
            stream = Stream(auth, listener)
            stream.filter(track=['corona'], languages=['en'], is_async=False)
            time.sleep(30)
        except Exception as e:
            logging.error('program error:')
            logging.error(e)
            logging.error(traceback.format_exc())
