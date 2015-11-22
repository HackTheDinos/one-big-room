from bone_explorer import app
import pystache
import os

pystache.defaults.SEARCH_DIRS.append("./bone_explorer/static/templates")

def mustache_render(tpl_file, data):
    return pystache.render(open('bone_explorer/static/templates/' + tpl_file, 'r').read(), data)

@app.route('/')
def index():
    return mustache_render('index.mustache', { 'message': 'Hello!'})

@app.route('/specimen')
def specimen():
    pageTitle = 'Specimen Page'
    data = { 

            'pageTitle': pageTitle,
            'imageUrl':'http://digimorph.org/specimens/anas_platyrhynchos/skull/specimen.jpg',
            'scientificName':'Anas platyrhynchos',
            'commonName': 'Domestic Mallard',
            'addedBy': 'Richard Ketcham',
            'addedFor': 'David Dufeau and Timothy Rowe',
            'addedByDate': '5/12/98',
            'classification' : ['Aves', 'Anseriformes', 'Anatidae']
        }
    return mustache_render('specimen.mustache', data)

@app.route('/search')
def specimenSearch():
    #render the search page

    return mustache_render('search.mustache', { 'message': 'Hello!'})

@app.route('/results')
def results():
    #render the search results page
    return mustache_render('results.mustache', { 'message': 'Hello!'})
