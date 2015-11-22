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
    data = {}
    for c in chopped:
        name = c[2].text.strip()
        try:
            data[name]["urls"].append(c[2]["href"])
        except KeyError:
            data[name] = {"group": c[0]["name"], "urls": [c[2]["href"]]}
    f = open("url_map.json", "a")
    f.write(json.dumps(data))
    f.write("\n")
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("durl")
    args = parser.parse_args()
    scrape_digimorph_html_tables(args.durl)
