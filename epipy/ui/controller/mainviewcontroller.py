# -*- coding: utf-8 -*-

import numpy as np

from epipy.ui.model.mainmodel import Event
from epipy.ui.model.mainmodel import MainModel


class MainViewController(object):
    def __init__(self):
        self.main_model = MainModel()
        self.views = []

    def set_model(self, model):
        self.main_model.model = model
        self.notify(Event.ENABLE_ADVANCED_BUTTON)

    def get_model(self):
        return self.main_model.model

    def set_model_group_box(self, model_group_box, model_class):
        self.main_model.model_group_box = model_group_box
        self.main_model.model_class = model_class
        self.notify(Event.SHOW_MODEL_PARAMETER_GROUP_BOX)

    def set_model_parameters(self, parameters):
        self.main_model.model_parameters = parameters

    def get_model_parameter_group_box(self):
        return self.main_model.model_group_box

    def fit_data(self):
        self.notify(Event.FIT_DATA)
        # ==========================
        # Data 1
        # ==========================
        x_data = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140,
                           147, 154, 161], dtype=float)

        y_data = np.array([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200,
                           1700, 1170, 830, 750, 770, 520, 550, 380], dtype=float)

        data_set_2 = {'Time': x_data, 'I': y_data}
        y_data = np.array(data_set_2["I"], dtype=float)
        x_data = np.array(data_set_2["Time"], dtype=float)
        population = 10000

        model_class = self.main_model.model_class
        params = self.main_model.model_parameters
        fitted_data = model_class.fit(x_data, y_data, N=population, **params)
        self.main_model.fitted_data = {'x': x_data, 'y': y_data}, {'x': x_data, 'y': fitted_data}
        # fitted_data contains regresionline, and so on ...
        self.main_model.plot_data = {'x': x_data, 'y': y_data}, {'x': x_data, 'y': fitted_data[0]}
        self.notify(Event.PLOT)

    def get_fitted_data(self):
        return self.main_model.fitted_data

    def get_plot_data(self):
        return self.main_model.plot_data

    def reset_data(self):
        pass

    def attach(self, views):
        if views not in self.views:
            self.views.append(views)

    def detach(self, view):
        try:
            self.views.remove(view)
        except ValueError as error:
            print 'View not attached %s' % error

    def notify(self, event):
        for view in self.views:
            view.update(event)
