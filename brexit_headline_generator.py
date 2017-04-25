#!/usr/bin/env python3

###################################################
#
#	Brexit Headline Generator
#
#	Description:
#		Makes stupid headline puns based on films
#		that have 'You' in the title.
#
###################################################

import random
import re
import requests
import bs4
import tweepy

## 1. Grab the IMDB search results for "You"
def site_grabber(url):
    """Pulls site date for given site."""
    req = requests.get(url)
    req.raise_for_status()
    site_data = req.text
    return site_data

SITE_DATA = site_grabber('http://www.imdb.com/find?q=you&s=tt&ref_=fn_al_tt_mr')

## 2. Parse the search results and strain out the juicy titles
def elem_strainer(site_data):
    """Strains out just titles elements from HTML data."""
    titles = []
    soup = bs4.BeautifulSoup(site_data, "html.parser")
    elems = soup.select('.result_text a')
    for elem in elems:
        title = elem.get_text()
        titles.append(title)
    return titles

TITLES = elem_strainer(SITE_DATA)

## 3. Twitter API things
CONSUMER_KEY = 'gdACHWhzhfntu1I8QPTKsvlif'
CONSUMER_SECRET = 'Zd5WeWSOotbtQPDbEXzC4t6WqugHRIHZutoXVveoPatKnfteO1'
ACCESS_KEY = '814845539145646081-dXIeKspt5g1Iv2urqV82uDhBDp1BtKo'
ACCESS_SECRET = '1mpGJgpdjBceGGY51RUOv2PfEeLVrCpubd5zQrCG43Jpk'

def twitter_auth():
    """Return a Twitter authentication object."""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

API_ACCESS = twitter_auth()

## 4. Pick a random title and replace 'You' with 'EU'
def post_to_twitter(api, strings):
    """Posts whatever to Twitter"""
    spent_titles = []
    while True:
        num = random.randint(0, len(strings)-1)
        chosen_title = strings[num]
        if chosen_title in spent_titles:
            continue
        if not 'You' in chosen_title:
            continue
        if chosen_title == 'You':
            continue
        regex = re.compile(r'.*You\w+')
        if regex.match(chosen_title):
            xmod = chosen_title.replace('You', '#EU -').upper()
        else:
            xmod = chosen_title.replace('You', '#EU').upper()
        spent_titles.append(chosen_title)
        print(xmod)
        api.update_status(status=xmod)
        break

post_to_twitter(API_ACCESS, TITLES)
