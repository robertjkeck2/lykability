# lykability
> Using empythy to score likability based on sentiment analysis of recent tweets about a given person

## Purpose
To piggyback off of the empythy natural languare classifier package to analyze average sentiment of tweets related to a particular person to calculate a 'likability score' for that person.  Useful in tracking sentiment changes across a certain period of time, i.e. the likability score of a celebrity before and after a concert.


## Instructions
- Open terminal.  Make sure you have ```python3``` and ```pip``` downloaded.
- ```pip install lykability```
- Create a csv file with the names of the people you'd like to analyze for likability.  Name this file name.csv in the current directory.
- Determine how many recent tweets you'd like to query for each person.  This will be used in the script below as ```num_tweets```.
- Make sure you have Twitter API keys and access tokens.  If you do not, go to [Twitter Apps](https://apps.twitter.com/), create an app, and find the required keys and tokens under Applications Settings -> Consumer Key (API Key) -> manage keys and access tokens.
- Run Python 3 by typing ```python``` into the terminal.
- Enter script below to run the LikabilityAnalyzer module.
```
from lykability import LikabilityAnalyzer
filepath = 'name.csv'
num_tweets = 100
sentimentScore = LikabilityAnalyzer.analyzer(filepath,num_tweets)
```
- When prompted, enter in your Twitter API keys.  This will allow likability to access the Twitter API to query the tweets needed to complete the sentiment analysis.  
- Wait for script to run to completion.  Please note, due to Twitter API Rate Limiting, querying more than 15 names will lead to longer wait times.  Please allow 1 minute per name for lists greater than 15 names.
- Upon completion, open the newly created Sentiment.csv in the current directory to access the likability scores for each person.


## Possible Usage
- Score top fantasy football players to see what the Twittersphere thinks about each player pre-draft
- Instead of names of people, use product names to track customer sentiment in real-time
- Solve the question: who is more likable, Justin Timberlake or Jimmy Fallon


