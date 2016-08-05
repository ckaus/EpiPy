# -*- coding: utf-8 -*-


class OptionsModel(object):
    """
    This class represents the option group box model. It stores information about the *SideBarWidget*.

    :returns: an instance of *OptionsModel*
    """

    def __init__(self):
        self.epidemic_model = None
        self.epidemic_model_class = None
        self.epidemic_model_parameters = None
        self.with_parameters = None

    def __repr__(self):
        return "<%r.%r - " \
               "epidemic_model=%r, " \
               "epidemic_model_class=%r, " \
               "epidemic_model_parameters=%r, " \
               "with_parameters=%r>" % (__name__,
                                        self.__class__.__name__,
                                        self.epidemic_model,
                                        self.epidemic_model_class,
                                        self.epidemic_model_parameters,
                                        self.with_parameters)

    def __str__(self):
        return "Model: %s - %s\n" \
               "Model Parameters: %s" % (self.epidemic_model_class.__name__,
                                         self.epidemic_model.__name__,
                                         self.epidemic_model_parameters)
