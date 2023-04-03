#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

----------------------------
Installing mysql for python:
----------------------------
https://pypi.org/project/mysqlclient/
https://mysqlclient.readthedocs.io/

----------------------------
If you get the error
----------------------------
ImportError: ... version `GLIBCXX_3.4.21' not found

https://askubuntu.com/questions/575505/glibcxx-3-4-20-not-found-how-to-fix-this-error
conda install libgcc

----------------------------
https://pythonspot.com/mysql-with-python/
https://www.tutorialspoint.com/python/python_database_access.htm
----------------------------
String formatting:
https://pyformat.info/#simple
----------------------------
Install mariadb:
https://linuxhint.com/install-mariadb-linux-mint-21/
----------------------------

"""

import MySQLdb as mysql
from datetime import datetime

db = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="password",     # password
                     db="qcards")   # name of the database

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)
