class PlotModel(object):
    def __init__(self):
        self.x_data = None
        self.y_data = None
        self.y_fitted_data = None
        self.regression_values = None

    def get_data(self):
        return {'x': self.x_data, 'y': self.y_data}, {'x': self.x_data, 'y': self.y_fitted_data}

    def __repr__(self):
        return "<x_data=%s, y_data=%s, y_fitted_data=%s, regression_values=%s>" % (
            self.x_data, self.y_data, self.y_fitted_data, self.regression_values)

    def __str__(self):
        return "Input X-Data: %s\nInput Y-Data: %s\nFitted Y-Data: %s\nRegression Values: %s" % (
            self.x_data, self.y_data, self.y_fitted_data, self.regression_values)
