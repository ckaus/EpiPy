# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from inspect import getargspec
from numpy import inf
from random import uniform
from scipy import optimize, stats

from epipy.utils import logging


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
                fitted, param_pcov, line_regression = self.iterate_fit(self.fit_model, x_data, y_data)
                _parameters = param_pcov[0].tolist()
                return fitted, _parameters, line_regression
            else:
                fitted = self.fit_model(x_data, **parameters)
                if with_line_regress:
                    return fitted, parameters.values(), self._line_regression(y_data, fitted)
                return fitted, parameters.values()

        except RuntimeError as error:
            logging.error('Runtime Error %s' % error)
            return

    def iterate_fit(self, model, x_data, y_data):
        """
        This function repeats the fitting with random initial guesses for parameters.
        
        :param model: model function of an epidemic model class
        :type model: function
        :param x_data: data on x-axis
        :type x_data: list
        :param y_data: data on y-axis
        :type y_data: list

        :returns: the set of parameters of the best fit
        """
        results = []
        args, _, _, values = getargspec(self.model)
        param_size = len(args) - 3
        for n in range(10):
            param, pcov = optimize.curve_fit(model, x_data, y_data, p0=[uniform(0., 1.) for x in range(param_size)],
                                             bounds=(0, inf), max_nfev=1000)
            fitted = self.fit_model(x_data, *param)
            line_regression = self._line_regression(y_data, fitted)
            results.append((fitted, (param, pcov), line_regression))
            # sort fitted models by qualities and return best fitted model
        return sorted(results, key=lambda x: x[2][2], reverse=True)[0]

    @abstractmethod
    def init_param(self, y0):
        pass

    def __repr__(self):
        return '<object=%s - Population=%s - Initial Parameter=%s - >' % (
            self.__class__.__name__, self.N, self.N0)

    def __str__(self):
        return '%s - %s\nPopulation: %s\nInitial Parameter %s' \
               % (self.__name__, self.__class__.__name__, self.N, self.N0)
