from bone_explorer import app
import pystache
import os
from flask import request
from lib import specimen, search

pystache.defaults.SEARCH_DIRS.append("./bone_explorer/static/templates")

def get_mustache_file(tpl_file):
    return open('bone_explorer/static/templates/' + tpl_file, 'r').read()

def mustache_render(tpl_file, data):
    return pystache.render(get_mustache_file(tpl_file), data)

GROUPS = [
    "Non-vertebrates",
    "Sharks, Fishes and Other Fish-like Creatures",
    "Amphibians",
    "Mammals and Their Extinct Relatives",
    "Turtles",
    "Lizards, Snakes and Their Relatives",
    "Alligators and Crocodiles",
    "Birds",
    "Dinosaurs, Pterosaurs and Their Extinct Relatives",
    "Bats",
    "Primates"
]


GROUPS_MAP = [
  { "Non-vertebrates" : ["Arthropods", "Brachiopoda", "Plants", "Echinoderms", "Mollusks", "Foraminifera"] },
  { "Sharks, Fishes and Other Fish-like Creatures" : ["Actinopterygians", "Chondrichthyians", "Actinistia", "Sarcopterygians", "Dipnoi"] },
  { "Amphibians" : ["Anura", "Caudata", "Gymnophiona"]},
  {"Mammals and Their Extinct Relatives" : ["Placentals", "Monotremes", "Basal Synapsids", "Marsupials", "Basal Mammals"]},
  {"Turtles" : ["Cryptodires", "Pleurodires"]},
  {"Lizards, Snakes and Their Relatives": ["Iguanians", "Scleroglossans"]},
  {"Alligators and Crocodiles" : ["Pseudosuchia"]},
  {"Birds" : ["Avians"]},
  {"Dinosaurs, Pterosaurs and Their Extinct Relatives" : ["Pterosaurs", "Non-avian Dinosaurs"]},
  {"Bats" : []},
  {"Primates" : []}
]


IMAGE_GROUPS = [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Slate_pencil_sea_urchin.jpg/1600px-Slate_pencil_sea_urchin.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/5/59/Caribbean_reef_shark.jpg',
    'http://voices.nationalgeographic.com/files/2013/11/poison-dart-frog-pumilio-defenses-s2048x1372-p.jpg',
    '//c1.staticflickr.com/3/2924/14658676205_7c1da2d8d9_h.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Chelonia_mydas_is_going_for_the_air.jpg/1920px-Chelonia_mydas_is_going_for_the_air.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/1/18/Bartagame_fcm.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Alligator_mississippiensis_-_Oasis_Park_-_13.jpg/1920px-Alligator_mississippiensis_-_Oasis_Park_-_13.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/3/32/House_sparrow04.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/6/6d/Laramie_Triceratops_skull.jpg',
'https://upload.wikimedia.org/wikipedia/commons/7/77/Big-eared-townsend-fledermaus.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Brown_Lemur_in_Andasibe.jpg/1599px-Brown_Lemur_in_Andasibe.jpg'
]

@app.route('/')
def index():
    inital_group = request.args.get('group', None);

    data = {
        'pageTitle': 'Search for Specimens',
        'inital_query': request.args.get('query', ''),
        'hierarchy' : getBrowseData(),
        'groups': [ {
                'name': group,
                'selected' : group == inital_group
            } for group in GROUPS ]
    }
    return mustache_render('search.mustache', data)

@app.route('/specimen/<specimen_id>')
def specimen_view(specimen_id=None):
    data = {
        'pageTitle': 'Specimen Page'
    }
    data.update(specimen.get_detail_view_data(search.get_scan_data(specimen_id)))
    return mustache_render('specimen.mustache', data)

@app.route('/about')
def about():
    return mustache_render('about.mustache', {
        'pageTitle': 'About Bone Explorer'
    })
    return mustache_render('results.mustache', data)

def getBrowseData():
    imgGroups = []

    for index, g in enumerate(GROUPS):
      x = {
          'group' : g,
          'image' : IMAGE_GROUPS[index]
        }
      imgGroups.append(x)

    return imgGroups

@app.route('/browse')
def browse():
    pageTitle = 'Explore Species by Groups'
  
    data = {
      'pageTitle' : pageTitle,
      'hierarchy' : getBrowseData() 
    }

    return mustache_render('browse.mustache', data)
