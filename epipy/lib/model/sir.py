# -*- coding: utf-8 -*-

"""The (S)usceptible (I)nfected (R)ecovered Model."""

__name__ = "(S)usceptible (I)nfected (R)ecovered Model"


def init_model(N, y0):
    """Initialize the SIR model.

    :param int y0: Infected rate at initial time step.
    :param int N: Population

    :returns: Model at initial time step
    :rtype: tuple(int, int, int)
    """
    return N - y0, y0, 0


def simple(y, x, N, beta, gamma):
    """Defines the SIR simple model.

    :param array y: Individuals at time step x
    :param array x: Time step
    :param int N: Population
    :param float beta: The parameter controlling how often a
        susceptible-infected contact results in a new infection.
    :param float gamma: The rate an infected recovers and moves into the
        resistant phase.

    :returns: S, I, R at time step n
    :rtype: tuple(int/float, int/float, int/float)
    """
    S = -beta * y[0] * y[1] / N
    I = beta * y[0] * y[1] / N - gamma * y[1]
    R = gamma * y[1]
    return S, I, R


def wbad(y, x, N, beta, gamma, mu):
    """Defines the SIR with births and deaths model.

    :param array y: Individuals at time step x
    :param array x: Time step
    :param int N: Population
    :param float beta: The parameter controlling how often a
        susceptible-infected contact results in a new infection.
    :param float gamma: The rate an infected recovers and moves into the
        resistant phase.
    :param float mu: The parameter represents the average death rate

    :returns: S, I, R at time step n
    :rtype: tuple(int/float, int/float, int/float)
    """
    S = -beta * y[0] * y[1] / N + mu * (N - y[0])
    I = beta * y[0] * y[1] / N - gamma * y[1] - mu * y[1]
    R = gamma * y[1] - mu * y[2]
    return S, I, R


def vaccine(y, x, N, beta, gamma, nu):
    """Defines the SIR vaccine model.

    :param array y: Individuals at time step x
    :param array x: Time step
    :param int N: Population
    :param float beta: The parameter controlling how often a
        susceptible-infected contact results in a new infection.
    :param float gamma: The rate an infected recovers and moves into the
        resistant phase.
    :param float nu: The rate at which susceptible become vaccinated.

    :returns: S, I, R at time step n
    :rtype: tuple(int/float, int/float, int/float)
    """
    S = -beta * y[0] * y[1] / N - nu * y[0]
    I = beta * y[0] * y[1] / N - gamma * y[1]
    R = gamma * y[1] + nu * y[2]
    return S, I, R
