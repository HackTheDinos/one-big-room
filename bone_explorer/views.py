from bone_explorer import app
import pystache
import os
from lib import digimorph

pystache.defaults.SEARCH_DIRS.append("./bone_explorer/static/templates")

specimen_url = 'http://digimorph.org/specimens/anas_platyrhynchos/skull'
total_slices = 372
mallardData = {  
  'imageUrl': digimorph.get_preview_url(specimen_url),
  'scientificName':'Anas platyrhynchos',
  'commonName': 'Domestic Mallard',
  'addedBy': 'Richard Ketcham',
  'addedFor': 'David Dufeau and Timothy Rowe',
  'addedByDate': '5/12/98',
  'classification' : ['Aves', 'Anseriformes', 'Anatidae'],
  'wikipedia': 'The mallard or wild duck (Anas platyrhynchos) is a dabbling duck which breeds throughout the temperate and subtropical Americas, Europe, Asia, and North Africa, and has been introduced to New Zealand, Australia, Peru, Brazil, Uruguay, Argentina, Chile, the Falkland Islands and South Africa.[2] This duck belongs to the subfamily Anatinae of the waterfowl family',
  'slice_urls': digimorph.get_slice_urls(specimen_url, total_slices)
}

def mustache_render(tpl_file, data):
    return pystache.render(open('bone_explorer/static/templates/' + tpl_file, 'r').read(), data)

@app.route('/')
def index():
    return mustache_render('index.mustache', { 'pageTitle': 'Bone Explorer'})

@app.route('/specimen')
def specimen():
    pageTitle = 'Specimen Page'

    data = {}
    data['pageTitle'] = pageTitle
    data.update(mallardData)

    return mustache_render('specimen.mustache', data)

@app.route('/search')
def specimenSearch():
    pageTitle = 'Search for Specimens'

    return mustache_render('search.mustache', { 'message': 'Hello!'})

@app.route('/results')
def results():
    #render the search results page
    pageTitle = 'Search Results'

    data = {
       'resultsList' : [ mallardData, mallardData ],
       'pageTitle' : pageTitle
    }
    return mustache_render('results.mustache', data)
