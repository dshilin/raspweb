#!/usr/bin/env python

import sqlite3

def curr_hum():
        conn = sqlite3.connect('/home/pi/webOs/hozyin_database.db')
        cursor = conn.execute("SELECT humidity from CURR_TEMP;")
        for row in cursor:
                ch=row[0];
        conn.close()
        return ch
        
if __name__ == '__main__':
        print "Content-type: text/html\n"
        print curr_hum()
else:
        curr_hum()
