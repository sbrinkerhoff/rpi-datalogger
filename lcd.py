#!/usr/bin/python

import lcddriver
from time import *
import sys

try:
    if sys.argv[3] == "init":
        lcd = lcddriver.lcd()
except:
    pass

lcd = lcddriver.lcd(init=False)

lcd.lcd_display_string(sys.argv[1], int(sys.argv[2]))

