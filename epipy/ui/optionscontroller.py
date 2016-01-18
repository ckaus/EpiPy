from epipy.ui.optionsmodel import OptionsModel
from epipy.model import sir, seir, sirs
from epipy.ui.advanceddialog import SIRAdvancedDialog, SEIRAdvancedDialog, SIRSAdvancedDialog
from epipy.ui.seirgroupbox import SEIRsimpleGroupBox
from epipy.ui.sirgroupbox import SIRsimpleGroupBox
from epipy.ui.sirsgroupbox import SIRSsimpleGroupBox
from PyQt4 import QtCore, QtGui

class OptionsController(object):

	def __init__(self, main_view_controller, options_view):
		self.options_view = options_view
		self.main_view_controller = main_view_controller
		self.options_model = None

		self.options_view.advanced_btn.clicked.connect(self.show_advanced_dialog)
		self.options_view.model_combo_box.currentIndexChanged['QString'].connect(
        	self.init_model_param_group_box)

	def init_model_param_group_box(self, selected_item):
		options_model = OptionsModel()
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
		self.options_model.set_options_group_box(options_group_box)
		self.options_model.set_epidemic_model(epidemic_model)
		self.options_model.set_advanced_dialog(advanced_dialog)

		if self.options_view.layout().itemAt(2) is not None:
			self.options_view.layout().itemAt(2).widget().setParent(None)
			
		parameters_group_box = self.options_model.options_group_box		
		self.options_view.layout().addRow(parameters_group_box)
		layout = self.options_model.options_group_box.layout()
		# add handler to spin boxes and imagine available labels
		for i in range(0, layout.count()):
			widget = layout.itemAt(i).widget()
			if (widget != 0) and (type(widget) is QtGui.QLabel):
				self.options_model.add_parameter(widget.text())
			elif (widget != 0) and (type(widget) is QtGui.QDoubleSpinBox):
				self.options_model.add_spin_box(widget)
				widget.valueChanged.connect(self.notify_main_window)

	def notify_main_window(self):
		# prepare parameters based on labels and spin boxes
		values = []
		for spin_box in self.options_model.spin_boxes:
			values.append(spin_box.value())
		available_parameters = self.options_model.parameters
		available_parameters = [str(item).lower() for item in available_parameters]
		param = dict(zip(available_parameters, values))
		self.main_view_controller.update(**param)

	def show_advanced_dialog(self):
		self.options_model.advanced_dialog.show()