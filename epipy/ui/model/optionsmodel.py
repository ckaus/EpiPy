# -*- coding: utf-8 -*-


class OptionsModel(object):
    def __init__(self):
        self.epidemic_model = None
        self.epidemic_model_class = None
        self.epidemic_model_parameters = []

    def __repr__(self):
        return "<%s.%s - epidemic_model=%s, epidemic_model_class=%s, epidemic_model_parameters=%s>" % \
               (__name__, self.__class__.__name__, self.epidemic_model, self.epidemic_model_class,
                self.epidemic_model_parameters)

    def __str__(self):
        return "Model: %s\n Model Parameters: %s" % (self.epidemic_model_class, self.epidemic_model_parameters)
