from base import ControllerBase
from model.activity import Activity as ActivityModel

class AdminIndex(ControllerBase):
    def get(self):        
        view_model = {}                
        self.template('admin/index', view_model)
        
class AdminActivity(ControllerBase):
    def get(self):
        
        view_model = {
            'activities': ActivityModel().getAll(), 
            }
        
        self.template('admin/activity', view_model)
        
    def post(self):        
        activity = ActivityModel()        
        activity.name = self.request.get('name')
        activity.put()
        
        self.redirect('/admin/activity')