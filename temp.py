#!/usr/bin/python

""" Simple Python datalogger for the Raspberry PI """

import datetime
import sys

import sqlite3


def get_dbhandle():
    """ Return a database handle to the SQLite file """
    con = None
    con = sqlite3.connect('/var/lib/rpi-datalogger/database.db')
    return con

def get_temp(file_link):
    """ Given a file_link to a dallas one-wire device return the
        temperature in fahrenheit  """

    with open(file_link) as sensor: 
        text = sensor.read()

    firstline = text.split("\n")[0]
    secondline = text.split("\n")[1]
    if not 'YES' in firstline:
        sys.exit(0)
    temp = secondline.split(" ")[9]

    # Sensor reads in celsius, C * 1.8 + 32 = F
    temp = round((int(temp[2:])/1000.0)*1.8+32, 2)
    return temp

def update_lcd():
    """ Update the onboard LCD with the current temps. """

    #from i2c_lib import lcddriver

    #lcd = lcddriver.lcd(init=False)
    #lcd.lcd_display_string("Inside : " +str(inside)+' F  ', 2)
    #lcd.lcd_display_string("Outside: " + str(outside) + " F  ", 3)
    #lcd.lcd_display_string(curdate, 4)


def main():
    """ Where the magic happens. """

    inside = get_temp("/sys/bus/w1/devices/28-000003d37411/w1_slave")
    outside = get_temp("/sys/bus/w1/devices/28-000003ea8a14/w1_slave")

    curdate = str(datetime.datetime.now())[0:19]

    con = get_dbhandle()
    cur = con.cursor()
    sql = 'insert into trends (timestamp, insidetemp_f, outsidetemp_f) \
           values ("%s", %s, %s)' % (curdate, inside, outside)

    cur.execute(sql)
    con.commit()

    print curdate, ",", inside, ",", outside


if __name__ == "__main__":
    main()

