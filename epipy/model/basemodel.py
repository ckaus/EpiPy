# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from scipy import optimize, stats
<<<<<<< HEAD

from epipy.utils import logging
=======
import inspect
>>>>>>> origin/yena


class BaseModel(object):
    """
    This class represents an abstract model for epidemic models.
    """

    def __init__(self):
        __metaclass__ = ABCMeta
        self.N = None
        self.N0 = None

    def _line_regression(self, y_data_1, y_data_2):
        """
        This function trigger a calculation of a regression line.
        Return R^2 and p-value of linear regression between x and y
        where x and y are array-like.

        :param y_data_1: data on y-axis
        :type y_data_1: a list
        :param y_data_2: data on y-axis
        :type y_data_1: a list
        :returns: see scipy.stats.stats.linregress
        """
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            y_data_1, y_data_2)
        return slope, intercept, r_value ** 2, p_value, std_err

    def fit(self, x_data, y_data, N=None, with_line_regress=True, **parameters):
        """
        This function fit a given data set (x_data, y_data) with on an epidemic model.

        :param x_data: data on x-axis
        :type x_data: list
        :param y_data: data on y-axis
        :type y_data: list
        :param N: population
        :type N: int
        :param with_line_regress: with line regression
        :type with_line_regress: bool
        :param parameters: model parameters
        :type parameters: mapping of values
        :return: the y-fitted-data as list, used parameters, in case of
        with line regression some regression information between y-data and y-fitted-data
        """
        try:
            self.N = N
            self.N0 = self.init_param(y_data[0])
            if not parameters:
                param, pcov = optimize.curve_fit(self.fit_model, x_data, y_data)
                fitted = self.fit_model(x_data, *param)
                _parameters = param.tolist()
            else:
                fitted = self.fit_model(x_data, **parameters)
                _parameters = parameters.values()
            result = (fitted, _parameters)
            if with_line_regress:
                return result + self._line_regression(y_data, fitted)
            return result

        except RuntimeError as error:
            logging.error('Runtime Error %s' % error)
            return

    @abstractmethod
    def init_param(self, y0):
        pass

    def __repr__(self):
        return '<object=%s - Population=%s - Initial Parameter=%s - >' % (
            self.__class__.__name__, self.N, self.N0)

    def __str__(self):
        return '%s - %s\nPopulation: %s\nInitial Parameter %s' \
               % (self.__name__, self.__class__.__name__, self.N, self.N0)
