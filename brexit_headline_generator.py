#!/usr/bin/python3

###################################################
#
#	Brexit Headline Generator
#
#	Description:
#		Makes stupid headline puns based on films
#		that have 'You' in the title.
#
###################################################

import requests, random, bs4, re, tweepy, time

## 1. Grab the IMDB search results for "You"
imdb_link = 'http://www.imdb.com/find?q=you&s=tt&ref_=fn_al_tt_mr'
r = requests.get(imdb_link)
r.raise_for_status()
site_data = r.text
titles = []

## 2. Parse the search results and strain out the juicy titles
soup = bs4.BeautifulSoup(site_data, 'lxml')
elems = soup.select('.result_text a')
for elem in elems:
	title = elem.get_text()
	titles.append(title)

## 3. Twitter API things
CONSUMER_KEY = 'API_KEY'
CONSUMER_SECRET = 'API_KEY'
ACCESS_KEY = 'API_KEY'
ACCESS_SECRET = 'API_KEY'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

spent_titles = []
for x in titles:
	## 4. Pick a random title and replace 'You' with 'EU'
	while True:
		num = random.randint(0, len(titles)-1)
		chosen_title = titles[num]
		if chosen_title in spent_titles:
			continue
		if not 'You' in chosen_title:
			continue
		if (chosen_title == 'You'):
			continue
		regex = re.compile(r'.*You\w+')
		if regex.match(chosen_title):
			xmod = chosen_title.replace('You', 'EU-').upper()
		else:
			xmod = chosen_title.replace('You', 'EU').upper()
		spent_titles.append(chosen_title)
		break
	api.update_status(status=xmod)
	time.sleep(900)
