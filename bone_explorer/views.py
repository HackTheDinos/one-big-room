from bone_explorer import app
import pystache
import os
from lib import specimen

pystache.defaults.SEARCH_DIRS.append("./bone_explorer/static/templates")

def get_mustache_file(tpl_file):
    return open('bone_explorer/static/templates/' + tpl_file, 'r').read()

def mustache_render(tpl_file, data):
    return pystache.render(get_mustache_file(tpl_file), data)

@app.route('/')
def index():
    data = {
        'pageTitle': 'Search for Specimens',
        'results_template': get_mustache_file('results.mustache'),
    }
    return mustache_render('search.mustache', data)

@app.route('/specimen')
def specimen():
    data = {
        'pageTitle': 'Specimen Page'
    }
    data.update(specimen.get_view_data())
    return mustache_render('specimen.mustache', data)

@app.route('/about')
def about():
    return mustache_render('about.mustache', {
        'pageTitle': 'About Bone Explorer'
    })