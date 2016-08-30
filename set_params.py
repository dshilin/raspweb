#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi, cgitb
import sqlite3

form = cgi.FieldStorage()

temp_par = form.getvalue("temperature")

hum_par  = form.getvalue("humidity")

conn=sqlite3.connect("/home/baas/webOs/database.db")

curs=conn.cursor()

curs.execute("""UPDATE camera_params SET tdate=date('now'), ttime=time('now'), temp_par=(?), hum_par=(?)""", (temp_par, hum_par))
      
conn.commit()

conn.close()

print "Content-type: text/html\n"
print 1
