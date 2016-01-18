# -*- coding: utf-8 -*-

from epipy.ui.mainmodel import MainModel
from epipy.ui.optionscontroller import OptionsController
from epipy.utils import logger
import numpy as np

class MainViewController(object):
	def __init__(self, main_view):
		self.main_view = main_view
		self.main_model = MainModel()
		self.options_controller = OptionsController(self, self.main_view.options_group_box)
		
		data = self.get_data()
		self.main_model.set_data_set(*data)

		self.main_view.open_file_action.triggered.connect(self.open_file)
		self.main_view.save_action.triggered.connect(self.save)
		self.main_view.save_as_action.triggered.connect(self.save_as)
		self.main_view.export_action.triggered.connect(self.export)
		self.main_view.exit_action.triggered.connect(self.main_view.close)
		self.main_view.show_fullscreen_action.triggered.connect(self.show_fullscreen)
		self.main_view.exit_fullscreen_action.triggered.connect(self.exit_fullscreen)
		self.main_view.exit_fullscreen_action.setVisible(False)
		self.main_view.show_sidebar_action.triggered.connect(self.show_sidebar)
		self.main_view.hide_sidebar_action.triggered.connect(self.hide_sidebar)
		self.main_view.show_sidebar_action.setVisible(False)
		self.main_view.about_action.triggered.connect(self.show_about)

	def get_data(self):
		# ===================
        # Data 1
        # ======================
        # data_set_1 = csvmanager.read(file_name="data1.csv", seperator=";", column=["Time", "I"])
        # ydata_1 = np.array(data_set_1["I"], dtype=float)
        # xdata_1 = np.array(data_set_1["Time"], dtype=float)
        # result_1 = sir.Simple().fit(xdata=xdata_1, ydata=ydata_1, N=1)
		x_data = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140,
                            147, 154, 161], dtype=float)

		y_data = np.array([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200,
                            1700, 1170, 830, 750, 770, 520, 550, 380], dtype=float)
    
		data_set_2 = {'Time': x_data, 'I': y_data}
		y_data = np.array(data_set_2["I"], dtype=float)
		x_data = np.array(data_set_2["Time"], dtype=float)
		population = 10000
		return x_data, y_data, population
	
	def open_file(self):
		logger.info("open file")
		self.main_view.info_group_box.info_plain_text_edit.appendPlainText("open file")

	def save(self):
		logger.info("save")
		self.main_view.info_group_box.info_plain_text_edit.appendPlainText("save")

	def save_as(self):
		logger.info("save as")
		self.main_view.info_group_box.info_plain_text_edit.appendPlainText("save as")

	def export(self):
		logger.info("export")
		self.main_view.info_group_box.info_plain_text_edit.appendPlainText("export")

	def show_fullscreen(self):
		self.main_view.show_fullscreen_action.setVisible(False)
		self.main_view.exit_fullscreen_action.setVisible(True)
		self.main_view.showFullScreen()

	def exit_fullscreen(self):
		self.main_view.show_fullscreen_action.setVisible(True)
		self.main_view.exit_fullscreen_action.setVisible(False)
		self.main_view.showNormal()

	def show_sidebar(self):
		self.main_view.side_bar_widget.setVisible(True)
		self.main_view.show_sidebar_action.setVisible(False)
		self.main_view.hide_sidebar_action.setVisible(True)

	def hide_sidebar(self):
		self.main_view.side_bar_widget.setVisible(False)
		self.main_view.show_sidebar_action.setVisible(True)
		self.main_view.hide_sidebar_action.setVisible(False)

	def show_about(self):
		self.main_view.about_dialog.show()

	def update(self, **param):
		x_data = self.main_model.x_data
		y_data = self.main_model.y_data
		population = self.main_model.population
		epi_model = self.options_controller.options_model.epidemic_model
		fit_data = epi_model.fit(x_data, y_data, N=population, **param)
		self.main_model.fit_data = fit_data
		self.main_view.plot_1.setData(x=x_data, y=y_data)
		self.main_view.plot_2.setData(x=x_data, y=fit_data)

	def run(self):
		self.main_view.show()