import time                     ## Import 'time' library (for 'sleep')
import serial
# A : Receive
# DE : 7
# RE : 11

# B : Sent
# DE 13
# RE 15

class Sensor485:
    # pin_DE : DE pin number of RPi
    # pin_RE : RE pin number of RPi
    def __init__(self):

        # connect to serial
        self.ser = serial.Serial(
            port='/dev/tty.SLAB_USBtoUART',
            baudrate = 9600,
			parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)
            
    # write to serial port
    # str: the data to write
    def write(self,str):
        writeStr = str.replace('\r', '') 
        writeStr = writeStr.replace('\n', '') 
        writeStr = '#'+ writeStr + '\n'
        self.ser.write(writeStr)
    
    # read from serial port
    # return data from serial port
    def read(self):
        data = self.ser.readline()
        print data[1:-1]
        return data[1:-1]
        
if __name__ == '__main__':
    a = Sensor485()
    while True:
        a.write('Hello GateWay!')
        time.sleep(5)
    print 'HEHE'