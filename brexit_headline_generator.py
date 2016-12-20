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

import requests, random, bs4, re

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

## 3. Pick a random title and replace 'You' with 'EU'
while True:
	num = random.randint(0, len(titles)-1)
	chosen_title = titles[num]
	if not 'You' in chosen_title:
		continue
	if (chosen_title == 'You'):
		continue
	print(chosen_title.replace('You', 'EU').upper())
	break
