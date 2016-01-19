from PyQt4 import QtCore, QtGui

from epipy.model import sir, seir, sirs
from epipy.ui.model.optionsmodel import OptionsModel
from epipy.ui.view.advanceddialog import SIRAdvancedDialog, SEIRAdvancedDialog, SIRSAdvancedDialog
from epipy.ui.view.optionsgroupbox import OptionsGroupBox
from epipy.ui.view.seirgroupbox import SEIRsimpleGroupBox
from epipy.ui.view.sirgroupbox import SIRsimpleGroupBox
from epipy.ui.view.sirsgroupbox import SIRSsimpleGroupBox


class OptionsController(object):
    def __init__(self, parent):
        self.options_view = OptionsGroupBox()
        self.parent = parent
        self.options_model = None
        self.options_view.advanced_btn.setEnabled(False)

        self.options_view.advanced_btn.clicked.connect(self.show_advanced_dialog)
        self.options_view.model_combo_box.currentIndexChanged['QString'].connect(
                self.init_model_param_group_box)
        self.parent.main_view.h_splitter.insertWidget(1, self.options_view)

    def init_model_param_group_box(self, selected_item):
        self.options_view.advanced_btn.setEnabled(True)
        if selected_item == QtCore.QString('SIR'):
            self.update(SIRAdvancedDialog(self),
                        SIRsimpleGroupBox(),
                        sir.Simple())

        elif selected_item == QtCore.QString('SEIR'):
            self.update(SEIRAdvancedDialog(self),
                        SEIRsimpleGroupBox(),
                        seir.Simple())

        elif selected_item == QtCore.QString('SIRS'):
            self.update(SIRSAdvancedDialog(self),
                        SIRSsimpleGroupBox(),
                        sirs.Simple())

    def update(self, advanced_dialog, options_group_box, epidemic_model):
        self.options_model = OptionsModel()
        self.options_model.options_group_box = options_group_box
        self.options_model.epidemic_model = epidemic_model
        self.options_model.advanced_dialog = advanced_dialog

        if self.options_view.layout().itemAt(2) is not None:
            self.options_view.layout().itemAt(2).widget().setParent(None)

        parameters_group_box = self.options_model.options_group_box
        self.options_view.layout().addRow(parameters_group_box)
        layout = self.options_model.options_group_box.layout()
        # add handler to spin boxes and imagine available labels
        for i in range(0, layout.count()):
            widget = layout.itemAt(i).widget()
            if (widget != 0) and (type(widget) is QtGui.QLabel):
                self.options_model.parameters.append((str(widget.text()).lower()))
            elif (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
                self.options_model.add_spin_box(widget)
                widget.valueChanged.connect(self.notify_main_window)

    def notify_main_window(self):
        self.options_model.parameters_values = []
        # prepare parameters based on labels and spin boxes
        values = []
        for spin_box in self.options_model.spin_boxes:
            value = spin_box.value()
            self.options_model.parameters_values.append(value)
            values.append(value)
        options_parameters = self.options_model.parameters
        # options_parameters = [str(item).lower() for item in options_parameters]
        param = dict(zip(options_parameters, values))
        self.parent.update(**param)

    def show_advanced_dialog(self):
        self.options_model.advanced_dialog.show()
