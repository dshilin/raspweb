#!/usr/bin/env python
import sqlite3


print "Content-type: text/html\n";
	
conn = sqlite3.connect('/home/pi/webOs/hozyin_database.db')

cursor = conn.execute("SELECT temperature from CURR_TEMP;")
for row in cursor:
	print row[0];

conn.close()
