# -*- coding: utf-8 -*-

"""This file contains functionality for loggin information."""

import inspect

class _Color:
	ERROR = '\033[91m' # red
	INFO = '\033[94m' # blue
	NORMAL = '\033[0m' # default
	SUCCESS = '\033[92m' # green
	WARNING = '\033[93m' # yellow

"""
Print messages to terminal with different colors
"""
def error(msg):
	clasz = inspect.stack()[1][1]
	line = inspect.stack()[1][2]
	func = inspect.stack()[1][3]
	
	print '[%s%s%s] Class: %s in %s() on line %s\n\tMessage: %s'\
	% (_Color.ERROR, 'ERROR', _Color.NORMAL, clasz,func, line, msg)
	
def info(msg):
	print '[%s%s%s] %s' % (_Color.INFO, 'INFO', _Color.NORMAL, msg)

def success(msg):
	print '[%s%s%s] %s' % (_Color.SUCCESS, 'SUCCESS', _Color.NORMAL, msg)

def warning(msg):
	print '[%s%s%s] %s' % (_Color.WARNING, 'WARNING', _Color.NORMAL,msg)