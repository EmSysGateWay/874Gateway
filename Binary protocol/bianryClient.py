import socket
import struct

class BinaryClient:
	ACK = 0
	NACK = 1
	LOGIN = 2
	REPORT = 3
	CONTROL = 4
	LOGOUT = 5

	def __init__(self,device_id,device_key,device_fmt,server_addr,server_port):
		self.device_id = device_id
		self.device_key = device_key
		self.device_fmt = device_fmt
		self.server_addr = server_addr
		self.server_port = server_port
		address = (server_addr, server_port)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
		self.socket.connect(address)		


	def login(self):
		packet = struct.pack("<bi32s", self.LOGIN, self.device_id, self.device_key)
		self.socket.send(packet)
		packet = self.socket.recv(1)
		if(self.is_ack(packet)):
			print("login success")
		else:
			print("login failed")
		return self.control_receive()


	def is_ack(self,packet):
		data = struct.unpack("<b",packet)
		if(data[0] == self.ACK):
			return 1
		else:
			return 0

	def logout(self):
		packet = struct.pack("<b", self.LOGOUT)
		self.socket.send(packet)
		print("logged out")
		self.socket.close()

	def control_receive(self):
		packet_head = self.socket.recv(5)
		packet_type,get_id = struct.unpack("<bL",packet_head)		
		if(packet_type != self.CONTROL or get_id != self.device_id):
			print "wrong packet type and device id"
		
		packet_data = self.socket.recv(struct.calcsize(self.device_fmt))
		control_data = struct.unpack(self.device_fmt, packet_data)
		return control_data
		

	def report(self,data):
		packet = struct.pack("<bLL", self.REPORT, self.device_id,0)
		self.socket.send(packet)
		self.socket.send(data)
		packet = self.socket.recv(1)
		if(self.is_ack(packet)):
			print("report success")
		else:
			print("report failed")
		
		return self.control_receive()


keys = {18: "ed78e2aa4799a0122eec4a31aa0ddcb1"}
fmt = {18: "<i8sf"}

def main():
	client = BinaryClient(18,"ed78e2aa4799a0122eec4a31aa0ddcb1","<i8sf","nya.fatmou.se",10659)
	control_data = client.login()
	print control_data
	
	report_data = struct.pack("<4s","1234")
	control_data = client.report(report_data)
	print control_data

	client.logout()
		
if __name__ == '__main__':
    main()


