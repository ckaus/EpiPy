# -*- coding: utf-8 -*-


class MainModel(object):
    """
    This class represents the main view model. It stores information about the *SideBarModel*.

    :returns: an instance of *MainModel*
    """

    def __init__(self):
        self.side_bar_model = None

    def __repr__(self):
        return "<%s.%s - side_bar_model=%s>" % \
               (__name__, self.__class__.__name__, self.side_bar_model)

    def __str__(self):
        return "%s\n" % self.side_bar_model
