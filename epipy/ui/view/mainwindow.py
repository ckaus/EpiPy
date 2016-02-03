# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

from epipy.ui.controller.event import Event
from epipy.ui.controller.sidebarcontroller import SideBarController
from epipy.ui.view.aboutdialog import AboutDialog
from epipy.ui.view.helpwidget import HelpWidget
from epipy.ui.view.infogroupbox import InfoGroupBox
from epipy.ui.view.plotwidget import PlotWidget
from epipy.ui.view.sidebarwidget import SideBarWidget

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
MainWindowUI, MainWindowBase = uic.loadUiType(os.path.join(folder_path, "mainwindow.ui"))


class MainWindow(MainWindowBase, MainWindowUI):
    """
    This class represents the main window.

    :param controller: the used controller
    :type controller: *MainWindowController*

    :returns: an instance of *MainWindow*
    """

    def __init__(self, controller):
        MainWindowBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)
        self.controller_service = self.controller.get_controller_service()

        # Menu
        self.about_dialog = AboutDialog()
        self.help_view = HelpWidget()
        self.exit_action.triggered.connect(self.close)
        self.show_fullscreen_action.triggered.connect(self.show_full_screen)
        self.exit_fullscreen_action.triggered.connect(self.exit_full_screen)
        self.exit_fullscreen_action.setVisible(False)
        self.show_sidebar_action.triggered.connect(self.show_sidebar)
        self.hide_sidebar_action.triggered.connect(self.hide_sidebar)
        self.show_sidebar_action.setVisible(False)
        self.clear_information_action.triggered.connect(self.controller.clear_information)
        self.help_action.triggered.connect(self.help_view.show)
        self.about_action.triggered.connect(self.about_dialog.show)

        # Top Left
        self.plot_view = PlotWidget(self)
        self.h_splitter.insertWidget(0, self.plot_view)

        # Top Right
        self.side_bar_controller = SideBarController(self.controller_service)
        self.side_bar = SideBarWidget(self.side_bar_controller)
        self.h_splitter.insertWidget(1, self.side_bar)

        # Bottom
        self.info_group_box = InfoGroupBox(self.controller)
        self.v_splitter.insertWidget(1, self.info_group_box)

    def show_full_screen(self):
        """
        This function enable the full screen mode of this view.
        """
        self.show_fullscreen_action.setVisible(False)
        self.exit_fullscreen_action.setVisible(True)
        self.showFullScreen()

    def exit_full_screen(self):
        """
        This function disable the full screen mode of this view.
        """
        self.show_fullscreen_action.setVisible(True)
        self.exit_fullscreen_action.setVisible(False)
        self.showNormal()

    def show_sidebar(self):
        """
        This function shows the side bar view.
        """
        self.h_splitter.widget(1).setVisible(True)
        self.show_sidebar_action.setVisible(False)
        self.hide_sidebar_action.setVisible(True)

    def hide_sidebar(self):
        """
        This function hides the side bar view.
        """
        self.h_splitter.widget(1).setVisible(False)
        self.show_sidebar_action.setVisible(True)
        self.hide_sidebar_action.setVisible(False)

    def update(self, event):
        """
        This function updates the view updates the plotted graph.

        :param event: an occurred event
        :type event: an *Event*
        """
        if event == Event.PLOT:
            file_data, fitted_data, forecast_data = self.side_bar_controller.get_plot_data()
            self.plot_view.plot(file_data, fitted_data, forecast_data)
            self.controller.set_side_bar_model(self.side_bar_controller.get_model())
