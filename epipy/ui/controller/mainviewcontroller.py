# -*- coding: utf-8 -*-


from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.model.mainmodel import MainModel


class MainViewController(BaseController):
    def __init__(self):
        BaseController.__init__(self)
        self.model = MainModel()

    def set_fit_result(self, result):
        self.model.fit_result = result

    def get_fit_result(self):
        return self.model.fit_result