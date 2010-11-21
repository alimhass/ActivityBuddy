from base import ControllerBase

class HomeIndex(ControllerBase):
    def get(self):        
        view_model = {
            'message': 'Hello world 2',
            }
                
        self.template('home/index', view_model)