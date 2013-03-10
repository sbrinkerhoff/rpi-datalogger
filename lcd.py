#!/usr/bin/python

from time import *
import sys

from i2c_lib import *
from i2c_lib import lcddriver as lcddriver

try:
    if sys.argv[3] == "init":
        lcd = lcddriver.lcd()
except:
    pass

lcd = lcddriver.lcd(init=False)

lcd.lcd_display_string(sys.argv[1], int(sys.argv[2]))

