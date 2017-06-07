# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.uic import loadUi
from epipy.ui.view import cwd
from epipy.ui.view.aboutdialog import AboutDialog
from epipy.ui.view.infogroupbox import InfoGroupBox
from epipy.ui.view.plotwidget import PlotWidget


class MainWindow(QtGui.QMainWindow):
    """This class represents the main window.

    :returns: an instance of *MainWindow*
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(cwd + '/mainwindow.ui', self)

        # Menu
        self.about_dialog = AboutDialog()
        self.exit_action.triggered.connect(self.close)
        self.clear_information_action.triggered.connect(self.clear_information)
        self.show_fullscreen_action.triggered.connect(self.show_full_screen)
        self.exit_fullscreen_action.triggered.connect(self.exit_full_screen)
        self.exit_fullscreen_action.setVisible(False)
        self.show_sidebar_action.triggered.connect(self.show_sidebar)
        self.hide_sidebar_action.triggered.connect(self.hide_sidebar)
        self.show_sidebar_action.setVisible(False)
        self.about_action.triggered.connect(self.about_dialog.show)

        # Top Left
        self.plot_view = PlotWidget()
        self.h_splitter.insertWidget(0, self.plot_view)

        # Bottom
        self.info_group_box = InfoGroupBox()
        self.v_splitter.insertWidget(1, self.info_group_box)

    def clear_information(self):
        """Clears the information of *InfoGroupBox*"""
        self.info_group_box.info_plain_text_edit.clear()

    def exit_full_screen(self):
        """Stops full screen mode of *MainWindow*."""
        self.show_fullscreen_action.setVisible(True)
        self.exit_fullscreen_action.setVisible(False)
        self.showNormal()

    def hide_sidebar(self):
        """Hides the side bar view."""
        self.h_splitter.widget(1).setVisible(False)
        self.show_sidebar_action.setVisible(True)
        self.hide_sidebar_action.setVisible(False)

    def show_notification_information(self, text):
        """Shows a notification window *QMessageBox*.

        :param text: the showing text
        :type text: str
        """
        QtGui.QMessageBox.information(self, 'Information', text,
                                      QtGui.QMessageBox.Ok)

    def show_full_screen(self):
        """Executes the full screen mode of *MainWindow*."""
        self.show_fullscreen_action.setVisible(False)
        self.exit_fullscreen_action.setVisible(True)
        self.showFullScreen()

    def show_sidebar(self):
        """Shows the side bar view."""
        self.h_splitter.widget(1).setVisible(True)
        self.show_sidebar_action.setVisible(False)
        self.hide_sidebar_action.setVisible(True)
