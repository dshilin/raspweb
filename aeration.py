#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from relay import Relay
r = Relay()
r.ON_AERATION()
time.sleep(30)
r.OFF_AERATION()

