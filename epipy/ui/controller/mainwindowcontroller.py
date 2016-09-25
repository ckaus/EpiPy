# -*- coding: utf-8 -*-

from epipy.ui.view.mainwindow import MainWindow
from epipy.ui.view.aboutdialog import AboutDialog
from epipy.ui.view.plotwidget import PlotWidget
from epipy.ui.view.infogroupbox import InfoGroupBox
from epipy.ui.controller.sidebarcontroller import SideBarController


class MainWindowController(object):
    """This class represents the controller of *MainWindow*.

    :returns: an instance of *MainWindowController*
    """

    def __init__(self):
        self.view = MainWindow()
        self.side_bar_controller = SideBarController(self)
        self.view.h_splitter.insertWidget(1, self.side_bar_controller.view)

    def plot_data(self, x_data_1, y_data_1, x_data_2, y_data_2):
        """Sends plot data to *PlotWidget*.

        :param x_data_1: X-axis data for plot 1
        :type x_data_1: array_like
        :param y_data_1: Y-axis data for plot 1
        :type y_data_1: array_like
        :param x_data_2: X-axis data for plot 2
        :type x_data_2: array_like
        :param y_data_2: Y-axis data for plot 2
        :type y_data_2: array_like
        """
        self.view.plot_view.plot(x_data_1, y_data_1, x_data_2, y_data_2)

    def set_info_text(self, text):
        """Send output information to *InfoGroupBox*.

        :param text: the output information
        :type text: str
        """

        self.view.info_group_box.set_info(text)
