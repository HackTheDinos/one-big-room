#!/usr/bin/env python
"""Gathers intro paragraph for each species from Wikipedia"""

import pycurl
import json
import glob
from StringIO import StringIO

SPECIES_FILES = glob.glob('digimorph_species_list/*.json')

BASE = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&redirects&titles="

SPECIES = ["Alioramus", "Melanerpes", "Saurornithoides", "Hydromantes platycephalus"]
MASTER_INTROS = {}

def get_intro_json(list_json):
    all_intros = {}
    species = get_species_list(list_json)
    for dino in species:
        json_data = make_request(BASE + dino)
        halfway_json = json_data["query"]["pages"]
        # because this level in between is the page ID
        for key, value in halfway_json.iteritems():
            if "extract" in value:
                all_intros[dino] = value["extract"]
            else:
                all_intros[dino] = ""
    return all_intros

def get_species_list(list_json):
    species_list = []
    list_json = json.loads(list_json)
    for species in list_json:
        if "species" in species:
            print species["species"]
            species_list.append(species["species"])
    return species_list


def make_request(url):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    return json.loads(body)

for json_file in SPECIES_FILES:
    f = open(json_file, 'r')
    file_json = f.read()
    intros = get_intro_json(file_json)
    MASTER_INTROS[f.name] = intros

with open('intros.json', 'w') as outfile:
    json.dump(MASTER_INTROS, outfile)
