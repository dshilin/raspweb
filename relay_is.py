#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
##import time
##import signal
##import sys

from relay import Relay
r = Relay()
### Called on process interruption. Set all pins to "Input" default mode.
##def endProcess(signalnum = None, handler = None):
##        r.ALLOFF()
##        sys.exit()
##
##signal.signal(signal.SIGINT, endProcess)

from is_enabled import is_enabled
while is_enabled():
        from select_current_temp import curr_temp
        from select_current_hum import curr_hum
        from get_temp_par import temp_par
        from get_hum_par import hum_par
        ct=curr_temp()
        ch=curr_hum()
        tp=temp_par()
        hp=hum_par()
        if ct>tp:
                if not r.IS_REFRIGERATOR():
                        r.ON_REFRIGERATOR()
        else:
                if r.IS_REFRIGERATOR():
                        r.OFF_REFRIGERATOR()
        if ch<hp:
                if not r.IS_HUMIDIFIER():
                        r.ON_HUMIDIFIER()
        else:
                if r.IS_HUMIDIFIER():
                        r.OFF_HUMIDIFIER()

else:
        print "off. waiting... while on"
