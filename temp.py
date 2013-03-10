#!/usr/bin/python

import datetime
import sys

import sqlite3

import lcddriver


def get_dbhandle():
    con = None
    con = sqlite3.connect('/var/lib/rpi-datalogger/database.db')
    return con

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

def main():
    inside = get_temp("/sys/bus/w1/devices/28-000003d37411/w1_slave")
    outside = get_temp("/sys/bus/w1/devices/28-000003ea8a14/w1_slave")

    con = get_dbhandle()
    cur = con.cursor()
    sql = 'insert into trends (timestamp, insidetemp_f, outsidetemp_f) values ("%s", %s, %s)' % ( str(datetime.datetime.now())[0:19], inside, outside)


    print sql 
    cur.execute(sql)
    con.commit()
    print str(datetime.datetime.now())[0:19],",",inside,",",outside
    lcd = lcddriver.lcd(init=False)
    lcd.lcd_display_string("Inside : " +str(inside)+' F  ',2)
    lcd.lcd_display_string("Outside: " + str(outside) + " F  ", 3)
    lcd.lcd_display_string(str(datetime.datetime.now())[0:19],4)


if __name__ == "__main__":
    main()

