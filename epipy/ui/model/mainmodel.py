# -*- coding: utf-8 -*-


class Event(object):
    ENABLE_MODEL_PARAMETER_GROUP_BOX = 1
    ENABLE_FIT_BUTTON = 2
    DISABLE_MODEL_PARAMETER_GROUP_BOX = 3
    DISABLE_FIT_BUTTON = 4
    ENABLE_ADVANCED_BUTTON = 5
    SHOW_MODEL_PARAMETER_GROUP_BOX = 6
    FIT_DATA = 7
    PLOT = 8


class MainModel(object):
    def __init__(self):
        self.views = []
        self.model = None
        self.model_group_box = None
        self.model_parameters = None
        self.model_class = None
        self.fitted_data = None
        self.plot_data = None

    def __str__(self):
        return "model=%s model_group_box=%s model_class=%s model_parameters=%s fitted_data=%s" % (
            self.model, self.model_group_box, self.model_class, self.model_parameters, self.fitted_data)
