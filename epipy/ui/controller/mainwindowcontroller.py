# -*- coding: utf-8 -*-


from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.controller.event import Event
from epipy.ui.model.mainmodel import MainModel


class MainWindowController(BaseController):
    """
    This class represents the main view controller.

    :param controller_service: a controller service
    :type controller_service: an instance of *ControllerService*

    :returns: an instance of *MainWindowController*
    """

    def __init__(self, controller_service):
        BaseController.__init__(self)
        self.model = MainModel()
        self.controller_service = controller_service
        self.controller_service.add_target(self)

    def get_model(self):
        """
        :returns: an instance of *MainModel*
        """
        return self.model

    def get_controller_service(self):
        """
        :returns: an instance of the *ControllerService*
        """
        return self.controller_service

    def set_side_bar_model(self, side_bar_model):
        """
        This function sets the side bar model to main model and notify the information view to print information.

        :param side_bar_model: a side bare model
        :type side_bar_model: an instance of *SideBarModel*
        """
        self.model.side_bar_model = side_bar_model
        self.notify(Event.PRINT_INFORMATION)

    def clear_information(self):
        """
        This function notifies the information view to clear the information.
        """
        self.notify(Event.CLEAR_INFORMATION)
