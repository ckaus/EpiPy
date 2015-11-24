## SI model

from pymc import *
from numpy import *

#observed data
T = 10
susceptible_data = array([999,997,996,994,993,992,990,989,986,984])
infected_data = array([1,2,5,6,7,8,9,11,13,15])

# stochastic priors
beta = Uniform('beta', 0., 40., value=1.)
gamma = Uniform('gamma', 0., 1., value=.001)
SI_0 = Uninformative('SI_0', value=[999., 1.])

# deterministic compartmental model
@deterministic
def SI(SI_0=SI_0, beta=beta, gamma=gamma):
    S = zeros(T)
    I = zeros(T)
    S[0] = SI_0[0]
    I[0] = SI_0[1]
    for i in range(1,T):
        S[i] = S[i-1] - 0.05*beta*S[i-1]*I[i-1]/(S[i-1]+I[i-1])
        I[i] = max(0., I[i-1] + 0.05*beta*S[i-1]*I[i-1]/(S[i-1]+I[i-1]) - gamma*I[i-1])
    return S, I
S = Lambda('S', lambda SI=SI: SI[0])
I = Lambda('I', lambda SI=SI: SI[1])

# data likelihood
# Poisson = http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.poisson.html
#           https://en.wikipedia.org/wiki/Poisson_distribution
A = Poisson('A', mu=S, value=susceptible_data, observed=True)
B = Poisson('B', mu=I, value=infected_data, observed=True)