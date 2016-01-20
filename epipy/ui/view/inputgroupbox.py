# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

from epipy.ui.model.mainmodel import Event

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
InputGroupBoxUI, InputGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "inputgroupbox.ui"))


class InputGroupBox(InputGroupBoxBase, InputGroupBoxUI):
    def __init__(self, controller):
        InputGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)

        # if file was completly loaded -> notify controller to display options group box
        # Example of delegate an event to controller:
        # Flow: format_check box is checked? -> display options_group_box
        self.format_check_box.stateChanged.connect(self.format_check_box_state_changed)

    # Only for testing events
    def format_check_box_state_changed(self, value):
        if value:
            self.controller.notify(Event.ENABLE_MODEL_PARAMETER_GROUP_BOX)
        else:
            self.controller.notify(Event.DISABLE_MODEL_PARAMETER_GROUP_BOX)

    def update(self, event):
        pass
