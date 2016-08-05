# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore, uic

from epipy.ui.controller.event import Event
from epipy.ui.view.advanceddialog import SIRAdvancedDialog, SEIRAdvancedDialog, SIRSAdvancedDialog

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
OptionsGroupBoxUI, OptionsGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "optionsgroupbox.ui"))


class OptionsGroupBox(OptionsGroupBoxBase, OptionsGroupBoxUI):
    """
    This class represents the options group box for a model.

    :param controller: the used controller
    :type controller: *SideBarController*

    :returns: an instance of *OptionsGroupBox*
    """

    def __init__(self, controller):
        OptionsGroupBoxBase.__init__(self)
        self.setupUi(self)

        self.controller = controller
        self.controller.attach(self)

        self.parameters_check_box.stateChanged.connect(self.switch_availability_parameter_group_box)
        self.advanced_dialog = None
        self.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)

    def switch_availability_parameter_group_box(self, state):
        if self.layout().itemAt(3):
            self.layout().itemAt(3).widget().setEnabled(state)
        self.controller.set_with_parameters(self.parameters_check_box.isChecked())

    def show_advanced_dialog(self):
        """
        This function shows the advanced dialog of a selected model.
        """
        curr_idx = self.model_combo_box.currentIndex()
        model = self.model_combo_box.itemText(curr_idx)

        if model == 'SIR':
            self.advanced_dialog = SIRAdvancedDialog(self.controller)
        elif model == 'SEIR':
            self.advanced_dialog = SEIRAdvancedDialog(self.controller)
        elif model == 'SIRS':
            self.advanced_dialog = SIRSAdvancedDialog(self.controller)
        else:
            QtGui.QMessageBox.warning(self, 'Warning',
                                      model,
                                      QtGui.QMessageBox.Ok)
            return
        self.advanced_dialog.show()

    def remove_parameter_group_box(self):
        if self.layout().itemAt(3):
            # something is on view at item(3)
            # remove group box from view
            self.layout().itemAt(3).widget().deleteLater()

    def update(self, event):
        """
        This function updates the view with content and change availability of
        GUI components.

        :param event: an occurred event
        :type event: an *Event*
        """
        if event == Event.SUCCESS_SELECT_OPTIONS:
            # add selected model parameter group box to view, depending on model type
            parameter_group_box = self.controller.get_current_parameter_group_box()
            self.remove_parameter_group_box()
            self.layout().addWidget(parameter_group_box, 3, 0, 1, 3)
            parameter_group_box.setEnabled(self.parameters_check_box.isChecked())
        elif event == Event.RESET:
            self.remove_parameter_group_box()
            self.model_combo_box.setCurrentIndex(0)
            self.parameters_check_box.setCheckState(0)
