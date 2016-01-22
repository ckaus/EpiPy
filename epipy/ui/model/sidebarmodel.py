# -*- coding: utf-8 -*-


class SideBarModel(object):
    def __init__(self):
        self.model = None
        self.epidemic_model_parameters = None
        self.epidemic_model_class = None
        self.fitted_data = None

    def __str__(self):
        return "model=%s, epidemic_model_parameters=%s, epidemic_model class=%s, fitted_data=%s" % (
        self.model, self.epidemic_model_parameters, self.epidemic_model_class, self.fitted_data)
