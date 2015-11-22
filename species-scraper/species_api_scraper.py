#!usr/bin/env python

import requests
import argparse

BASE = "http://api.gbif.org/v1/species/search"
# SPECIES = ["Alioramus", "Melanerpes", "Zanabazar"]

def make_urls(base, param_list):
	url_list = []
	for p in param_list:
		payload = {"q": p}
		r = requests.get(BASE, params=payload)
		url_list.append(r.url)
	return url_list

def hit_the_api(url_list):
	json_mega = []
	for u in url_list:
		try:
			json_mega.append(requests.get(u).json()["results"][0])
		except IndexError:
			pass
	return json_mega

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("params", nargs="+")
	args = parser.parse_args()
	urls = make_urls(BASE, args.params)
	hit_the_api(urls)
