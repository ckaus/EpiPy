""" Script to fit the SI model defined in si_model.py

Also produce some plots, to be used in a short healthyalgorithms blog
post about attaching statistical models to system dynamics models

http://healthyalgorithms.com/2010/10/19/mcmc-in-python-how-to-stick-a-statistical-model-on-a-system-dynamics-model-in-pymc/

"""

from pylab import *
from pymc import *

# load the model
import si_model as mod
reload(mod)  # this reload streamlines interactive debugging

def start():
    # fit the model with mcmc
    mc = MCMC(mod)
    mc.use_step_method(AdaptiveMetropolis, [mod.beta, mod.gamma, mod.SI_0])
    mc.sample(iter=200000, burn=100000, thin=20, verbose=1)

    # plot the estimated size of S and I over time
    figure(1)

    subplots_adjust(hspace=0, right=1)
    subplot(2, 1, 1)
    title('SI model with uncertainty')
    plot(mod.susceptible_data, 's', mec='black', color='black', alpha=.9)
    plot(mod.S.stats()['mean'], color='red', linewidth=2)
    plot(mod.S.stats()['95% HPD interval'], color='red',
     linewidth=1, linestyle='dotted')
    yticks([950,975,1000,1025])
    ylabel('S (people)')
    axis([-1,10,925,1050])

    subplot(2, 1, 2)
    plot(mod.infected_data, 's', mec='black', color='black', alpha=.9)
    plot(mod.I.stats()['mean'], color='blue', linewidth=2)
    plot(mod.I.stats()['95% HPD interval'], color='blue', linewidth=1, linestyle='dotted')
    xticks(range(1,10,2))
    xlabel('Time (days)')
    yticks([0,15,30])
    ylabel('I (people)')
    axis([-1,10,-1,35])
    savefig('SI.png')

if __name__ == '__main__':
    start()