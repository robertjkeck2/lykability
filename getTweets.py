import time
import json
import tweepy

class getTweets(object):
    """Creates a csv file with set number of most recent tweets containing a given query

    Attributes:
        num_tweets (int): Total number of tweets to be queried
        
    """

    def __init__(self,num_tweets,api):
        self.max_tweets = num_tweets
        self.api = api

    def search(self,name):
        """Uses tweepy api.search to create JSON file of most recent tweets without RTs given a query

        Args:
            name (str): Name, word, or phrase to be searched for/queried

        """
        try:
            api = self.api
            tweetResults = []
            query = name + "-filter:retweets"
            tweets = [status for status in tweepy.Cursor(api.search,q=query,lang="en").items(self.max_tweets)]
            for tweet in tweets:
                tweetResults.append(tweet.text)
        
        except Exception as e:
            print("Program Failure.  Error: {}".format(e))
            time.sleep(60*15)

        finally:
            name = name.replace(" ", "")
            with open('{}Tweets'.format(name), 'w') as saveFile:
                json.dump(tweetResults, saveFile)
 