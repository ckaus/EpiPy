# -*- coding: utf-8 -*-


class PlotModel(object):
    """
    This class represents the plot model. It stores information about the graphs on *PlotViewBox*.

    :returns: an instance of *PlotModel*
    """

    def __init__(self):
        self.x_data = None
        self.y_data = None
        self.x_fitted = None
        self.y_fitted = None
        self.x_forecast = None
        self.y_forecast = None
        self.regression_values = None

    def get_data(self):
        return [self.x_data, self.y_data], [self.x_fitted, self.y_fitted], [self.x_forecast, self.y_forecast]

    def __repr__(self):
        return "<x_fitted=%s, y_fitted=%s regression_values=%s>" % (
            self.x_fitted, self.y_fitted, self.regression_values)

    def __str__(self):
        return "Regression Values: %s" % self.regression_values
