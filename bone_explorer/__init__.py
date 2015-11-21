import flask
import sys
import logging

app = flask.Flask(__name__)

app.debug = True
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

import views