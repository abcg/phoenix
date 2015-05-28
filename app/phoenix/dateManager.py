#|/usr/bin/python

from datetime import *

def parseDate(date):
    return datetime.strptime(date, '%Y-%m-%d').date()

def today():
    return datetime.now().date()

def dateToString(date):
    date.strftime('%Y-%m-%d')

