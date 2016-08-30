#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def curr_temp():	
        conn = sqlite3.connect("/home/baas/webOs/database.db")
        cursor = conn.execute("SELECT temperature from CURR_TEMP;")
        for row in cursor:
                 ct=row[0];
        conn.close()
        return ct
        
if __name__ == '__main__':
        print ("Content-type: text/html\n")
        print (curr_temp())
else:
        curr_temp()
