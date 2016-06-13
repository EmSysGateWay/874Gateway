import serial
import time

ser = serial.Serial(
            port='/dev/ttyAMA0',
            baudrate = 9600,
			parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)
            
while True:
    data = ser.readline()
    if len(data)>0:
        print data
    time.sleep(1)