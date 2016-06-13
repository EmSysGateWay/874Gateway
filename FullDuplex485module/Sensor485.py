import time                     ## Import 'time' library (for 'sleep')
import serial
import json
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
            port='/dev/ttyAMA0',
            baudrate = 115200,
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
        return data[1:-1]
    def readline(self):
        data = self.ser.readline()
        return data[1:-1]

class Transmit:
    def __init__(self):
        self.Sensor485 = Sensor485()
    
    def requestAuth(self):
        dic = dict()
        dic['RequestType']='auth'
        dic['DiviceId']='869'
        self.Sensor485.write(json.dumps(dic))
    
    def uploadLogin(self,time,id,legal,logInOrOut):
        dic = dict()
        dic['RequestType']='upload'
        dic['DiviceId']='869'
        dic['Data']={'time':time,'id':id,'legal':legal,'logInOrOut':logInOrOut}
        self.Sensor485.write(json.dumps(dic))
    
    def read(self){
        return self.Sensor485.readline()
    }
            
if __name__ == '__main__':
    a = Sensor485()

    print 'HEHE'