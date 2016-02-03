# -*- coding: utf-8 -*-

from epipy.utils import logging


class ControllerService(object):
    """
    This class represents a service for controller.
    The service can redirect an event to a target view.

    :returns: an instance of *ControllerService*
    """

    def __init__(self):
        self.target_view = None

    def add_target(self, target_view):
        """
        This function adds a view as target view to the controller service.

        :param target_view: a target_view view
        :type target_view: a *QWidget*
        """
        self.target_view = target_view

    def redirect(self, event):
        """
        This function redirects an event to a target view.

        :param event: an occurred event
        :type event: an *Event*
        """
        if self.target_view:
            self.target_view.notify(event)
        else:
            logging.warning("No target_view controller found.")
