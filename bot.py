import tweepy
import credentials as creds

auth = tweepy.OAuthHandler(creds.CONSUMER_KEY, creds.CONSUMER_SECRET)
auth.set_access_token(creds.ACCESS_TOKEN, creds.ACCESS_SECRET)
api = tweepy.API(auth)

soccer = api.get_user("IlliniSoccer")
