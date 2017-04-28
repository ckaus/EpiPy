# -*- coding: utf-8 -*-

"""A collection of basic fitting and statistic functions for EpiPy."""

import numpy as np
from inspect import getargspec
from random import uniform
from scipy import integrate, optimize
from epipy.lib.core.utils import corr_coef


def fit(model, xdata, N0, ydata=None, params=None, iter=10):
    """Fit given model base initial coordinates with paramters. Are no paramter
    given, this function will use initial guesses for paramters.

    :param callable model: Function which defines an epidemic mo
    :param array xdata: Observation steps
    :param tuple N0: Model values at initial observation step
    :param array ydata: Infected individuals
    :param tuple params: Epidemic model parameters
    :param int iter: Number of iterations

    :returns: The fitted epidemic model, used parameters and correlation
    coefficient.
    :rtype: tuple(array, array, float/None)
    """
    # Population
    N = np.sum(N0)

    def fit_odeint(xdata, *params):
        return integrate.odeint(model, N0, xdata, args=((N,) + params))[:, 1]

    # static fit - Fit a given epidemic model based on parameters.
    if params:
        return fit_odeint(xdata, *params), np.array(params), None
    # Iterative - Fit a given epidemic model and initial guesses for parameters
    # and return the best fitted model based on the correlation coefficient.
    else:
        args, _, _, values = getargspec(model)
        param_size = len(args) - 3
        result = []
        p0 = [uniform(0., 1.) for x in range(param_size)]
        for n in range(iter):
            params, _ = optimize.curve_fit(fit_odeint,
                                           xdata, ydata,
                                           p0=p0,
                                           maxfev=1000)
            fitted = fit_odeint(xdata, *params)
            _corr_coef = corr_coef(ydata, fitted)
            result.append((fitted, params, _corr_coef))
        return sorted(result, key=lambda x: x[2], reverse=True)[0]
