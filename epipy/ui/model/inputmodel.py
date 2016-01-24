# -*- coding: utf-8 -*-


class InputModel(object):
    def __init__(self):
        self.file_name = ''
        self.file_content = None
        self.population = None

    def __repr__(self):
        return "<%s.%s - file_name=%s - file_content=%s - population=%s>" % (
            __name__, self.__class__.__name__, self.file_name, self.file_content, self.population)

    def __str__(self):
        return "File Name: %s" % self.file_name
