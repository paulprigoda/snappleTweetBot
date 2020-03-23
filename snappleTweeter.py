import twitter
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random
import re

api = twitter.Api(consumer_key='zEUBp9ddyZ0uQYy9nGITvPx0H',
                  consumer_secret='eiW2KvJ9GOAh9iThxyYRvdTbPNQ4YRxcXk3K7HAjy5W9kG1os6',
                  access_token_key='1214733990759931904-N7QQWMEey0WpeaL5rUGMfjcrkOknM5',
                  access_token_secret='1ZusLHEyEEVWLzB27JIYUfHZ7ydlpmIMAqfD6WWkn1lt1')

def webData():
	driver = webdriver.Chrome()
	driver.get('https://www.snapple.com/real-facts')

	#import pdb; pdb.set_trace()
	content = driver.page_source
	soup = BeautifulSoup(content, features="lxml")
	snapRandValue = str(random.randrange(1,1504))
	print(snapRandValue)

	randFact = soup.find(href=re.compile("""/real-facts/"""+snapRandValue+""""""))

	if randFact == None:
		while randFact == None:
			snapRandValue = str(random.randrange(1,1504))
			print(snapRandValue)
			randFact = soup.find(href=re.compile("""/real-facts/"""+snapRandValue+""""""))
		
	randFact = randFact.get_text()

	print(randFact)
	return randFact, snapRandValue


def snappleTweeter():

	#api.PostDirectMessage("test", "854011872")
	#print('sent')

	#for i in range(10):
	#	api.PostDirectMessage(i, "854011872")
	#	print("sent", i)


	#api.PostUpdate('jess got a big dick')

	#timeline = api.GetUserTimeline(screen_name = '@mad_dog_20')

	#for u in timeline:
	#	print(u.text)

	#api.CreateFriendship('392949439', True)
	#print('friendship created')