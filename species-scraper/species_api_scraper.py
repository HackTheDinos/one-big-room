#!usr/bin/env python

import requests
import argparse
import json

BASE = "http://api.gbif.org/v1/species/search"
# SPECIES = ["Alioramus", "Melanerpes", "Zanabazar"]

def get_species_data(base, param_list, species_group):
	for p in param_list:
		payload = {"q": p}
		try:
			r = requests.get(BASE, params=payload).json()["results"][0]
			with open(species_group + ".json", "a") as f:
				f.write(json.dumps(r))
				f.write("\n")
		except IndexError:
			pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("params", nargs="+")
	args = parser.parse_args()
	get_species_data(BASE, params)
