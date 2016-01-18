class OptionsModel(object):
	def __init__(self):
		self.epidemic_model = None
		self.advanced_dialog = None
		self.options_group_box = None
		self.spin_boxes = []
		self.parameters = []

	def add_parameter(self, parameter):
		self.parameters.append(parameter)

	def add_spin_box(self, spin_box):
		self.spin_boxes.append(spin_box)

	def set_epidemic_model(self, epidemic_model):
		self.epidemic_model = epidemic_model

	def set_advanced_dialog(self, advanced_dialog):
		self.advanced_dialog = advanced_dialog

	def set_options_group_box(self, options_group_box):
		self.options_group_box = options_group_box