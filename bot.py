import tweepy
import re
from time import sleep
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

api = None
manutd = None

def auth():
	#Authenticating API keys
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	#Calling the api
	global api
	api = tweepy.API(auth)

	#Getting Manchester United's handle
	global manutd
	manutd = api.get_user("ManUtd")

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def print_tweets():
	pids = []
	# score = re.compile(r'[0-9]+\s*\-\s*[0-9]+')

	while True:
		for tweet in api.user_timeline(manutd.screen_name):
			try:
				# Retweet tweets as they are found
				tweet.retweet()
				print(tweet.text)
				sleep(60 * 60 * 24)

			except tweepy.TweepError as e:
				print(e.reason)

def main():
	auth()
	print_tweets()

if __name__ == "__main__":
	main()