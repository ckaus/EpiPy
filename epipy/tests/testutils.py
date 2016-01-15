# -*- coding: utf-8 -*-

from epipy.utils import csvmanager
import matplotlib.pyplot as plt
from matplotlib import gridspec


def normalize(vector):
    return [v * 1.0 / sum(vector) for v in vector]


def read(file_name, seperator, column):
    return csvmanager.CSVManager().read(file_name=file_name, seperator=seperator, column=column)


def plot_with_data(title, xo, yo, yr0, yr1, yr2, l0, l1, l2):
    fig = plt.figure()
    fig.suptitle(title)
    gs = gridspec.GridSpec(3, 3)

    ax0 = fig.add_subplot(gs[0, :])
    ax0.plot(xo, yo, label='Data')
    ax0.plot(xo, yr0, label=l0)
    ax0.legend(loc='best')

    ax1 = fig.add_subplot(gs[1, :])
    ax1.plot(xo, yo, label='Data')
    ax1.plot(xo, yr1, label=l1)
    ax1.legend(loc='best')

    ax2 = fig.add_subplot(gs[2, :])
    ax2.plot(xo, yo, label='Data')
    ax2.plot(xo, yr2, label=l2)
    ax2.legend(loc='best')

    plt.show()


def plot(title, xr, yr0, yr1, yr2, l0, l1, l2):
    fig = plt.figure()
    fig.suptitle(title)
    gs = gridspec.GridSpec(3, 3)

    ax0 = fig.add_subplot(gs[0, :])
    ax0.plot(xr, yr0, label=l0)
    ax0.legend(loc='best')

    ax1 = fig.add_subplot(gs[1, :])
    ax1.plot(xr, yr1, label=l1)
    ax1.legend(loc='best')

    ax2 = fig.add_subplot(gs[2, :])
    ax2.plot(xr, yr2, label=l2)
    ax2.legend(loc='best')

    plt.show()
