# -*- coding: utf-8 -*-


class FitModel(object):
    def __init__(self):
        self.main_model = None
        self.options_model = None

    def __repr__(self):
        return '<object=%s - main_model=%s - options_model=%s>' % (
            self.__class__.__name__, self.main_model, self.options_model)

    def __str__(self):
        header = '==========RESULTS=========='
        return header + '\n%s\n%s' % (self.options_model, self.main_model)
