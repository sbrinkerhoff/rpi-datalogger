#!/usr/bin/python
import datetime
import sys
def get_temp(file_link):
   file = open(file_link)
   text = file.read()
   file.close()
   firstline = text.split("\n")[0]
   if not 'YES' in firstline:
     sys.exit(0)
   secondline = text.split("\n")[1]
   temp = secondline.split(" ")[9]


   temp = round((int(temp[2:])/1000.0)*1.8+32,2)
   return temp


inside = get_temp("/sys/bus/w1/devices/28-000003d37411/w1_slave")
outside = get_temp("/sys/bus/w1/devices/28-00000428d743/w1_slave")

print str(datetime.datetime.now())[0:19],",",inside,",",outside

import lcddriver
import sys

lcd = lcddriver.lcd(init=False)




lcd.lcd_display_string("Inside : " +str(inside)+' F  ',2)
lcd.lcd_display_string("Outside: " + str(outside) + " F  ", 3)
lcd.lcd_display_string(str(datetime.datetime.now())[0:18],4)




