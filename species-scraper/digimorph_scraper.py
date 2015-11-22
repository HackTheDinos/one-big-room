#!usr/bin/env python

import json
import requests
import argparse
from bs4 import BeautifulSoup

BASE = "http://digimorph.org/specimens"

def scrape_digimorph_html_tables(digimorph_url):
	'''gets the list of species from a digimorph
	browse page, super hacky and bad sry'''
	r = requests.get(digimorph_url)
	soup = BeautifulSoup(r.text)
	dinos_hopefully = soup('table')[5].findAll("a")
	grouped = [dinos_hopefully[i:i+3] for i in xrange(0, len(dinos_hopefully), 3)] 
	chopped = grouped[8:]
	final = []
	for c in chopped:
		for a in c:
			if a.get("name"):
				final.append(a.get("name"))
			if a.get("href"):
				final.append(BASE + a.get("href"))
			if a.text:
				final.append(a.text)
	regrouped = [final[i:i+3] for i in xrange(0, len(final), 3)] # could probably not group twice but ??!?
	keys = ["group", "link", "name"]
	actual_final = []
	for g in regrouped:
		actual_final.append(dict(zip(keys, g)))
	return json.dumps(actual_final)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("durl")
	args = parser.parse_args()
	scrape_digimorph_html_tables(args.durl)
