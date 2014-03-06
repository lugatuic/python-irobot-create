import serial

class Robot:
	def __init__(self, port, baud_rate = 57600):
		self.port = port
		self.baud_rate = 57600 #Eventually this will be editable

		self.conn = serial.Serial(self.port, baudrate=self.baud_rate, timeout=0.5)

	#wrapper for serial send function
	def send(self, num):
		if self.conn:
			self.conn.send(bytes(num, encoding='Latin-1' ))
		else:
			raise Exception("No serial connection.")

	def sendAll(self, nums):
		for n in nums:
			self.send(n)

	#Wrapper for serial read function
	def read(self, bys):
		if self.conn:
			return self.conn.read(bys)
		else:
			raise Exception("No serial connection.")