# -*- coding: utf-8 -*-

from epipy.ui.model.inputmodel import InputModel
from epipy.ui.model.optionsmodel import OptionsModel
from epipy.ui.model.plotmodel import PlotModel


class SideBarModel(object):
    """
    This class represents the side bar model of *SideBarWidget*. It stores information about *OptionsModel*,
    *InputModel* and *PlotModel*

    :returns: an instance of *SideBarModel*
    """

    def __init__(self):
        self.options_model = OptionsModel()
        self.input_model = InputModel()
        self.plot_model = PlotModel()

    def __repr__(self):
        return "<%s.%s - input_model=%s, options_model=%s, plot_model=%s>" % \
               (__name__, self.__class__.__name__, self.input_model, self.options_model, self.plot_model)

    def __str__(self):
        return "%s\n%s\n%s" % (self.input_model, self.options_model, self.plot_model)
