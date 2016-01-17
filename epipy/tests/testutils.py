# -*- coding: utf-8 -*-

from epipy.utils import csvmanager
import matplotlib.pyplot as plt
from matplotlib import gridspec


def normalize(vector):
    return [v * 1.0 / sum(vector) for v in vector]


def read(file_name, seperator, column):
    return csvmanager.read(file_name=file_name, seperator=seperator, column=column)


def plot_with_data(title, xdata=[], ydata=[], results=[], labels=[]):
    fig = plt.figure()
    fig.suptitle(title)
    gs = gridspec.GridSpec(len(results), len(results))

    for i in range(0, len(results)):
        ax0 = fig.add_subplot(gs[i, :])
        ax0.plot(xdata, ydata, 'o', label='Data')
        ax0.plot(xdata, results[i], label=labels[i])
        ax0.legend(loc='best')

    plt.show()

def plot(title, xdata, ydata=[], labels=[]):
    fig = plt.figure()
    fig.suptitle(title)
    gs = gridspec.GridSpec(len(ydata), len(ydata))

    for i in range(0, len(ydata)):
        ax0 = fig.add_subplot(gs[i, :])
        ax0.plot(xdata, ydata[i], label=labels[i])
        ax0.legend(loc='best')

    plt.show()
