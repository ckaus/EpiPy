# -*- coding: utf-8 -*-


from epipy.ui.model.infomodel import InfoModel
from epipy.ui.model.plotmodel import PlotModel


class MainModel(object):
    """
    This class represents the main view model. It stores information about the *SideBarModel*.

    :returns: an instance of *MainModel*
    """

    def __init__(self):
        self.plot_model = PlotModel()
        self.info_model = InfoModel()

    def get_plot_model(self):
        return self.plot_model

    def get_info_model(self):
        return self.info_model

    def __repr__(self):
        return "<%r.%r - " \
               "side_bar_model=%r, " \
               "plot_model=%r " \
               "info_model=%r>" % (__name__,
                                   self.__class__.__name__,
                                   self.side_bar_model,
                                   self.plot_model,
                                   self.info_model)

    def __str__(self):
        return "Sidebar model: %s\n" % self.side_bar_model
