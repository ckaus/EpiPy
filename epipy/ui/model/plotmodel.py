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
        self.regression_values = None

    def set_data(self, x_data, y_data, x_fitted, y_fitted, regression_values):
        self.x_data = x_data
        self.y_data = y_data
        self.x_fitted = x_fitted
        self.y_fitted = y_fitted
        self.regression_values = regression_values

    def get_data(self):
        """
        :returns: the plottable graphs
        """
        return [self.x_data, self.y_data]

    def get_fitted(self):
        return [self.x_fitted, self.y_fitted]

    def __repr__(self):
        return "<%r.%r - " \
               "x_data=%r, " \
               "y_data=%r, " \
               "x_fitted=%r, " \
               "y_fitted=%r, " \
               "regression_values=%r>" % (__name__,
                                          self.__class__.__name__,
                                          self.x_data,
                                          self.y_data,
                                          self.x_fitted,
                                          self.y_fitted,
                                          self.regression_values)

    def __str__(self):
        return "Regression Values: %s" % self.regression_values
