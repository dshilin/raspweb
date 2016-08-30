#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

print "Content-type: text/html\n"

print '0'
        
conn=sqlite3.connect('/home/baas/webOs/database.db')

curs=conn.cursor()

curs.execute("""UPDATE camera_params SET is_enabled=0""")
      
conn.commit()

conn.close()
