#!/usr/bin/env python

import sqlite3
import RPi.GPIO as GPIO

DATA_PIN = 24
SCK_PIN = 23

from select_current_temp import curr_temp
from select_current_hum import curr_hum
from get_temp_par import temp_par
from get_hum_par import hum_par
ct=curr_temp()
ch=curr_hum()
tp=temp_par()
hp=hum_par()

conn=sqlite3.connect('/home/pi/webOs/database.db')

curs=conn.cursor()
temp=ct
hum=ch
if ct<tp:
	temp=temp+0.1
	hum=hum+0.1
else:
	temp=temp-0.1
	hum=hum-0.1
	
 
def add_temps(temp, hum):
	curs.execute("""UPDATE curr_temp SET tdate=date('now'), ttime=time('now'), temperature=(?), humidity=(?)""", (temp, hum))

add_temps(temp, hum)
      
conn.commit()

conn.close()
