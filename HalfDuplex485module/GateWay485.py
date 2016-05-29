# author : Liu Zongtao
import RPi.GPIO as GPIO         ## Import GPIO Library
import time                     ## Import 'time' library (for 'sleep')
import serial


class GateWay485:
    # pin_DE : DE pin number of RPi
    # pin_RE : RE pin number of RPi
    def __init__(self,pin_DE, pin_RE):
        self.pin_DE = pin_DE
        self.pin_RE = pin_RE
        
        GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering
        # setup the gpio condition
        GPIO.setup(self.pin_DE, GPIO.OUT)
        GPIO.setup(self.pin_RE, GPIO.OUT)
        
		# set a_RE = 1, a_DE = 1
        GPIO.output(self.pin_RE, GPIO.LOW)
        GPIO.output(self.pin_DE, GPIO.LOW)
        
        self.ser = serial.Serial(
            port='/dev/ttyAMA0',
            baudrate = 9600,
			parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)

    def write(self,str):
        GPIO.output(self.pin_RE, GPIO.HIGH)
        GPIO.output(self.pin_DE, GPIO.HIGH)

        writeStr = '#'+ str + '\n'
        self.ser.write(writeStr)
        
        time.sleep(1)
        GPIO.output(self.pin_RE, GPIO.LOW)
        GPIO.output(self.pin_DE, GPIO.LOW)

    def read(self):
        data = self.ser.readline()
        while True:
            if len(data)>0:
                break
            data = self.ser.readline()
        # print data[1:-1]
        return data[1:-1]

    def read(self,times):
        data = self.ser.readline()
        for i in range(times):
            if len(data)>0:
                break
            data = self.ser.readline()
        if len(data)>0:
            print data[1:-1]
            return data[1:-1]
        else :
            return ''

    def tryConnect(self):
        while True:
            self.write('Connect')
            if self.read(10000000) == 'OK':
                break
if __name__ == '__main__':
    pinA_DE = 7
    pinA_RE = 11

    GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering

    # set these pins to output
    GPIO.setup(pinA_DE, GPIO.OUT)       ## Set pin 7 to OUTPUT
    GPIO.setup(pinA_RE, GPIO.OUT)



    # set b_RE = 0. b_DE = 1
    GPIO.output(pinA_RE, GPIO.HIGH)
    GPIO.output(pinA_DE, GPIO.HIGH)
    a = GateWay485(13,15)
    
            
    # 
    a.tryConnect()
    print 'HEHE'
    