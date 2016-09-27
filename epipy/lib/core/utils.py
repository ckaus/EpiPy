# -*- coding: utf-8 -*-

"""A collection of useful functions for the fitting process."""

from scipy import stats


def corr_coef(ydata_1, ydata_2):
    """Returns the correlation coefficient between y-axis data.

    :param array ydata_1: Data of y-axis-1
    :param array ydata_2: Data of y-axis-2

    :returns: The correlation coefficient of linear least-squares regression
    for two sets.
    :rtype: float
    """
    return stats.linregress(ydata_1, ydata_2)[2] ** 2
