import pyodbc
import sys
import os
import platform
from os.path import expanduser
import csv
import datetime
import time

def __db_open():

	with open(os.path.join('C:/Users/yjunlee.NA/', '.auth/pw.txt'), 'r') as file:
		passwd = file.readline().rstrip()
	

__db_open()