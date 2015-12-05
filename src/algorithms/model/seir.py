import numpy as np

## define ODE equations
def ode(seir_values, t, mu, sigma, beta, gamma, k):
    s = seir_values[0]
    e = seir_values[1]
    i = seir_values[2]

    seir = np.zeros((3))    
    seir[0] = mu - beta * s * i - mu * s
    seir[1] = beta * s * i - sigma * e - mu * e
    seir[2] = sigma * e - gamma * i - mu * i
    return seir

## define initial parameters: mu, alpha, beta, gamma
def param():
    # mu = death rate, birth rate
	# beta = transmission rate between S and I + probability of transmission
	# sigma = rate at which individuals move from the exposed to the infectious classes. 
	# Its reciprocal (1/sigma) is the average latent (exposed) period.
	# gamma = recovery rate

    return [0, 0.75, 0.75, 0.75]
    
def pop(I, k):
    I0 = I*k
    S0 = 1 - I0
    N = [S0, 0, I0, 0]
    return N