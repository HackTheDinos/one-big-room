#! user/bin/env python

import requests
import argparse

BASE = "http://api.gbif.org/v1/species/search?q='"
SPECIES = ["Alioramus", "Melanerpes", "Zanabazar"] # edit with actual data

def make_urls(base, param_list):
	return [base + p for p in param_list]

def hit_the_api(url_list):
	json_mega = [requests.get(u).json()["results"][0] for u in url_list]
	return json_mega

