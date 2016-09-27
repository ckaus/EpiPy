# -*- coding: utf-8 -*-

import numpy as np
from epipy.lib.core.fit import fit
from epipy.ui.view import Notification
from epipy.utils import csvmanager, dateconverter
from epipy.ui.model.sidebarmodel import SideBarModel
from epipy.ui.view.sidebarwidget import SideBarWidget
from epipy.ui.view.advanceddialog import SIRAdvancedDialog,\
    SEIRAdvancedDialog, SIRSAdvancedDialog


class SideBarController(object):
    """This class represents the controller of *SideBarWidget*.

    :param: parent: the parent controller
    :type parent: *MainWIndowsController*

    :returns: an instance of *SideBarController*
    """

    def __init__(self, parent):
        self.parent = parent
        self.model = SideBarModel()
        self.view = SideBarWidget()
        self.advanced_dialog = None

        self.view.fit_btn.clicked.connect(self.fit)
        self.view.reset_btn.clicked.connect(self.reset)

        open_file_btn = self.view.input_group_box.open_file_btn
        open_file_btn.clicked.connect(self.open_file)
        advanced_btn = self.view.options_group_box.advanced_btn
        advanced_btn.clicked.connect(self.show_advanced_dialog)

    def open_file(self):
        """Shows an open file dialog and update the *InputGroupBox* with
        information from selected CSV file. Scanned data *InputModel*
        will be save in *InputModel*.
        """
        view = self.view.input_group_box
        model = self.model.input_model

        file_name = self.view.input_group_box.open_file()
        file_content = csvmanager.read(file_name)

        if not file_name:
            return  # no file was selected, do nothing

        if not file_content:
            self.view.options_group_box.warning(Notification.INVALID_DATA)

        model.file_name = file_name
        model.file_content = file_content
        model.file_length = len(file_content.values()[0])
        model.data_range = '0:%s' % model.file_length  # Default
        model.data_percentage = 100.00  # Default
        model.population = 1  # Default
        view.update(file_name=model.file_name,
                    date_cb_title=file_content.keys(),
                    data_cb_title=file_content.keys(),
                    data_range=model.data_range,
                    data_percentage=model.data_percentage,
                    population=model.population)

    def fit(self):
        """Starts the fitting process by collectoing information from
        *InputGroupBox* and *OptionsGroupBox*. Information will triggered
        to *epipylib.core.fit*.
        """
        if not self.update_input_model():
            return  # Do nothing
        if not self.update_options_model():
            return  # Do nothing
        im = self.model.input_model

        data_range = im.data_range.split(":")
        from_value = int(data_range[0])
        to_value = int(data_range[1])

        file_content = im.file_content
        try:
            # X-axis = time
            x_data = file_content[str(im.date_col_title)]
            # Y-axis = infected individual
            y_data = file_content[str(im.data_col_title)]
            y_data = np.array(y_data[from_value:to_value], dtype=float)
            try:
                x_data = np.array(x_data[from_value:to_value], dtype=float)
            except ValueError:  # Try to convert dates into a valid format
                x_data = dateconverter.convert(x_data)
                if len(x_data) == 0:  # Can not convert dates
                    self.view.input_group_box.show_notification(
                        Notification.INVALID_DATE_DATA)
                    return
                    # Convert dates
                x_data = x_data[from_value:to_value]
        except ValueError:
            return

        percentage = int(im.data_percentage)
        x_data = x_data[:len(x_data) * percentage / 100]
        y_data = y_data[:len(y_data) * percentage / 100]

        om = self.model.options_model
        epi_model = om.epidemic_model
        epi_model_param = om.epidemic_model_parameters.values()
        N0 = om.epidemic_model_class.init_model(N=im.population,
                                                y0=y_data[-1])
        if om.with_parameters:
            fitted_data, param, corr_coef = fit(model=epi_model,
                                                N0=N0,
                                                xdata=x_data,
                                                params=(epi_model_param))

        else:
            y_data_fit, param, corr_coef = fit(model=epi_model,
                                               xdata=x_data,
                                               ydata=y_data,
                                               N0=N0,
                                               iter=10)
        om.epidemic_model_parameters = param

        self.parent.set_info_text(str(self.model))
        self.parent.plot_data(x_data, y_data,
                              x_data, y_data_fit)

    def reset(self):
        """Resets *SideBarWidget* and create new *SideBarModel*."""
        self.view.clear()
        self.model = SideBarModel()

    def set_options_model(self):
        """Sets selected epidemic model information from *AdvancedDialog*."""
        param_group_box, epidemic_model_class, epidemic_model =\
            self.advanced_dialog.get_selected_model()
        self.view.options_group_box.add_parameter_group_box(param_group_box)
        self.model.options_model.epidemic_model = epidemic_model
        self.model.options_model.epidemic_model_class = epidemic_model_class

    def show_advanced_dialog(self):
        """Shows the *AdvancedDialog* based on selected epidemic model from
        *OptionsGroupBox*.
        """
        model = self.view.options_group_box.model_combo_box.currentText()
        if model == 'SIR':
            self.advanced_dialog = SIRAdvancedDialog()
        elif model == 'SEIR':
            self.advanced_dialog = SEIRAdvancedDialog()
        elif model == 'SIRS':
            self.advanced_dialog = SIRSAdvancedDialog()
        if self.advanced_dialog:
            self.advanced_dialog.show()
            self.advanced_dialog.button_box.accepted.connect(
                self.set_options_model)
        else:
            self.view.options_group_box.warning(Notification.NO_MODEL)

    def update_input_model(self):
        """Updates the *InputModel* with information from *InputGroupBox*.

        :returns: success of update
        :rtype: True/False
        """
        view = self.view.input_group_box
        model = self.model.input_model

        if not model.file_content:
            view.show_notification(Notification.NO_FILE)
            return False

        model.data_percentage = view.get_data_percentage()

        date_col_title = view.get_selected_date_cb_text()
        data_col_title = view.get_selected_data_cb_text()
        if date_col_title == data_col_title:
            view.show_notification(Notification.SAME_DATE_DATA)
            return False
        model.date_col_title = date_col_title
        model.data_col_title = data_col_title

        data_range = str(view.get_data_range())
        if not data_range or data_range.startswith(':'):
            view.show_notification(NO_DATA_RANGE)
            return False
        from_value = int(data_range.split(":")[0])
        to_value = int(data_range.split(":")[1])
        if to_value < from_value or to_value > model.file_length:
            view.show_notification(Notification.INVALID_DATA_RANGE)
            return False
        model.data_range = data_range

        population = view.get_population()
        if not population:
            view.show_notification(Notification.NO_POPULATION)
            return False
        model.population = population
        return True

    def update_options_model(self):
        """Update the *OptionsModel* with information from
        *OptionsGroupBox*.

        :returns: success of update
        :rtype: True/False
        """
        view = self.view.options_group_box
        model = self.model.options_model
        parameters = view.get_model_parameters()
        if not parameters:
            view.show_notification(Notification.NO_MODEL)
            return False
        model.epidemic_model_parameters = parameters
        model.with_parameters = view.parameters_check_box.isChecked()
        return True
