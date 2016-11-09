#Part A
import nltk
import random

# import nltk
nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize
from nltk.book import text2

debug = False #True

# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")

tokens = text2[0:150]

# print("TOKENS")
# print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens)
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "CC": "a compound conjunction"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "CC": .1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

#Part B
import requests
from bs4 import BeautifulSoup
import re

baseurl = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
q = requests.get(baseurl)
soup = BeautifulSoup(q.text, 'html.parser')

link = soup.find_all ('img')

for b in link:
	href = b["src"]
	if (href) == 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg':
		print (href)
		b["src"] = 'https://v.cdn.vine.co/v/avatars/6DC374D0-DC74-409F-BDA3-612F1B7483EB-647-0000003BE673C9DD.jpg?versionId=9Ddn9Ozq9kB2wzNvzxO8px.QFPd7I_rh'
		print (b["src"])

for b in link: 
	href = b["src"]
	if not href.startswith("https:"):
		print ("before changing", b["src"])
		b["src"] = 'logo.png'
		print (b["src"])

result = str(soup)

element = soup.prettify()
htmlcode = re.sub('student', 'AMAZING student', element)


f = open('project.html', 'w')
f.write(htmlcode)
f.close()
#Part C
import tweepy

# Unique code from Twitter
access_token = "791353481718272000-1uJ6zKOq3ToiwqRjVIrrqwGQTyFgEjI"
access_token_secret = "3BOBlFtOGCjeJ3gJ2RNt3EBdwCXc6AKrw40k4meDJTO8u"
consumer_key = "Q3FpppLcnC9bNGZHPxTEM1lMC"
consumer_secret = "BButKTpPh3mMDFJicgNqgLoRTW6WfhyBLpaRO8bGh406awUuwF"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
image = "vote.JPG"
message = "Voted for the first time in a historical election! #UMSI-206 #Proj3"
api.update_with_media(image, status=message)


#Part D
import tweepy
from textblob import TextBlob

access_token = "791353481718272000-1uJ6zKOq3ToiwqRjVIrrqwGQTyFgEjI"
access_token_secret = "3BOBlFtOGCjeJ3gJ2RNt3EBdwCXc6AKrw40k4meDJTO8u"
consumer_key = "Q3FpppLcnC9bNGZHPxTEM1lMC"
consumer_secret = "BButKTpPh3mMDFJicgNqgLoRTW6WfhyBLpaRO8bGh406awUuwF"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

avg_count_s = 0
avg_count_p = 0
tweet_count = 0
subjectivity_count = 0
polarity_count = 0 
for tweet in public_tweets:
	tweet_count += 1
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	subjectivity_count += analysis.sentiment.subjectivity
	polarity_count += analysis.sentiment.polarity 
	print(analysis.sentiment)
avg_count_s = subjectivity_count / tweet_count
avg_count_p = polarity_count / tweet_count
print("Average Subjectivity:", avg_count_s)
print("Average Polarity:", avg_count_p)






