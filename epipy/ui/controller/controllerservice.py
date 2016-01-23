class ControllerService(object):
    def __init__(self):
        self.target = None

    def add_target(self, target):
        self.target = target

    def redirect(self, event):
        if self.target:
            self.target.notify(event)
        else:
            print "No target controller found."
