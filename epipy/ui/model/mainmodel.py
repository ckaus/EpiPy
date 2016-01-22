# -*- coding: utf-8 -*-

from epipy.ui.model.infomodel import LogModel
from epipy.ui.model.plotmodel import PlotModel


class MainModel(object):
    def __init__(self):
        self.log_model = LogModel()
        self.plot_model = PlotModel()
        self.fit_result = None

    def __repr__(self):
        return "<%s.%s - log_model=%s, plot_model=%s>" % \
               (__name__, self.__class__.__name__, self.log_model, self.plot_model)
