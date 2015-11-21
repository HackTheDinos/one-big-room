import os
import flask
import sys
import logging
import pystache

app = flask.Flask(__name__)

app.debug = True
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

def mustache_render(tpl_file, data):
    return pystache.render(open('templates/' + tpl_file, 'r').read(), data)

@app.route('/')
def index():
    return mustache_render('index.mustache', { 'message': 'Hello!'})