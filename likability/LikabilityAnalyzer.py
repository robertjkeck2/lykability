import os
import time
import pandas as pd 
import numpy as np 

from twitterAPI import getAPI
from findSentiment import findSentiment
from getTweets import getTweets

class LikabilityAnalyzer(object):
	"""Queries Twitter for tweets containing names given in csv file and uses empythy to give each name a likability score.

	Attributes:
		path (str): File name in current directory of csv containing names to be queried
		num_tweets (int): Total number of tweets to be queried

	"""

	def __init__(self,path,num_tweets):
		self.path = os.getcwd() + '/' + path
		self.max_tweets = num_tweets

	def score(self):
		"""Outputs a csv titled 'Sentiment' that gives a likability score to each name given in query csv
	
		"""

		df = pd.read_csv(self.path, header=0)

		df1 = df['Name']

		api = getAPI()

		tweets = getTweets(self.max_tweets,api)

		pred = [0 for i in range(0,len(df1))]
		df.insert(1, 'Sentiment',pred)

		start_time = time.time()

		for i in range(0,len(df1)):
			sentiment = findSentiment()
			sentiment.train()
			tweets.search(df1[i])
			df = df.drop('Sentiment',1)
			name = df1[i]
			filename = name.replace(" ", "") + 'Tweets'
			pred[i] = sentiment.analyze(filename,self.max_tweets)
			os.remove(filename)
	
			df.insert(1, 'Sentiment',pred)
			df.to_csv('Sentiment', sep=',', encoding='utf-8')

		print("Total runtime -- %s seconds --" % (time.time() - start_time))
