import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True)


class MainPage(webapp2.RequestHandler):

    def get(self):

        self.response.write("Get request!")
        
        template_values = {
        	'var1': 100,
        	'var2': 'Nick the Stick'
        }
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        
        self.response.write(template.render(template_values))
        
    def post(self):
	    self.response.write("Post request!")
    


application = webapp2.WSGIApplication([
    ('/', MainPage),('/pizzle', MainPage)
], debug=True)