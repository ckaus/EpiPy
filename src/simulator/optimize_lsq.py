# -*- coding: utf-8 -*-

from algorithm import Leastsquare
from model import sir_model as sir

def execute_lsq(steps, data, start_, end_t):
	for i in range(start_t, end_t, steps):
		lsq = Leastsquare(sir, self.data, i)
		lsq.run()
		check_errors(lsq.erros)

def check_errors(errors):
	if errors > 0.0 and errors < 1.0:
		return True
	return False