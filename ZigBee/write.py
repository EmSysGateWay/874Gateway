#!/usr/bin/env python     
import struct
import serial
import time
      
ser = serial.Serial( 
      port='/dev/ttyUSB1',	#set port
      baudrate = 9600,		#ser baud rate
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS,
      timeout=None
     )

print "Whether the serial is open:", ser.isOpen()

start = 0xFD
length = 0x15
dest = 0x036A
src = 0x0372
pm25 = 168		#4 bytes
HCHO = 1		#4 bytes formaldehyde concentration
temp = 23		#4 bytes temperature
humidity = 86	#4 bytes humidity
CO = 50			#4 bytes carbon monoxide
rank = 3		#

data1 = struct.pack("<BB2H5IB",
				    start,
				    length,
				    dest,
				    src,
				    pm25,
				    HCHO,
				    temp,
				    humidity,
				    CO,
				    rank
					)

start = 0xFD
length = 0x12
dest = 0x036A
src = 0x036C
longitude = 120.19
eORw = 0
latitude = 30.26
nORs = 3
humidity = 86	#4 bytes humidity
CO = 50			#4 bytes carbon monoxide

data2 = struct.pack("<BB2HfBfBII",
				    start,
				    length,
				    dest,
				    src,
				    pm25,
				    HCHO,
				    temp,
				    humidity,
				    CO,
				    rank
					)

flag = 0    
while 1:
	if(flag):
	   ser.write(data1)	#write
	else:
		ser.write(data2)
	flag = 1 - flag
	time.sleep(5)