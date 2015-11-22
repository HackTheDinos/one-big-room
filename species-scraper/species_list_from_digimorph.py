#!usr/bin/env python

import requests
from bs4 import BeautifulSoup

def get_species_names_from_digimorph(digimorph_url):
    r = requests.get(digimorph_url)
    soup = BeautifulSoup(r.text)
    dinos_hopefully = soup('table')[5].findAll("a")
    grouped = [dinos_hopefully[i:i+3] for i in xrange(0, len(dinos_hopefully), 3)] 
    chopped = grouped[8:]
    data = []
    for c in chopped:
        name = c[1].text.strip()
        data.append(name)
    return list(set(data))
