#!/usr/bin/env python     
"""
@brief Receive the data from the  sensors
	And parse the data according to the established protocol
@Author wang_kejie@foxmail.com
@Date 2016/5/28
@Protocol Description:
struct generalUnpacket
{
	unsigned char start;	//1 byte
	unsigned char length;	//1 byte
	unsigned short dest;	//2 bytes
	unsigned short src;		//2 bytes
	unsigned char data[length];
};

Group 871/882
struct unpacket
{
	unsigned char start;	//1 byte
	unsigned char length;	//1 byte
	unsigned short dest;	//2 bytes
	unsigned short src;		//2 bytes
	unsigned int pm25;		//4 bytes
	unsigned int HCHO;		//4 bytes formaldehyde concentration
	unsigned int temp;		//4 bytes temperature
	unsigned int humidity;	//4 bytes humidity
	unsigned int CO;		//4 bytes carbon monoxide
	unsigned char rank;
};

Group 876
struct unpacket
{
	unsigned char start;	//1 byte
	unsigned char length;	//1 byte
	unsigned short dest;	//2 bytes
	unsigned short src;		//2 bytes
	float longitude;		//4 bytes
	unsigned char eORw;		//1 byte
	float latitude;			//4 bytes
	unsigned char nORs;		//1 bytes
	unsigned int temp;		//4 bytes
	unsigned int humidity;	//4 bytes
};
"""
import httpclient
import struct
import serial
import post

DATALEN871_882 = 21
DATALEN876 = 18

MYDEVICEID = 874
DEVICEID871 = 871
DEVICEID882 = 882
DEVICEID876 = 876


SERVERDEVICEID876 = 40
SERVERDEVICEID882 = 38
SERVERDEVICEID871 = 34


ser = serial.Serial( 
      port='/dev/ttyUSB0',	#set port
      baudrate = 38400,		#ser baud rate
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS,
      timeout=None
     )
auth_id = 15
auth_key = "d7fe7b0a3c1dbde58e251d3aafc4954f"
client = httpclient.HTTPClient(auth_id, auth_key, "nya.fatmou.se")


while (1):
	start, = struct.unpack("B", ser.read(1))
	#print int(start)
	if(start != 0xFD):
		#print "wrong start"
		continue
	#get the packet information such as length, souce, destination
	DataInfo = ser.read(5)
	length, dest, src = struct.unpack("<B2H", DataInfo)
	print "length=",length, "dest=",dest, "src=",src
	#the destination is not this device
	if(dest != MYDEVICEID):
		print "Unmatched destination"
		continue

	if(src == DEVICEID871 or src == DEVICEID882):
		if(length != DATALEN871_882):
			print "Get a unpacket from Group %d with unmatched length" %(src)
		data = ser.read(length)
		pm25, HCHO, temp, humidity, CO, rank = struct.unpack("<5IB", data)

		print "-----------------------------------------------"
		print "From Device ", src
		print "PM2.5: ", pm25
		print "HCHO concentration: ", HCHO
		print "temperature: ", temp
		print "humidity: ", humidity
		print "CO: ", CO
		print "rank: ", rank
		print "-----------------------------------------------\n\n"

		sendData882 = {
			"pm": pm25,
			"HCHO": HCHO,
			"Temperature": temp,
			"Humidity": humidity,
			"CO": CO,
			"Rank": rank
		}
		sendData871 = {
			"pm25": pm25,
			"HCHO": HCHO,
			"Temperature": temp,
			"Humidity": humidity,
			"CO": CO,
			"DetectPeople": rank		
		}
		#send to the server
		if(src == DEVICEID871):
			client.report(SERVERDEVICEID871, sendData871)
		elif(src == DEVICEID882):
			client.report(SERVERDEVICEID882, sendData882)

	elif(src == DEVICEID876):
		if(length != DATALEN876):
			print "Get a unpacket from Group %d with unmatched length" %(src)
		data = ser.read(length)
		longitude, eORw, latitude, nORs, temp, humidity = struct.unpack("<fBfBII", data)

		print "-----------------------------------------------"
		print "From Device ", src
		print "longitude: ", longitude
		print "east or west: ", eORw
		print "latitude: ", latitude
		print "north or south: ", nORs
		print "temperature: ", temp
		print "humidity: ", humidity
		print "-----------------------------------------------\n\n"
		if(eORw == 0):
			eORwStr = "east"
		else:
			eORwStr = "west"
		if(nORs == 2):
			nORsStr = "south"
		else:
			nORsStr = "north"
		sendData876 = {
			"longitude": longitude,
			"ew": eORwStr,
			"latitude": latitude,
			"ns": nORsStr,
			"temp": temp,
			"humi": humidity
		}
		#send to the server
		client.report(SERVERDEVICEID876, sendData876)

	else:
		print "Get a unpack from unknown source"