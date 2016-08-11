#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi, cgitb
import sqlite3

form = cgi.FieldStorage()

astart = form.getvalue('astart')

astop  = form.getvalue('astop')

conn=sqlite3.connect('/home/pi/webOs/database.db')

curs=conn.cursor()

curs.execute("""UPDATE camera_params SET tdate=date('now'), ttime=time('now'), aer_start=(?), aer_stop=(?)""", (astart, astop))
      
conn.commit()

conn.close()

print "Content-type: text/html\n"
print 1
