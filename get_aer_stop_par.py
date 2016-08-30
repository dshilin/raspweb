#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def aer_stop_par():
        conn = sqlite3.connect('/home/baas/webOs/database.db')
        cursor = conn.execute("SELECT aer_stop from CAMERA_PARAMS;")
        for row in cursor:
                 ao=row[0];
        conn.close()
        return ao
        
if __name__ == '__main__':
        print ("Content-type: text/html\n")
        print (aer_stop_par())
else:
        aer_stop_par()
