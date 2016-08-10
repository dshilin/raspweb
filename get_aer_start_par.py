#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def aer_start_par():
        conn = sqlite3.connect('/home/pi/webOs/database.db')
        cursor = conn.execute("SELECT aer_start from CAMERA_PARAMS;")
        for row in cursor:
                 aa=row[0];
        conn.close()
        return aa
        
if __name__ == '__main__':
        print ("Content-type: text/html\n")
        print (aer_start_par())
else:
        aer_start_par()
