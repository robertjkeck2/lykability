from empythy import EmpathyMachines
import os
import json

class findSentiment(object):
	"""Uses empythy package to determine tweet sentiment and aggregate into likability score.

	"""

	def __init__(self):
		self.results = []
		self.scores = []
		self.nlp = EmpathyMachines()

	def train(self):
		"""Trains the natural language classifier from EmpathyMachines module

		"""

		self.nlp.train(verbose=False)

	def analyze(self,path,num_tweets):
		"""Predicts sentiment using EmpathyMachines module and calculates weighted likability score.

		Args:
			path (str): File name in current directory for csv file with tweets for a given name 
			num_tweets (int): Total number of tweets queried for each name

		Returns:
			sum(self.scores) (float): Calculated likability score for given name

		"""

		with open(path, 'r') as fileHandler:
			jsonData = json.load(fileHandler)
		tweets = jsonData

		if len(tweets) > 0:
			for tweet in tweets:
				self.results.append(self.nlp.predict(tweets))

			for result in self.results[0]:
				if result == 'positive':
					self.scores.append((1/num_tweets))
				elif result == 'negative':
					self.scores.append(-(1/num_tweets))
				else:
					self.scores.append(0)

		else:
			return(0)

		return sum(self.scores)
