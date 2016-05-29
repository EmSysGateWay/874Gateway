# 全双工485 模块

## 模块说明
本网关用于485通信的模块基于MAX485的芯片，其引脚图和两块芯片的连线电路图如下所示：
![485连线图](http://7xljx0.com1.z0.glb.clouddn.com/Picture1.png?imageView/2/w/619/q/90)

![MAX485各个引脚含义](http://7xljx0.com1.z0.glb.clouddn.com/Picture2.png?imageView/2/w/619/q/90)

其中，**发送数据时**，RE,DE均需置于**高电平**，**接收数据时**，RE,DE均需置于**低电平**。

不难看出，连接485模块需要用到树莓派的UCC,GND,TX,RX,两个GPIO共六个输入输出引脚。

## 连接方式
最终，我们使用如下图示的方式连接：

![MAX485各个引脚含义](http://7xljx0.com1.z0.glb.clouddn.com/%E6%96%B0%E5%BB%BA%E5%A4%87%E5%BF%98%E5%BD%95.png?imageView/2/w/619/q/90)

## 协议
### 数据传输
我们使用两对485转ttl模块，用网关端的gpio控制使能，来达到全双关。
### 网关
1. 初始启动时，设置gpio，使得网关传感器端的数据能正常发送
2. 此后的每次发送和普通全双关串口发送行为一致

### 传感器
1. 传感器只需等待网关初始完成后，就可以和使用普通串口一样使用485模块了。

## 模块介绍
### GateWay485 && Sensor485
`__init__(self,pin_DE, pin_RE)`：构造函数，其中pin_DE表示DE所对应的树莓派引脚，pinRE同理

`write(self,str)`:向串口写数据，str为写入字符串，无返回

`readline(self)`:从串口读数据

`read(self,len)`:从串口读取指定长度的数据

## 实现细节
### GPIO的控制
我们选用的是python的RPi.GPIO库，首先设置GPIO的模式为面板模式（即通过引脚对应的编号来选择控制的引脚）：
[引脚编号](http://zhidx.com/p/60.html)

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


 