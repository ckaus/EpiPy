# -*- coding: utf-8 -*-

''' 
  Name: 
    Christian Kaus
  File:
    database.py 
  Description: 
    This file represents the database connection.
'''

import psycopg2
import ConfigParser
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# import logger

class Singleton:
  def __init__(self, llass):
    self.llass = llass
    self.instance = None
  def __call__(self, *args, **kwds):
    if self.instance == None:
      self.instance = self.llass(*args, **kwds)
    return self.instance

@Singleton
class Database:
  connection = None
  '''This function returns a connection to database'''
  def get_connection(self):
    try:
      if self.connection is not None:
        cur = self.connection.cursor()
        '''if not failed, database is reachable'''
        cur.execute('SELECT 1')
        return self.connection.cursor()
      else:
        config = ConfigParser.ConfigParser()
        config.read('../config.cfg')
        dbname = config.get('db_access', 'dbname')
        user = config.get('db_access','user')
        host = config.get('db_access', 'host')
        password = config.get('db_access', 'password')
        properties = 'dbname='+ dbname + ' user='+ user + ' host='+ host +' password='+ password
        self.connection = psycopg2.connect(properties)
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return self.connection.cursor()
    except:
      print 'Database is not reachable'
      # logger.error('Database is not reachable')
      return