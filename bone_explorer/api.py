from bone_explorer import app
from flask import request, jsonify
from lib.search import do_search, get_scan_data

from lib import specimen

API_URL = '/api'

@app.route(API_URL + '/search')
def search():
    query = request.args.get('query', None)

    group = request.args.get('group', None)
    if (group):
        groups = [group]
    else:
        groups = []
    
    return jsonify({
        'query': query,
        'results': [ specimen.get_result_view_data(s) for s in do_search(query, groups) ]
    })

@app.route(API_URL + '/scan')
def get_scan():
    id = request.args.get('id', None)
    return jsonify(get_scan_data(id))
