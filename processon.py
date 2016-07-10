#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import smbus
import signal
import sys
import sqlite3

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
print "Content-type: text/html\n";
class Relay():  
    global bus
    def __init__(self):
        self.DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
        self.DEVICE_REG_MODE1 = 0x06
        self.DEVICE_REG_DATA = 0xff
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
             
    def ON_1(self): 
        print '1'
        self.DEVICE_REG_DATA &= ~(0x1<<0)  
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
        
relay = Relay()

relay.ON_1()

conn=sqlite3.connect('./hozyin_database.db')

curs=conn.cursor()

curs.execute("""UPDATE camera_params SET is_enabled=1""")
      
conn.commit()

conn.close()
