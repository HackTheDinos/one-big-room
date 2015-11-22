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


IMAGE_GROUPS = [
      'http://digimorph.org/images/urchinsm.jpg',
      'http://digimorph.org/images/sharksm.jpg',
      'http://digimorph.org/images/hylacineriasm.jpg',
      'http://digimorph.org/images/possumsm.jpg',
      'http://digimorph.org/images/turtlesm.jpg',
      'http://digimorph.org/images/sphenodonsm.jpg',
      'http://digimorph.org/images/alligatorsm.jpg',
      'http://digimorph.org/images/emusm.jpg',
      'http://digimorph.org/images/dino.gif',
'https://upload.wikimedia.org/wikipedia/commons/7/77/Big-eared-townsend-fledermaus.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Brown_Lemur_in_Andasibe.jpg/1599px-Brown_Lemur_in_Andasibe.jpg'
]

@app.route('/')
def index():
    inital_group = request.args.get('group', None);
    data = {
        'pageTitle': 'Search for Specimens',
        'inital_query': request.args.get('query', ''),
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
    data.update(specimen.get_detail_view_data(search.getScanData(specimen_id)))
    return mustache_render('specimen.mustache', data)

@app.route('/about')
def about():
    return mustache_render('about.mustache', {
        'pageTitle': 'About Bone Explorer'
    })
    return mustache_render('results.mustache', data)

@app.route('/browse')
def browse():
    pageTitle = 'Explore Species by Groups'
  
    imgGroups = []

    for index, g in enumerate(GROUPS):
      x = {
          'group' : g,
          'image' : IMAGE_GROUPS[index]
        }
      imgGroups.append(x)



    data = {
      'pageTitle' : pageTitle,
      'hierarchy' : imgGroups
    }

    return mustache_render('browse.mustache', data)
