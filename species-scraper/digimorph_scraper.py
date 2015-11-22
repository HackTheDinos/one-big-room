#!usr/bin/env python

import json
import requests
from bs4 import BeautifulSoup

digimorph = "http://digimorph.org/listbygroup.phtml?grp=dinosaur&sort=CommonName" # test for below

def scrape_digimorph_html_tables(digimorph_url):
	'''gets the list of species from a digimorph
	browse page, super hacky sry'''
	r = requests.get(digimorph_url)
	soup = BeautifulSoup(r.text)
	dinos_hopefully = soup('table')[5].findAll("a").text
	grouped = [dinos_hopefully[i:i+3] for i in xrange(0, len(dinos_hopefully), 3)] 
	chopped = grouped[8:]
	return json.dumps(chopped)

