from google.appengine.ext import db

class Activity(db.Model):
    name = db.StringProperty()
    
    def getAll(self):
        return self.gql('ORDER BY name')