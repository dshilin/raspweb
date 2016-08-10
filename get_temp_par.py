#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def temp_par():
        conn = sqlite3.connect('/home/pi/webOs/database.db')
        cursor = conn.execute("SELECT temp_par from CAMERA_PARAMS;")
        for row in cursor:
                 tp=row[0]
        conn.close()
        return tp

if __name__ == '__main__':
        print ("Content-type: text/html\n")
        print (temp_par())
else:
        temp_par()
