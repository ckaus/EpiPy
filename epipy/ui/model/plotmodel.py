# -*- coding: utf-8 -*-


class PlotModel(object):
    """
    This class represents the plot model. It stores information about the graphs on *PlotViewBox*.

    :returns: an instance of *PlotModel*
    """

    def __init__(self):
        self.x_data = None
        self.y_data = None
        self.y_fitted_data = None
        self.y_base_data = None
        self.regression_values = None

    def get_data(self):
        return {'x': self.x_data, 'y': self.y_data}, {'y_fitted': self.y_fitted_data}, {'y_base': self.y_base_data}

    def __repr__(self):
        return "<x_data=%s, y_data=%s, y_fitted_data=%s, regression_values=%s>" % (
            self.x_data, self.y_data, self.y_fitted_data, self.regression_values)

    def __str__(self):
        return "Regression Values: %s" % self.regression_values
