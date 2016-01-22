class ControllerService(object):
    def __init__(self):
        self.origin = None
        self.target = None

    def add_origin(self, origin):
        self.origin = origin

    def add_target(self, target):
        self.target = target

    def redirect(self, event):
        if self.target:
            self.target.notify(event)
        else:
            print "Not target controller found."
