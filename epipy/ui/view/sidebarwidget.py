import os
from PyQt4 import uic, QtGui

from epipy.ui.controller.sidebarcontroller import Event
from epipy.ui.view.optionsgroupbox import OptionsGroupBox
from epipy.ui.view.inputgroupbox import InputGroupBox


dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
SideBarWidgetUI, SideBarWidgetBase = uic.loadUiType(os.path.join(folder_path, "sidebarwidget.ui"))


class SideBarWidget(SideBarWidgetBase, SideBarWidgetUI):
    def __init__(self, controller):
        SideBarWidgetBase.__init__(self)
        self.setupUi(self)

        self.controller = controller
        self.controller.attach(self)

        # Top
        self.input_group_box = InputGroupBox(self.controller)
        self.layout().addWidget(self.input_group_box)

        # Center
        self.options_group_box = OptionsGroupBox(self.controller)
        self.layout().addWidget(self.options_group_box)
        self.spacer = QtGui.QSpacerItem(0, 0, 0, QtGui.QSizePolicy.Expanding)
        self.layout().addItem(self.spacer)

        # Bottom
        self.side_bar_bottom_widget = QtGui.QWidget(self)
        self.side_bar_bottom_layout = QtGui.QHBoxLayout(self.side_bar_bottom_widget)
        self.fit_btn = QtGui.QPushButton('Fit')
        self.fit_btn.clicked.connect(self.controller.fit_data)
        self.fit_btn.setEnabled(False)
        self.side_bar_bottom_layout.addWidget(self.fit_btn)
        self.reset_btn = QtGui.QPushButton('Reset')
        # connect RESET Button
        self.side_bar_bottom_layout.addWidget(self.reset_btn)
        self.reset_btn.clicked.connect(self.controller.reset_data)
        self.layout().addWidget(self.side_bar_bottom_widget)

    def update(self, event):
        if event == Event.ENABLE_FIT_BUTTON:
            self.fit_btn.setEnabled(True)
        elif event == Event.DISABLE_FIT_BUTTON and self.fit_btn.isEnabled():
            self.fit_btn.setEnabled(False)
