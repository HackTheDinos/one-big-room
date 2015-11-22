#!/usr/bin/env python
"""Gathers intro paragraph for each species from Wikipedia"""

import pycurl
import json
from StringIO import StringIO

BASE = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles="

SPECIES = ["Alioramus", "Melanerpes", "Saurornithoides"]

for dino in SPECIES:
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, BASE + dino)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    json_data = json.loads(body)
    halfway_json = json_data["query"]["pages"]
    # because this level in between is the page ID
    for key, value in halfway_json.iteritems():
        print value["extract"]

