from bone_explorer import app
from flask import request, jsonify

API_URL = '/api'

@app.route(API_URL + '/search')
def search():
    query = request.args.get('q')
    return jsonify({
        'query': query,
        'results': [
            {
                'kingdom':  'Animalia',
                'phylum':   'Chordata',
                'order':    'Saurischia',
                'suborder': 'Theropoda',
                'family':   'Tyrannosauridae',
                'tribe':    'Alioramini',
                'genus':    'Alioramus'
            },
            {
                'kingdom':  'Animalia 2',
                'phylum':   'Chordata 2',
                'order':    'Saurischia 2',
                'suborder': 'Theropoda 2',
                'family':   'Tyrannosauridae 2',
                'tribe':    'Alioramini 2',
                'genus':    'Alioramus 2'
            }
        ]
    })