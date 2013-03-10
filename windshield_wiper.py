#!/usr/bin/python

from i2c_lib import lcddriver as lcddriver
import time


lcd = lcddriver.lcd(init=False)

for y in range(1,20):
    for x in range(1,5):
        lcd.lcd_display_string(' '*y+'|', x)

lcddriver.lcd()
