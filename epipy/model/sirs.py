# -*- coding: utf-8 -*-

from scipy import integrate

from basemodel import BaseModel


class SIRS(BaseModel):
    """
    This class represents an abstract model for SIRS Models.
    """

    def __init__(self):
        BaseModel.__init__(self)
        self.__name__ = 'SIRS'

    def init_param(self, y0):
        """
        This function initialize the model parameters.

        :param y0: infected value in t0.
        :type y0: int or float

        :returns: tuple of S,I,R model values in t0
        """
        I0 = y0
        S0 = self.N - I0
        R0 = 0.0
        return S0, I0, R0


class Simple(SIRS):
    """
    This class represents the SIRS Simple Model.
    """

    def __init__(self):
        SIRS.__init__(self)

    @staticmethod
    def param():
        return ["beta", "gamma", "mu"]

    def model(self, y, x, beta, gamma, mu):
        """
        This function defines the SIRS Simple Model.

        :param y: y values, which represents the individuals
        :type y: array
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :param mu: The parameter represents the average death rate
        :type mu: float

        :returns: a tuple of S,I,R in tn, where n=time step
        """
        S = -beta * y[0] * y[1] / self.N + mu * y[2]
        I = beta * y[0] * y[1] / self.N - gamma * y[1]
        R = gamma * y[1] - mu * y[2]
        return S, I, R

    def fit_model(self, x_data, beta, gamma, mu):
        """
        This function start the fitting process.
        It integrates a system of ordinary differential equations.

        :param x_data: data on x-axis
        :type x_data: array
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :param mu: The parameter represents the average death rate
        :type mu: float

        :returns: a fitted model for infected individuals
        """
        return integrate.odeint(self.model, self.N0, x_data, args=(beta, gamma, mu))[:, 1]


class WithBirthsAndDeaths(SIRS):
    """
    This class represents the SIRS with births and deaths Model.
    """

    def __init__(self):
        SIRS.__init__(self)

    def model(self, y, x, beta, gamma, mu, f):
        """
        This function defines the SIRS with births and deaths Model

        :param y: y values, which represents the individuals
        :type y: array
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :param mu: The parameter represents the average death rate
        :type mu: float
        :param f: The parameter represents the average loss of immunity rate of recovered individuals
        :type f: float

        :returns: a tuple of S,I,R in tn, where n=time step
        """
        S = -beta * y[0] * y[1] / self.N + mu * y[2] + f * self.N
        I = beta * y[0] * y[1] / self.N - gamma * y[1] - f * y[1]
        R = gamma * y[1] - mu * y[2] - f * y[2]
        return S, I, R

    def fit_model(self, x_data, beta, gamma, mu, f):
        """
        This function start the fitting process.
        It integrates a system of ordinary differential equations.

        :param x_data: x value, where x-axis represents the time
        :type x_data: int
        :param beta: The parameter controlling how often a susceptible-infected contact results in a new infection.
        :type beta: float
        :param gamma: The rate an infected recovers and moves into the resistant phase.
        :type gamma: float
        :param mu: The parameter represents the average death rate
        :type mu: float
        :param f: The parameter represents the average loss of immunity rate of recovered individuals
        :type f: float

        :returns: a fitted model for infected individuals
        """
        return integrate.odeint(self.model, self.N0, x_data, args=(beta, gamma, mu, f))[:, 1]
