from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from controller.home import HomeIndex
from controller.account import AccountIndex
from controller.activity import ActivityIndex, ActivityDetail
from controller.admin import AdminIndex, AdminActivity

path = [('/', HomeIndex),
        ('/account', AccountIndex),
        ('/a/', ActivityIndex),
        ('/a/(.*)', ActivityDetail),
        
        ('/admin', AdminIndex),
        ('/admin/activity', AdminActivity),
        ]

facebook_config = [
                   '173552245992905',
                   'fbbc37c04a14771c9977663613eccb55',
                   '8e7237ebda88af27fb9d01ef1623eb69',
                   ]

application = webapp.WSGIApplication(path, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
