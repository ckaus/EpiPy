# -*- coding: utf-8 -*-


class PlotModel(object):
    def __init__(self):
        self.plot_data = None
        self.fitted_data = None

    def __repr__(self):
        return "<%s.%s -  fitted_data=%s>" % (__name__, self.__class__.__name__, self.fitted_data)

