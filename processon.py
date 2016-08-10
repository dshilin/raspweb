#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

print "Content-type: text/html\n"

print "1"

conn=sqlite3.connect('/home/pi/webOs/database.db')

curs=conn.cursor()

curs.execute("""UPDATE camera_params SET is_enabled=1""")
      
conn.commit()

conn.close()

#from ma import main
#main()
