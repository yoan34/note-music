from .view import View


class Controller:
    def __init__(self, path):
        self.path = path
        self.view = View()
        
    def run(self):
        self.view.showView(self.path)