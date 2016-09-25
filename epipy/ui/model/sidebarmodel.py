# -*- coding: utf-8 -*-

from epipy.ui.model.inputmodel import InputModel
from epipy.ui.model.optionsmodel import OptionsModel


class SideBarModel(object):
    """
    This class represents the model of *SideBarWidget*.

    :returns: an instance of *SideBarModel*
    """

    def __init__(self):
        self.input_model = InputModel()
        self.options_model = OptionsModel()

    def __repr__(self):
        return "<%r.%r - " \
               "input_model=%r," \
               "options_model=%r>" % (__name__,
                                      self.__class__.__name__,
                                      self.input_model.__repr__,
                                      self.options_model.__repr__)

    def __str__(self):
        return "Input settings\n%s" \
               "\nOption settings\n%s" % (self.input_model,
                                          self.options_model)
