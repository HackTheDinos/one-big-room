import flask
import sys
import logging

class MyFlask(flask.Flask):
    def get_send_file_max_age(self, name):
        return 60

app = MyFlask(__name__)

app.debug = True
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

import views
import api