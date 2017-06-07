# Introduction

## Why EpiPy?

Several tools are available that can simulate epidemics and generate data with given parameter for an epidemic model. 
However, there is yet no tool for easy fitting of epidemic models. EpiPy simplifies the fitting of various models to 
data and aims to help you understand different epidemics models. It offers a range of possibilities for you to explore.

## What Are Epidemic Models?

Epidemics have been an interesting subject to study in many disciplines. Not only in epidemiology but also in biology, 
mathematics, sociology, computer science and more, the study of epidemics offers many areas for application. 
Mathematicians over time have suggested various models to understand and foresee the development of epidemics.

For example, SIR model is defined by the following equations:

![SIR Model](http://i.imgur.com/rdFWsJJ.png)

where β is the rate of infection and ɣ the rate of recovery.

If we solve the equations and plot against time, we get three curves representing the numbers of susceptibles, infected,
and recovered respectively. The shape of the graph depends on the parameters β, ɣ, S0 and I0.

![Graph of SIR Model](http://i.imgur.com/Y7TMSUk.png)

## Parameter Estimation

The most commonly used algorithms for the parameter estimation according to [Sam2013] can be categorised into 
deterministic methods and stochastic methods. Of those, deterministic methods include gradient-based approaches, which
have advantages such as simplicity of applications and short computation time. Their disadvantage is that the estimated
parameters are dependent of the initial values but it can be mitigated by iteration.

We have adopted the least squares method out of many including Markov Chain Monte Carlo, Bayes estimators and Maximum
likelihood, due to its simplicity in the implementation.

[Sam2013] Samsuzzoha, M., Singh, M., & Lucy, D. (2013). Parameter estimation of influenza epidemic model. 
Applied Mathematics and Computation, 220, 616-629.