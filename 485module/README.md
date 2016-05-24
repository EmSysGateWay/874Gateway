# 485 模块

## 连接方式
本网关用于485通信的模块基于MAX485的芯片，其引脚图和两块芯片的连线电路图如下所示：
![485连线图](http://7xljx0.com1.z0.glb.clouddn.com/Picture1.png?imageView/2/w/619/q/90)

![MAX485各个引脚含义](http://7xljx0.com1.z0.glb.clouddn.com/Picture2.png?imageView/2/w/619/q/90)

其中，**发送数据时**，RE,DE均需置于**高电平**，**接收数据时**，RE,DE均需置于**低电平**。此外，为了使A，B线间的电压差稳定，需要在连线间接入电阻。

不难看出，连接485模块需要用到树莓派的UCC,GND,TX,RX,两个GPIO共六个输入输出引脚。

## 协议
### 数据传输
数据以字符串的方式传递。所有字符串均以`'#'+字符串+'\n'`形式发送，接收时也会相应去除首尾的标记。
### 网关
1. 初始启动时，不断发送字符串`'Connect'`给串口，直到从串口收到字符串`'OK'`，表示连接成功
2. 此后，每一次发送信息都必须要在收取到对方信息后进行

### 传感器
1. 初始启动时，须等待接收字符串`'Connect'`，接收到后向串口发送字符串`'OK'`
2. 此后，每一次发送信息都必须要在收取到对方信息后进行

## 模块介绍
### GateWay485 && Sensor485
`__init__(self,pin_DE, pin_RE)`：构造函数，其中pin_DE表示DE所对应的树莓派引脚，pinRE同理

`write(self,str)`:向串口写数据，str为写入字符串，无返回

`read(self)`:向串口读数据，返回为读取的数据。如果；一直没读到，就会一直读

`read(self,times)`:向串口读数据，times表示最多读取的次数，具体可以看代码，返回为读取的数据。

`tryConnect(self)`:尝试连接，连接成功函数结束，如果不成功则一直等待

## 实现细节
### GPIO的控制
我们选用的是python的RPi.GPIO库，首先设置为引脚的编号为面板模式：

	GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering

然后指定输出的引脚：

	# set these pins to output
	GPIO.setup(pinA_DE, GPIO.OUT)       ## Set pin 7 to OUTPUT
	GPIO.setup(pinA_RE, GPIO.OUT)

然后就可以控制GPIO输出高低电平：

	# set b_RE = 0. b_DE = 1
	GPIO.output(pinA_RE, GPIO.HIGH)
	GPIO.output(pinA_DE, GPIO.HIGH)

### 串口收发
这里我选用的是python的serial模块

收的部分：

	#!/usr/bin/env python     
	import time
	import serial
	      
	ser = serial.Serial( 
	      port='/dev/ttyAMA0',	#set port
	      baudrate = 9600,		#ser baud rate
	      parity=serial.PARITY_NONE,
	      stopbits=serial.STOPBITS_ONE,
	      bytesize=serial.EIGHTBITS,
	      timeout=1
	     )
	
	print "Whether the serial is open:", ser.isOpen()
	           
	while 1:
	   data = ser.readline()
	   if len(data)>0:
	      print data
      
发的部分：

	#!/usr/bin/env python     
	import time
	import serial
	      
	ser = serial.Serial( 
	      port='/dev/ttyAMA0',	#set port
	      baudrate = 9600,		#ser baud rate
	      parity=serial.PARITY_NONE,
	      stopbits=serial.STOPBITS_ONE,
	      bytesize=serial.EIGHTBITS,
	      timeout=1
	     )
	
	print "Whether the serial is open:", ser.isOpen()
	
	data = "abcdefghigklmnopqrstuvwxyz0123456789\n"
	
	counter=0            
	while 1:
	   ser.write(data)
	   #ser.write('Write counter: %d \n\r'%(counter))	#write
	   time.sleep(1)
	   counter += 1

	
其他具体实现可以看代码！

当然其实如果传感器方有性能需求，只要遵守协议，传感器方用C重写Sensor485模块也是没问题的。
 