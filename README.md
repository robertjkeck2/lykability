# likability
> Using empythy to score likability based on sentiment analysis of recent tweets about a given person

## Purpose
To piggyback off of the empythy natural languare classifier package to analyze average sentiment of tweets related to a particular person to calculate a 'likability score' for that person.  Useful in tracking sentiment changes across a certain period of time, i.e. the likability score of a celebrity before and after a concert.


## Instructions
1. Open terminal.  Make sure you have ```python3``` and ```pip``` downloaded.
2.```pip install likability```
3. Create a csv file with the names of the people you'd like to analyze for likability.  Name this file name.csv in the current directory.
4. Determine how many recent tweets you'd like to query for each person.  This will be used in the script below as ```num_tweets```.
5. Run Python 3 by typing ```python``` into the terminal.
6. Enter script below to run the LikabilityAnalyzer.
```
from likability import LikabilityAnalyzer
filepath = name.csv #created csv file containing a single row, header of 'Name', and a list of names to score
num_tweets = 100 #the number of recent tweets to query for each name, should be between 100 and 1000
sentimentScore = LikabilityAnalyzer(filepath,num_tweets)
```

