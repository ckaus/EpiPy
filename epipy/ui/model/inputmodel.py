# -*- coding: utf-8 -*-


class InputModel(object):
    """
    This class represents the model of *InputGroupBox*.

    :returns: an instance of *InputModel*
    """

    def __init__(self):
        self.file_name = None
        self.file_content = None
        self.file_length = None
        self.data_range = None
        self.population = None
        self.data_percentage = None
        self.date_col_title = None
        self.data_col_title = None

    def __repr__(self):
        return "<%r.%r - " \
               "file_name=%r, " \
               "file_content=%r, " \
               "file_length=%r, " \
               "data_range=%r, " \
               "population=%r, " \
               "data_percentage=%r, " \
               "date_col_title=%r, " \
               "data_col_title=%r>" % (__name__, self.__class__,
                                       self.file_name,
                                       self.file_content,
                                       self.file_length,
                                       self.data_range,
                                       self.population,
                                       self.data_percentage,
                                       self.date_col_title,
                                       self.data_col_title)

    def __str__(self):
        return "File name: %s\n" \
               "Data range: %s\n" \
               "Population: %s\n" \
               "Percentage: %s" % (self.file_name,
                                   self.data_range,
                                   self.population,
                                   self.data_percentage)
