# -*- coding: utf-8 -*-

from epipy.ui.model.inputmodel import InputModel
from epipy.ui.model.optionsmodel import OptionsModel


class SideBarModel(object):
    def __init__(self):
        self.options_model = OptionsModel()
        self.input_model = InputModel()

    def __repr__(self):
        return "<%s.%s - input_model=%s, options_model=%s>" % \
               (__name__, self.__class__.__name__, self.input_model, self.options_model)