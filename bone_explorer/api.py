from bone_explorer import app
from flask import request, jsonify
from lib.search import test

API_URL = '/api'

@app.route(API_URL + '/search')
def search():
    query = request.args.get('q')
    return jsonify({
        'q': query,
        'results': test()
    })
