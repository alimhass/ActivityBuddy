from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty()