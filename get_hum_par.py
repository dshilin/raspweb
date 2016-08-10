#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def hum_par():
        conn = sqlite3.connect('/home/pi/webOs/database.db')
        cursor = conn.execute("SELECT hum_par from CAMERA_PARAMS;")
        for row in cursor:
                 hp=row[0];
        conn.close()
        return hp
        
if __name__ == '__main__':
        print ("Content-type: text/html\n")
        print (hum_par())
else:
        hum_par()
