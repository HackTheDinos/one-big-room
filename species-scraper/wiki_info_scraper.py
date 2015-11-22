#!/usr/bin/env python
"""Gathers intro paragraph for each species from Wikipedia"""

import pycurl
import json
from StringIO import StringIO

BASE = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&redirects&titles="

SPECIES = ["Alioramus", "Melanerpes", "Saurornithoides", "Hydromantes platycephalus"]

def get_intro_json(species):
    all_intros = {}
    for dino in species:
        json_data = make_request(BASE + dino)
        halfway_json = json_data["query"]["pages"]
        # because this level in between is the page ID
        for key, value in halfway_json.iteritems():
            all_intros[dino] = value["extract"]
    return json.dumps(all_intros)

def make_request(url):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    return json.loads(body)

print get_intro_json(SPECIES)
