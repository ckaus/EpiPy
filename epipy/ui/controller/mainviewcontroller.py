# -*- coding: utf-8 -*-


from epipy.ui.controller.basecontroller import BaseController
from epipy.ui.controller.event import Event
from epipy.ui.model.mainmodel import MainModel


class MainViewController(BaseController):
    def __init__(self, controller_service):
        BaseController.__init__(self)
        self.model = MainModel()
        self.controller_service = controller_service
        self.controller_service.add_target(self)

    def get_model(self):
        return self.model

    def get_controller_service(self):
        return self.controller_service

    def set_side_bar_model(self, model):
        self.model.side_bar_model = model
        self.notify(Event.LOG)
