#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


print "Content-type: text/html\n";
	
conn = sqlite3.connect('./hozyin_database.db')

cursor = conn.execute("SELECT temp_par from CAMERA_PARAMS;")
for row in cursor:
	print row[0];

conn.close()
