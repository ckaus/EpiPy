# -*- coding: utf-8 -*-

"""The (S)usceptible (E)xposed (I)nfected (R)ecovered Model."""


def init_model(N, y0):
    """Initialize the SEIR model.

    :param int y0: Infected rate at initial time step.
    :param int N: Population

    :returns: Model at initial time step
    :rtype: tuple(int, int, int)
    """
    return N - y0, y0, 0, 0


def simple(y, x, N, beta, gamma, sigma, mu):
    """Defines the SEIR simple model.

    :param array y: Individuals at time step x
    :param array x: Time step
    :param int N: Population
    :param float beta: The parameter controlling how often a
        susceptible-infected contact results in a new infection.
    :param float gamma: The rate an infected recovers and moves into the
        resistant phase.
    :param float sigma: The rate at which an exposed person becomes infective.
    :param float mu: The parameter represents the average death rate

    :returns: S, E, I, R at time step n
    :rtype: tuple(int/float, int/float, int/float)
    """
    S = mu * (N - y[0]) - (beta * y[0] * y[2] / N)
    E = beta * y[0] * y[2] / N - (mu + sigma) * y[1]
    I = sigma * y[1] - (mu + gamma) * y[2]
    R = gamma * y[2] - mu * y[3]
    return S, E, I, R
