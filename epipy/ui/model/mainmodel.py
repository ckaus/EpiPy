# -*- coding: utf-8 -*-


class MainModel(object):
    def __init__(self):
        self.x_data = None
        self.y_data = None
        self.fit_data = None
        self.population = None

    def set_data_set(self, x_data, y_data, population):
        self.x_data = x_data
        self.y_data = y_data
        self.population = population

    def __repr__(self):
        return '<object=%s - x_data=%s - y_data=%s - fit_data=%s - population=%s>' % (
            self.__class__.__name__, self.x_data, self.y_data, self.fit_data, self.population)

    def __str__(self):
        header = '# FIT DATA'
        return header + '\nFit X-Axis: %s\nFit Y-Axis: %s\nPopulation: %s' \
                        % (self.x_data, self.fit_data, self.population)
