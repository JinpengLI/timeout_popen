# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:24:40 2013

@author: jinpeng
"""

import datetime
import time
import sys


# seconds
duration = 20
start = datetime.datetime.now()
while True:
    now = datetime.datetime.now()
    if (now - start).seconds > duration:
        break
    sys.stdout.write("now is %s" % repr(now))
    time.sleep(1)
print "finished"
