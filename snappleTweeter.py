#!/usr/bin/env python3

import twitter
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random
import re

api = twitter.Api(consumer_key='xxx',
                  consumer_secret='xxx',
                  access_token_key='xx-x',
                  access_token_secret='xxx')

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
			print("Hit None")
			snapRandValue = str(random.randrange(1,1504))
			print(snapRandValue)
			randFact = soup.find(href=re.compile("""/real-facts/"""+snapRandValue+""""""))
		
	randFact = randFact.get_text()
	return randFact, snapRandValue


def snappleDupeCheck(randFact, snapRandValue):

	timeline = api.GetUserTimeline(user_id = '1214733990759931904')
	
	for i in timeline:
		eachTweet = i.text
		if snapRandValue in eachTweet:
			newRandFact, newSnapRandValue = webData()
			return newRandFact, newSnapRandValue
		else:
			return None, None


def main():
	print ("Webscraping...")
	randFact, snapRandValue = webData()
	print(snapRandValue, randFact)

	print("Checking duplicate fact tweets...")
	newFact, newNum = snappleDupeCheck(randFact, snapRandValue)

	print("Posting to Twitter")
	if newFact == None:
		api.PostUpdate('Snapple Fact #'+str(snapRandValue)+': '+randFact)
	elif newFact != None:
		api.PostUpdate('Snapple Fact #'+str(newNum)+': '+newFact)

	print("Done")
main()


