from base import ControllerBase
from model.activity import Activity as ActivityModel

class ActivityIndex(ControllerBase):
    def get(self):
        view_model = {
            'activities': ActivityModel().getAll(),
            }
                
        self.template('activity/index', view_model)
        
class ActivityDetail(ControllerBase):
    def get(self, activity):
        view_model = {
            'message': activity,
            }
                
        self.template('activity/detail', view_model)