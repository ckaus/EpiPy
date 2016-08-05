# -*- coding: utf-8 -*-


class InputModel(object):
    """
    This class represents an input model. It stores input file information.

    :returns: an instance of *InputModel*
    """

    def __init__(self):
        self.file_name = ''
        self.file_content = None
        self.data_range = None
        self.population = None
        self.data_input_length = None
        self.data_percentage = None
        self.date_col_title = None
        self.data_col_title = None

    def set_data_col_title(self, data_col_title):
        self.data_col_title = data_col_title

    def set_date_col_title(self, date_col_title):
        self.date_col_title = date_col_title

    def set_data_range(self, data_range):
        self.data_range = data_range

    def set_population(self, population):
        self.population = population

    def set_data_percentage(self, data_percentage):
        self.data_percentage = data_percentage

    def __repr__(self):
        return "<%r.%r - " \
               "file_name=%r, " \
               "file_content=%r, " \
               "data_range=%r, " \
               "population=%r, " \
               "data_input_length=%r, " \
               "data_percentage=%r, " \
               "date_col=%r, " \
               "data_col=%r>" % (__name__,
                                 self.__class__,
                                 self.file_name,
                                 self.file_content,
                                 self.data_range,
                                 self.population,
                                 self.data_input_length,
                                 self.data_percentage,
                                 self.date_col_title,
                                 self.data_col_title)

    def __str__(self):
        return "File name: %s\n" \
               "Data range: %s\n" \
               "Population: %s\n" \
               "Used file data length: %s\n" \
               "Used percentage: %s" % (self.file_name,
                                        self.data_range,
                                        self.population,
                                        self.data_input_length,
                                        self.data_percentage)
