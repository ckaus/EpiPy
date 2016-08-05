# -*- coding: utf-8 -*-

from epipy.utils import logging


class BaseController(object):
    """
    This class represents the basic class of a controller.
    All controllers inherit this class.
    This controller notify attached views for updating.

    :returns: an instance of *BaseController*
    """

    def __init__(self, parent=None, model=None):
        self.model = model
        self.views = []
        self.parent = parent

    def get_model(self):
        return self.model

    def attach(self, view):
        """
        This function attaches a given view to a controller.

        :param view: a view
        :type view: a *QWidget*
        """
        if view not in self.views:
            self.views.append(view)
        else:
            logging.warning('%s attached already' % view)

    def detach(self, view):
        """
        This function detach a given view from a controller.

        :param view: a view
        :param view: a *QWidget*

        :raises: *ValueError* when view was not attached
        """
        try:
            self.views.remove(view)
            logging.info('View:%s removed' % view)
        except ValueError as error:
            logging.warning('View not attached %s' % error)

    def notify(self, event):
        """
        This function notifies stored views about an *Event*

        :param event: the occurred event
        :type event: an *Event*
        """
        for view in self.views:
            view.update(event)
