# # -*- coding: utf-8 -*-

# from basemodel import BaseModel

# class SEIR(BaseModel):

#     def __init__(self, xdata, ydata):
#         BaseModel.__init__(self)
#         self.xdata = xdata
#         self.ydata = ydata
#         self.N = 1
#         self.N0 = self.init_param(ydata, self.N)

#     def init_param(self, ydata, N):
#         I0 = ydata[0]
#         S0 = N - I0
#         return S0, I0

#     def model(self, y, x, beta, gamma, sigma, mu):
#     	s = y[0]
#     	e = y[1]
#     	i = y[2]
#     	r = y[3]

#     	S = mu - beta * s * i - mu * s
#     	E = beta * s * i - ( mu + sigma ) *  e
#     	I = sigma * e - ( mu + gamma ) * i
#     	R = gamma * i - mu * r
#     	return S, E, I, R

# 	def fit_odeint(x, beta, gamma, sigma, mu):
# 		print sigma
# 		return integrate.odeint(self.model, self.N0, x, args=(beta, gamma, signma, mu))[:,1]