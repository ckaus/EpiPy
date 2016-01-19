from PyQt4 import QtGui

from epipy.ui.view.infogroupbox import InfoGroupBox


class InfoController(object):
    def __init__(self, parent):
        self.parent = parent
        self.info_view = InfoGroupBox()
        self.info_view.clear_btn.clicked.connect(self.clear_fitting_info)
        self.parent.main_view.v_splitter.addWidget(self.info_view)

    def clear_fitting_info(self):
        if self.info_view.info_plain_text_edit.toPlainText():
            reply = QtGui.QMessageBox.question(self.info_view, 'Message',
                                               "Are you sure to clear the fitting information?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.info_view.info_plain_text_edit.clear()

    def update_file_name(self, file_name):
        self.info_view.file_name = file_name

    def update_information(self, text):
        self.info_view.info_plain_text_edit.appendPlainText("%s" % text)
