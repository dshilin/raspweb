from threading import Thread

import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
                
class Relay():
    
    global bus
    
    def __init__(self):
        self.DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
        self.DEVICE_REG_MODE1 = 0x06
        self.DEVICE_REG_DATA = 0xff
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_REFRIGERATOR(self):
        print ('ON REFRIGERATOR')
        self.DEVICE_REG_DATA &= ~(0x1<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
        time.sleep(2.0)
        
    def ON_HUMIDIFIER(self):
        print ('ON HUMIDIFIER')
        self.DEVICE_REG_DATA &= ~(0x1<<1)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
        
    def ON_AERATION(self):
        print ('ON AERATION')
        self.DEVICE_REG_DATA &= ~(0x1<<2)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
    def ON_HEATER(self):
        print ('ON HEATER')
        self.DEVICE_REG_DATA &= ~(0x1<<3)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_REFRIGERATOR(self):
        print ('OFF REFRIGERATOR')
        self.DEVICE_REG_DATA |= (0x1<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
        time.sleep(2.0)
        
    def OFF_HUMIDIFIER(self):
        print ('OFF HUMIDIFIER')
        self.DEVICE_REG_DATA |= (0x1<<1)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_AERATION(self):
        print ('OFF AERATION')
        self.DEVICE_REG_DATA |= (0x1<<2)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_HEATER(self):
        print ('OFF HEATER')
        self.DEVICE_REG_DATA |= (0x1<<3)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLON(self):
        print ('ALLON')
        self.DEVICE_REG_DATA &= ~(0xf<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLOFF(self):
        print ('ALLOFF')
        self.DEVICE_REG_DATA |= (0xf<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def IS_REFRIGERATOR(self):
        #print bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)
        if (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==254):
            print ('REFRIGERATOR is ON')
            return True
        elif (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==252):
            print ('REFRIGERATOR is ON')
            return True
        else:
            print ('REFRIGERATOR is OFF')
            return False

    def IS_HUMIDIFIER(self):
        #print bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)
        if (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==253):
            print ('HUMIDIFIER is ON')
            return True
        elif (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==252):
            print ('HUMIDIFIER is ON')
            return True
        else:
            print ('HUMIDIFIER is OFF')
            return False

class AerThread(Thread):
    
    global r
       
    def __init__(self):
       super(AerThread,self).__init__()
       return

    def run(self):
        while True:
            from is_enabled import is_enabled
            while is_enabled():
                from get_aer_start_par import aer_start_par
                from get_aer_stop_par import aer_stop_par
                time.sleep(aer_start_par())
                self.aer_start()
                time.sleep(aer_start_par())
                self.aer_stop()
            
    def aer_stop(self):
        global r
        r.OFF_AERATION()
        return
    
    def aer_start(self):
        global r
        r.ON_AERATION()
        return
       
if __name__=="__main__":

    r=Relay()    
    at=AerThread()
    at.start()
    def cam():
            from select_current_temp import curr_temp
            from select_current_hum import curr_hum
            from get_temp_par import temp_par
            from get_hum_par import hum_par
            ct=curr_temp()
            ch=curr_hum()
            tp=temp_par()
            hp=hum_par()
            if ct>tp:
                    if r.IS_REFRIGERATOR():
                            pass     
                    else:
                            r.ON_REFRIGERATOR()
            else:
                    if r.IS_REFRIGERATOR():
                            r.OFF_REFRIGERATOR()
            if ch<hp:
                    if r.IS_HUMIDIFIER():
                            pass        
                    else:
                            r.ON_HUMIDIFIER()
            else:
                    if r.IS_HUMIDIFIER():
                            r.OFF_HUMIDIFIER()

    while True:
        from is_enabled import is_enabled
        while is_enabled():
            cam()
        r.ALLOFF()

