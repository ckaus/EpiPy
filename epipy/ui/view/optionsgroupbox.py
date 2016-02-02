# -*- coding: utf-8 -*-

import os
from PyQt4 import QtCore, uic

from epipy.ui.controller.event import Event
from epipy.ui.view.advanceddialog import SIRAdvancedDialog, SEIRAdvancedDialog, SIRSAdvancedDialog

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
OptionsGroupBoxUI, OptionsGroupBoxBase = uic.loadUiType(os.path.join(folder_path, "optionsgroupbox.ui"))


class OptionsGroupBox(OptionsGroupBoxBase, OptionsGroupBoxUI):
    """
    This class represents the options group box for a model.

    :param controller: the used controller
    :type controller: *SideBarViewController*

    :returns: an instance of *OptionsGroupBox*
    """
    def __init__(self, controller):
        OptionsGroupBoxBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)
        self.parameters_check_box.setEnabled(False)
        self.parameters_check_box.stateChanged.connect(self.controller.with_parameters)
        self.advanced_dialog = None
        self.advanced_btn.setEnabled(False)
        self.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.model_combo_box.setItemData(0, QtCore.QVariant(0), QtCore.Qt.UserRole - 1)
        self.model_combo_box.currentIndexChanged['QString'].connect(self.controller.set_model)
        self.setEnabled(False)

    def show_advanced_dialog(self):
        """
        This function shows the advanced dialog of a selected model.
        """
        model = self.controller.get_epidemic_model()
        if model == 'SIR':
            self.advanced_dialog = SIRAdvancedDialog(self.controller)
        elif model == 'SEIR':
            self.advanced_dialog = SEIRAdvancedDialog(self.controller)
        elif model == 'SIRS':
            self.advanced_dialog = SIRSAdvancedDialog(self.controller)
        self.advanced_dialog.show()

    def update(self, event):
        """
        This function updates the view with content and change availability of
        GUI components.

        :param event: an occurred event
        :type event: an *Event*
        """
        if event == Event.CHANGE_AVAILABILITY_OPTIONS:
            if self.isEnabled():
                self.setEnabled(False)
            else:
                self.setEnabled(True)
        elif event == Event.SELECT_NEW_MODEL:
            if not self.advanced_btn.isEnabled():
                self.advanced_btn.setEnabled(True)
            # remove model parameter group from view if exist
            if self.layout().itemAt(3):
                self.layout().itemAt(3).widget().deleteLater()
        elif event == Event.SELECT_NEW_MODEL_TYPE:
            self.parameters_check_box.setChecked(False)
            self.parameters_check_box.setEnabled(True)
            # add selected model parameter group box to view, depending on model type
            parameter_group_box = self.controller.get_current_model_parameter_group_box()
            # remove model parameter group box from view if exist
            possible_group_box = self.layout().itemAt(3)
            if possible_group_box:
                # something is on view at item(3) and
                if type(possible_group_box.widget()) != type(parameter_group_box):
                    # group box is not already on view
                    # user not selected the same model type group box
                    possible_group_box.widget().deleteLater()
                    self.layout().addWidget(parameter_group_box, 3, 0, 1, 3)
                    parameter_group_box.setEnabled(False)
            else:
                # nothing is on view at item(3)
                self.layout().addWidget(parameter_group_box, 3, 0, 1, 3)
                parameter_group_box.setEnabled(False)

        elif event == Event.SELECT_WITH_PARAMETERS:
            parameter_group_box = self.layout().itemAt(3).widget()
            if not self.parameters_check_box.isChecked():
                parameter_group_box.setEnabled(False)
            else:
                parameter_group_box.setEnabled(True)
