#!usr/bin/env python

import re
import requests
from bs4 import BeautifulSoup

digimorph = "http://digimorph.org/listbygroup.phtml?grp=dinosaur&sort=CommonName"

r = requests.get(digimorph)
soup = BeautifulSoup(r.text)
dino_tags= [td for td in soup.find_all("td", attrs={"class": "lightmenuitem"})4:]
chopped = dinos[:4]
grouped = [chopped[i:i+3] for i in xrange(0, len(chopped), 3)] 

