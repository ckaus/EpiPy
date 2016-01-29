# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

from epipy.ui.controller.event import Event
from epipy.ui.controller.sidebarviewcontroller import SideBarController
from epipy.ui.view.aboutdialog import AboutDialog
from epipy.ui.view.infogroupbox import InfoGroupBox
from epipy.ui.view.plotview import PlotView
from epipy.ui.view.sidebarwidget import SideBarWidget

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
MainWindowUI, MainWindowBase = uic.loadUiType(os.path.join(folder_path, "mainwindow.ui"))


class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self, controller):
        MainWindowBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)
        self.controller_service = self.controller.get_controller_service()

        # Menu
        self.about_dialog = AboutDialog()
        self.open_file_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save)
        self.save_as_action.triggered.connect(self.save_as)
        self.export_action.triggered.connect(self.export)
        self.exit_action.triggered.connect(self.close)
        self.show_fullscreen_action.triggered.connect(self.show_fullscreen)
        self.exit_fullscreen_action.triggered.connect(self.exit_fullscreen)
        self.exit_fullscreen_action.setVisible(False)
        self.show_sidebar_action.triggered.connect(self.show_sidebar)
        self.hide_sidebar_action.triggered.connect(self.hide_sidebar)
        self.show_sidebar_action.setVisible(False)
        self.clear_information_action.triggered.connect(self.controller.clear_information)
        self.about_action.triggered.connect(self.about_dialog.show)

        # Top Left
        self.plot_view = PlotView(self)
        self.h_splitter.insertWidget(0, self.plot_view)

        # Top Right
        self.side_bar_controller = SideBarController(self.controller_service)
        self.side_bar = SideBarWidget(self.side_bar_controller)
        self.h_splitter.insertWidget(1, self.side_bar)

        # Bottom
        self.info_group_box = InfoGroupBox(self.controller)
        self.v_splitter.insertWidget(1, self.info_group_box)

    def open_file(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    def export(self):
        pass

    def show_fullscreen(self):
        self.show_fullscreen_action.setVisible(False)
        self.exit_fullscreen_action.setVisible(True)
        self.showFullScreen()

    def exit_fullscreen(self):
        self.show_fullscreen_action.setVisible(True)
        self.exit_fullscreen_action.setVisible(False)
        self.showNormal()

    def show_sidebar(self):
        self.h_splitter.widget(1).setVisible(True)
        self.show_sidebar_action.setVisible(False)
        self.hide_sidebar_action.setVisible(True)

    def hide_sidebar(self):
        self.h_splitter.widget(1).setVisible(False)
        self.show_sidebar_action.setVisible(True)
        self.hide_sidebar_action.setVisible(False)

    def update(self, event):
        if event == Event.PLOT:
            file_data, fitted_data = self.side_bar_controller.get_plot_data()
            x_data = file_data.get('x')
            y_data = file_data.get('y')
            y_fitted = fitted_data.get('y_fitted')
            self.plot_view.plot(x_data, y_data, y_fitted)
            self.controller.set_side_bar_model(self.side_bar_controller.get_model())
