# -*- coding: utf-8 -*-


class InfoModel(object):
    def __init__(self):
        self.text = ''

    def get_text(self):
        return self.text

    def __repr__(self):
        return "<%r.%r - " \
               "text=%r>" % (__name__,
                             self.__class__,
                             self.text)

    def __str__(self):
        return "%s" % self.text
