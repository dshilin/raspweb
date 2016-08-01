#!/usr/bin/env python

import sqlite3
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x

DATA_PIN = 24
SCK_PIN = 23

conn=sqlite3.connect('/home/pi/webOs/hozyin_database.db')

curs=conn.cursor()

with SHT1x(DATA_PIN, SCK_PIN, gpio_mode=GPIO.BCM, resolution='Low') as sensor:
    temperature = sensor.read_temperature()
    humidity = sensor.read_humidity(temperature)
 
def add_temps(temp, hum):
	curs.execute("""UPDATE curr_temp SET tdate=date('now'), ttime=time('now'), temperature=(?), humidity=(?)""", (temp, hum))

add_temps(temperature, humidity)
      
conn.commit()

conn.close()
