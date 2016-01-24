# -*- coding: utf-8 -*-


class InputModel(object):
    def __init__(self):
        self.file_name = ''

    def __repr__(self):
        return "<%s.%s - file_name=%s>" % (__name__, self.__class__.__name__, self.file_name)

    def __str__(self):
        return "File Name: %s" % self.file_name
