# -*- coding: utf-8 -*-

from epipy.ui.model.inputmodel import InputModel
from epipy.ui.model.optionsmodel import OptionsModel


class SideBarModel(object):
    """
    This class represents the plot model. It stores information about the graphs on *PlotViewBox*.

    :returns: an instance of *PlotModel*
    """

    def __init__(self):
        self.input_model = InputModel()
        self.options_model = OptionsModel()

    def get_input_model(self):
        return self.input_model

    def get_options_model(self):
        return self.options_model

    def __repr__(self):
        return "<%r.%r - " \
               "input_model=%r," \
               "options_model=%r>" % (__name__,
                                      self.__class__.__name__,
                                      self.input_model,
                                      self.options_model)

    def __str__(self):
        return "Input - %s\n" \
               "Options - %s" % (self.input_model,
                                 self.options_model)
