# -*- coding: utf-8 -*-

''' 
	File:
		importer.py 
	Description: 
		This file import data to a database
'''

CREATE_TABLES_Q = '''
CREATE TABLE location (
	id	serial,
	city	varchar(40),
	PRIMARY KEY (id)
);

CREATE TABLE SIdataset (
	id 	serial,
	locationID 	integer,
	date 		date	NOT NULL,
	susceptable 	float8		NOT NULL,
	infected 	float8		NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (locationID) REFERENCES location (id)
);
'''
from database import Database
import sys
import csv
import re

def init_db():
	db = Database().get_connection()
	db.execute(CREATE_TABLES_Q)
	with open('../datasets/1.csv', 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			date = row['Time_Date']
			location = row['City'].replace(',','')
			if 'NA' in row['Suscept'] or 'NA' in row['Infect']:
				continue
			else:
				# check whether the location already exist
				db.execute('SELECT 1 FROM location WHERE city='"'%s'"';' % (location))
				locationID = db.fetchone()
				if locationID is None:
					db.execute('INSERT INTO location (city) VALUES ('"'%s'"');' % (location))
				else:
					susceptable = float(row['Suscept'])
					infected = float(row['Infect'])
					db.execute('INSERT INTO SIdataset (locationID, date, susceptable, infected) VALUES (%d, '"'%s'"', %f, %f);' % (int(locationID[0]), date, susceptable, infected))

if __name__ == "__main__":
	allowed_args = ['init', 'update']
	if len(sys.argv) == 2 and sys.argv[1] in allowed_args: 
		if sys.argv[1] == 'init':
			init_db()
	else:
		print '''Usage:
		python importer.py [command]
	\bCommands:
		init - Initialize database with tables for the first time 
		update - Update database set with data'''