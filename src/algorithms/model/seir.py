import numpy as np


## define ODE equations
def ode(N, t, mu, alpha, beta, gamma, k):
     # Creating an array of equations
    Eqs = np.zeros((3))
    Eqs[0] = mu*beta*N[0]*N[2] - mu*N[0]
    Eqs[1] = beta*N[0]*N[2] - (mu+alpha)*N[1]
    Eqs[2] = alpha*N[1]-(mu+gamma)*N[2]
    return Eqs

## define initial parameters: mu, alpha, beta, gamma
def param():
    return [0, 0.75, 0.75, 0.75]
    
def pop(I, k):
    I0 = I*k
    S0 = 1 - I0
    N = [S0, 0, I0, 0]
    return N