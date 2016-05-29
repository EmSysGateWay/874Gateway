import RPi.GPIO as GPIO         ## Import GPIO Library
import time                     ## Import 'time' library (for 'sleep')
import serial
# A : Receive
# DE : 7
# RE : 11

# B : Sent
# DE 13
# RE 15

class GateWay485:
    # pin_DE : DE pin number of RPi
    # pin_RE : RE pin number of RPi
    def __init__(self,pinHigh, pinLow):
        self.pinHigh = pinHigh
        self.pinLow = pinLow
        GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering
        # setup the gpio condition
        GPIO.setup(self.pinHigh, GPIO.OUT)
        GPIO.setup(self.pinLow, GPIO.OUT)
        
		# set a_RE = 1, a_DE = 1
        GPIO.output(self.pinHigh, GPIO.HIGH)
        GPIO.output(self.pinLow, GPIO.LOW)
        
        self.ser = serial.Serial(
            port='/dev/ttyAMA0',
            baudrate = 9600,
			parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)

    def write(self,str):
        writeStr = str.replace('\r', '') 
        writeStr = writeStr.replace('\n', '') 
        writeStr = '#'+ writeStr + '\n'
        self.ser.write(writeStr)

    def readline(self):
        data = self.ser.readline()
        print data[1:-1]
        return data[1:-1]
        
    def read(self,num):
        return self.ser.read(num)

if __name__ == '__main__':

    a = GateWay485(7,11)
    while True:
        str = a.readline()
        print str
    print 'HEHE'
    