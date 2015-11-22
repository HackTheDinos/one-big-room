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
    "Sharks, Fishes &amp; Other Fish-like Creatures",
    "Amphibians",
    "Mammals and Their Extinct Relatives",
    "Turtles",
    "Lizards, Snakes and Their Relatives",
    "Alligators and Crocodiles",
    "Birds",
    "Dinosaurs, Pterosaurs and Their Extinct Relatives",
    "Primates",
    "Bats"
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
    data.update(specimen.get_detail_view_data(search.get_scan_data(specimen_id)))
    return mustache_render('specimen.mustache', data)

@app.route('/about')
def about():
    return mustache_render('about.mustache', {
        'pageTitle': 'About Bone Explorer'
    })
    return mustache_render('results.mustache', data)

@app.route('/browse')
def browse():
    pageTitle = 'Explore Species'

    data = {
      'pageTitle' : pageTitle,
      'hierarchy' : ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
          
    }

    return mustache_render('browse.mustache', data)
