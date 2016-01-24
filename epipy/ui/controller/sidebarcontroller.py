# -*- coding: utf-8 -*-

import numpy as np

from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.model.sidebarmodel import SideBarModel
from epipy.ui.controller.event import Event
from pyqtgraph import QtGui
from epipy.utils import csvmanager

class SideBarController(BaseController):
    def __init__(self, controller_service):
        BaseController.__init__(self)
        self.model = SideBarModel()

        self.controller_service = controller_service
        self.current_model_group_box = None

    def set_model(self, model):
        self.model.options_model.epidemic_model = model
        self.notify(Event.ENABLE_ADVANCED_BUTTON)

    def get_epidemic_model(self):
        return self.model.options_model.epidemic_model

    def set_model_group_box(self, model_group_box, model_class):
        self.current_model_group_box = model_group_box
        self.model.options_model.epidemic_model_class = model_class
        self.notify(Event.SHOW_MODEL_PARAMETER_GROUP_BOX)
        self.notify(Event.ENABLE_FIT_BUTTON)

    def get_model_parameter_group_box(self):
        return self.current_model_group_box

    def get_model_parameters(self):
        parameters = []
        parameter_values = []
        group_box = self.current_model_group_box
        for i in range(0, group_box.layout().count()):
            widget = group_box.layout().itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QLabel):
                parameters.append((str(widget.text()).lower()))
            elif (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                parameter_values.append(widget.value())
        return dict(zip(parameters, parameter_values))

    def get_model(self):
        return self.model

    def fit_data(self):
        param = self.get_model_parameters()
        self.model.options_model.epidemic_model_parameters = param

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

        model_class = self.model.options_model.epidemic_model_class
        fitted_data = model_class.fit(x_data, y_data, N=population, **param)
        self.model.plot_model.x_data = x_data
        self.model.plot_model.y_data = y_data
        self.model.plot_model.y_fitted_data = fitted_data[0]
        self.controller_service.redirect(Event.PLOT)

    def get_plot_data(self):
        return self.model.plot_model.get_data()

    def set_input_file(self, file_name):
        self.model.input_model.file_name = file_name
        print csvmanager.read(file_name, "")
        # self.notify(Event.READ_FILE)

    def get_input_file(self):
        return self.model.input_model.file_name

    def reset_data(self):
        pass
