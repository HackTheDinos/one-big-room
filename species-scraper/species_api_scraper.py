#!usr/bin/env python

import requests
import argparse

BASE = "http://api.gbif.org/v1/species/search?q='"
# SPECIES = ["Alioramus", "Melanerpes", "Zanabazar"]

def make_urls(base, param_list):
	return [base + p for p in param_list]

def hit_the_api(url_list):
	json_mega = [requests.get(u).json()["results"][0] for u in url_list]
	return json_mega

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("params", nargs="+")
	args = parser.parse_args()
	urls = make_urls(BASE, args.params)
	hit_the_api(urls)
