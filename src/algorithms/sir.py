import numpy as np


## define ODE equations
def ode(N, t, beta, gamma, k):
     # Creating an array of equations
    Eqs = np.zeros((3))
    Eqs[0] = -beta*N[0]*N[1]
    Eqs[1] = beta*N[0]*N[1] - gamma*N[1]
    Eqs[2] = gamma*N[1]
    return Eqs

## define initial parameters
def param():
    return [0.75, 0.75]