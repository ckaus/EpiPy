# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta
from utils import logger

class BaseSimulator():
	def __init__(self):
		__metaclass__ = ABCMeta

	@abstractmethod
	def run(self):
		pass

	def read_file(self, file_path):
		logger.info("%s: read_file with param: file_path=%s" % (self.name, file_path))
		return None

	def plot(self):
		logger.error("Not implemented error")
		raise NotImplementedError