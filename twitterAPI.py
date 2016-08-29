import tweepy
from twitterKeys import getKeys
 
def getAPI():
	"""Queries token and key from twitterKeys module to access Twitter API

	Returns:
		api (obj): Authenticated Tweepy api object 

	"""

	access_token, access_secret, consumer_key, consumer_secret = getKeys()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	
	return api