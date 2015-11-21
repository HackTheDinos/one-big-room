from bone_explorer import app
import pystache
import os

def mustache_render(tpl_file, data):
    return pystache.render(open('templates/' + tpl_file, 'r').read(), data)

@app.route('/')
def index():
    return mustache_render('index.mustache', { 'message': 'Hello!'})