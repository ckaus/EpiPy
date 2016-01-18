# -*- coding: utf-8 -*-


class OptionsModel(object):
    def __init__(self):
        self.epidemic_model = None
        self.advanced_dialog = None
        self.options_group_box = None
        self.spin_boxes = []
        self.parameters = []
        self.parameters_values = []

    def add_spin_box(self, spin_box):
        self.spin_boxes.append(spin_box)

    def __repr__(self):
        return '<object=%s - epidemic_model=%s - advanced_dialog=%s - options_group_box=%s  - spin_boxes=%s - \
        parameters=%s  - parameters_values=%s>' % (self.__class__.__name__, self.epidemic_model, self.advanced_dialog,
                                                   self.options_group_box, self.spin_boxes, self.parameters,
                                                   self.parameters_values)

    def __str__(self):
        header = '# PARAMETERS'
        return header + '\nEpidemic Model: %s\nParameters: %s\nParameters Values: %s>' \
                        % (self.epidemic_model, self.parameters, self.parameters_values)
