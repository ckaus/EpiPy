# -*- coding: utf-8 -*-


from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.controller.event import Event
from epipy.ui.model.mainmodel import MainModel


class MainWindowController(BaseController):
    """
    This class represents the main view controller.

    :returns: an instance of *MainWindowController*
    """

    def __init__(self, parent=None):
        BaseController.__init__(self, parent, MainModel())

    def set_plot_data(self, x_data, y_data, x_fitted, y_fitted, regression_values):
        self.model.plot_model.set_data(x_data, y_data, x_fitted, y_fitted, regression_values)
        self.notify(Event.PLOT)

    def set_info_text(self, text):
        self.model.info_model.text = str(self.model.plot_model) + text
        self.notify(Event.PRINT_INFORMATION)

    def get_plot_data(self):
        p_model = self.model.plot_model
        return p_model.get_data(), p_model.get_fitted()

    def get_info_text(self):
        self.model.info_model.get_text()

    def clear_information(self):
        self.notify(Event.CLEAR_INFORMATION)
