import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class ControllerBase(webapp.RequestHandler):
    def template(self, path, view_model):
        full_path = os.path.join(os.path.dirname(__file__), '../template/' + path + '.html')
        self.response.out.write(template.render(full_path, view_model))