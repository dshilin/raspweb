
import smbus

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

class Relay():
    global bus
    def __init__(self):
        self.DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
        self.DEVICE_REG_MODE1 = 0x06
        self.DEVICE_REG_DATA = 0xff
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ON_REFRIGERATOR(self):
        print 'ON REFRIGERATOR'
        self.DEVICE_REG_DATA &= ~(0x1<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
    def ON_HUMIDIFIER(self):
        print 'ON HUMIDIFIER'
        self.DEVICE_REG_DATA &= ~(0x1<<1)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
    def ON_AERATION(self):
        print 'ON AERATION'
        self.DEVICE_REG_DATA &= ~(0x1<<2)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)
    def ON_HEATER(self):
        print 'ON HEATER'
        self.DEVICE_REG_DATA &= ~(0x1<<3)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_REFRIGERATOR(self):
        print 'OFF REFRIGERATOR'
        self.DEVICE_REG_DATA |= (0x1<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_HUMIDIFIER(self):
        print 'OFF HUMIDIFIER'
        self.DEVICE_REG_DATA |= (0x1<<1)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_AERATION(self):
        print 'OFF AERATION'
        self.DEVICE_REG_DATA |= (0x1<<2)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def OFF_HEATER(self):
        print 'OFF HEATER'
        self.DEVICE_REG_DATA |= (0x1<<3)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLON(self):
        print 'ALLON'
        self.DEVICE_REG_DATA &= ~(0xf<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def ALLOFF(self):
        print 'ALLOFF'
        self.DEVICE_REG_DATA |= (0xf<<0)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def IS_REFRIGERATOR(self):
        #print bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)
        if (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==254):
            print 'REFRIGERATOR is ON'
            return True
        elif (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==252):
            print 'REFRIGERATOR is ON'
            return True
        else:
            print 'REFRIGERATOR is OFF'
            return False

    def IS_HUMIDIFIER(self):
        #print bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)
        if (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==253):
            print 'HUMIDIFIER is ON'
            return True
        elif (bus.read_byte_data(self.DEVICE_ADDRESS,self.DEVICE_REG_MODE1)==252):
            print 'HUMIDIFIER is ON'
            return True
        else:
            print 'HUMIDIFIER is OFF'
            return False

##
##if __name__=="__main__":
##        
