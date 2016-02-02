# -*- coding: utf-8 -*-

from scipy import integrate

from basemodel import BaseModel


class SIR(BaseModel):
    """
    This class represents an abstract model for SIR Models.
    """

    def __init__(self):
        BaseModel.__init__(self)
        self.__name__ = 'SIR'

    def init_param(self, y0):
        """
        This function initialize the model parameters.

        :param y0: infected value in t0.
        :type y0: int or float
        :return: tuple of model values in t0
        """
        I0 = y0
        S0 = self.N - I0
        R0 = 0.0
        return S0, I0, R0


class Simple(SIR):
    """
    This class represents the Simple SIR Model.
    """

    def __init__(self):
        SIR.__init__(self)

    def model(self, y, x, beta, gamma):
        """
        This function defines the Simple SIR Model.

        :param y: y value, where y-axis represents the individuals.
        :type y: int or float
        :param x: x value, where x-axis represents the time
        :type x: int
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :returns: a tuple of S,I,R in tn, where n=time step
        """
        S = -beta * y[0] * y[1] / self.N
        I = beta * y[0] * y[1] / self.N - gamma * y[1]
        R = gamma * y[1]
        return S, I, R

    def fit_model(self, x_data, beta, gamma):
        """
        This function start the fitting process.
        It integrate a system of ordinary differential equations.

        :param x_data: data on x-axis
        :type x_data: list
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :returns: a fitted model for infected individuals
        """
        return integrate.odeint(self.model, self.N0, x_data, args=(beta, gamma))[:, 1]


class Vaccine(SIR):
    def __init__(self):
        SIR.__init__(self)

    def model(self, y, x, beta, gamma, nu):
        S = -beta * y[0] * y[1] / self.N - nu * y[0]
        I = beta * y[0] * y[1] / self.N - gamma * y[1]
        R = gamma * y[1] + nu * y[2]
        return S, I, R

    def fit_model(self, x, beta, gamma, nu):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, nu))[:, 1]


class WithBirthsAndDeaths(SIR):
    def __init__(self):
        SIR.__init__(self)

    def model(self, y, x, beta, gamma, mu):
        S = -beta * y[0] * y[1] / self.N + mu * (self.N - y[0])
        I = beta * y[0] * y[1] / self.N - gamma * y[1] - mu * y[1]
        R = gamma * y[1] - mu * y[2]
        return S, I, R

    def fit_model(self, x, beta, gamma, mu):
        return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, mu))[:, 1]
