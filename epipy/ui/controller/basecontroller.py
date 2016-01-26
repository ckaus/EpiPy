# -*- coding: utf-8 -*-


class BaseController(object):
    """
    This class represents a basic class of a controller.
    All controller inherit this class.
    This controller notify attached views for updating.

    :returns: an instance of *BaseController*
    """

    def __init__(self):
        self.model = None
        self.views = []

    def attach(self, view):
        """
        This function attach a given view to a controller.

        :param view: a view
        :type view: *QWiget*
        """
        if view not in self.views:
            self.views.append(view)

    def detach(self, view):
        """
        This function detach a given view from a controller.

        :param view: a view
        :param view: *QWidget*
        :raises: *ValueError* when view was not attached
        """
        try:
            self.views.remove(view)
        except ValueError as error:
            print 'View not attached %s' % error

    def notify(self, event):
        for view in self.views:
            view.update(event)
