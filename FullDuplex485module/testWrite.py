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
    data = ser.write('hehe\r\n')
    time.sleep(1)