# -*- coding: utf-8 -*-

from epipy.utils import logging


class ControllerService(object):
    """
    This class represents service for controller.
    This service can redirect an event to a view.

    :returns: an instance of *ControllerService*
    """

    def __init__(self):
        self.target_view = None

    def add_target(self, target_view):
        """
        This function add a target_view view to the controller service.

        :param target_view: a target_view view
        :type target_view: QWidget
        """
        self.target_view = target_view

    def redirect(self, event):
        """
        This function redirect an given event to the target_view view.

        :param event: an event
        :type event: *Event*
        """
        if self.target_view:
            self.target_view.notify(event)
        else:
            logging.warning("No target_view controller found.")
