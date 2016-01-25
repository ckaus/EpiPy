# -*- coding: utf-8 -*-


class BaseController(object):
    def __init__(self):
        self.model = None
        self.views = []

    def attach(self, views):
        if views not in self.views:
            self.views.append(views)

    def detach(self, view):
        try:
            self.views.remove(view)
        except ValueError as error:
            print 'View not attached %s' % error

    def notify(self, event):
        for view in self.views:
            view.update(event)