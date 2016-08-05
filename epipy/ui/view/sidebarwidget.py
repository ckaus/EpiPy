import os
from PyQt4 import uic, QtGui

from epipy.ui.controller.event import Event
from epipy.ui.view.inputgroupbox import InputGroupBox
from epipy.ui.view.optionsgroupbox import OptionsGroupBox

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
SideBarWidgetUI, SideBarWidgetBase = uic.loadUiType(os.path.join(folder_path, "sidebarwidget.ui"))


class SideBarWidget(SideBarWidgetBase, SideBarWidgetUI):
    """
    This class represents the side bar widget.

    :param controller: the used controller
    :type controller: *SideBarController*

    :returns: an instance of *SideBarWidget*
    """

    def __init__(self, controller):
        SideBarWidgetBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)

        # Top
        self.input_group_box = InputGroupBox(self.controller)
        self.layout().addWidget(self.input_group_box)

        # Center
        self.options_group_box = OptionsGroupBox(controller)
        self.layout().addWidget(self.options_group_box)
        self.spacer = QtGui.QSpacerItem(0, 0, 0, QtGui.QSizePolicy.Expanding)
        self.layout().addItem(self.spacer)

        # Bottom
        self.side_bar_bottom_widget = QtGui.QWidget(self)
        self.side_bar_bottom_layout = QtGui.QHBoxLayout(self.side_bar_bottom_widget)
        self.fit_btn = QtGui.QPushButton('Fit')
        self.fit_btn.clicked.connect(controller.fit_data)
        self.fit_btn.setEnabled(False)
        self.side_bar_bottom_layout.addWidget(self.fit_btn)
        self.reset_btn = QtGui.QPushButton('Reset')
        self.reset_btn.clicked.connect(controller.reset_data)
        self.side_bar_bottom_layout.addWidget(self.reset_btn)
        # self.reset_btn.clicked.connect(self.controller.reset_data)
        self.layout().addWidget(self.side_bar_bottom_widget)

    def update(self, event):
        """
        This function change the availability of GUI components.

        :param event: an occurred event
        :type event: an *Event*
        """
        if event == Event.ENABLE_FIT_BUTTON:
            self.fit_btn.setEnabled(True)
        elif event == Event.RESET:
            self.fit_btn.setEnabled(False)
        elif event == Event.SHOW_RUNTIME_ERROR:
            QtGui.QMessageBox.critical(self,
                                       'Runtime Error', "Fitting process raises an Error.",
                                       QtGui.QMessageBox.Ok)
