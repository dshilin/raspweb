#!/usr/bin/env python

import sqlite3

def is_enabled():	
        conn = sqlite3.connect("/home/pi/webOs/hozyin_database.db")
        cursor = conn.execute("SELECT is_enabled from CAMERA_PARAMS;")
        for row in cursor:
                en = row[0]      
        conn.close()
        return en

if __name__ == "__main__":
        print "Content-type: text/html\n"
        print is_enabled()
else:
        is_enabled()
