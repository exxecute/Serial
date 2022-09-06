import Defines as Def
import serial

class CSerial(object):

	def __init__(self):
		self.ser = serial.Serial()
		self.ser.bytesize = serial.EIGHTBITS
		self.ser.stopbits = serial.STOPBITS_ONE
		self.ser.baudrate = 115200 
		self.ser.rtscts = False
		self.ser.dsrdtr = False
		self.ser.timeout = None
		self.ser.write_timeout= 1.0

		self.Port = 'Close'
		self.PortIsOpen = False

		self.Columns = 1
		self.NumFormat = Def.NoDec
		self.ByteSize = Def.EightBytes

	def CheckPort(self, Port):
		self.ser.port = Port 
		Answer = True
		try:
			self.ser.open()
		except:
			print(Port + ' fail')
			Answer = False
		else:
			self.ser.close()
			print(Port + ' ok')
		return Answer

	def ClosePort(self):
		self.PortIsOpen = False
		self.ser.close()

	def OpenPort(self, port):
		self.Port = port 

		self.ser.port = self.Port
		try:
			self.ser.open()
		except:
			print('Serial port is closed try again')
		else:
			self.PortIsOpen = True

		return self.PortIsOpen

	def ReadPort(self):
		print('use ^C to stop conversation')
		ReadFlag = True 

		while ReadFlag:
			Cycle = 0
			DataLine = ''

			while(Cycle != self.Columns):
				try:
					ReciveData = self.ser.readline(self.ByteSize)
					Data = 0
					for Num in ReciveData:
						Data = (Data << Def.EightBytesNum) + Num
				except:
					ReadFlag = False
					self.ser.close()
					try:
						self.ser.open()
					except:
						self.PortIsOpen = False
					else:
						break
				else:
					if(self.NumFormat == Def.NoHex):
						DataLine += str(hex(Data)) + '	'

					elif(self.NumFormat == Def.NoDec):
						DataLine += str(Data) + '	'

					elif(self.NumFormat == Def.NoOct):
						DataLine += str(oct(Data)) + '	'

					elif(self.NumFormat == Def.NoBin):
						DataLine += str(bin(Data)) + '	'


					if(Data < Def.MinDataLine):
						DataLine += '	'

				Cycle += 1
			if(DataLine != ''):
				print(DataLine)		

	def GetPortStatus(self):
		return self.PortIsOpen

	def GetPortName(self):
		return self.Port

	def GetColumns(self):
		return self.Columns

	def GetNumFormat(self):
		Answer = ''
		if(self.NumFormat == Def.NoHex):
			Answer = 'Hex'
		elif(self.NumFormat == Def.NoDec):
			Answer = 'Dec'
		elif(self.NumFormat == Def.NoOct):
			Answer = 'Oct'
		elif(self.NumFormat == Def.NoBin):
			Answer = 'Bin'
		return Answer

	def GetByteSize(self):
		Answer = ''
		if(self.ByteSize == Def.EightBytes):
			Answer = 'Eight Byte Size'
		elif(self.ByteSize == Def.SixteenBytes):
			Answer = 'Sixteen Byte Size'
		elif(self.ByteSize == Def.TwentyFourBytes):
			Answer = 'Twenty Four Byte Size'
		elif(self.ByteSize == Def.ThirtyTwoBytes):
			Answer = 'Thirty Two Byte Size'
		return Answer

	def SetColumns(self, Columns):
		if(Columns < 11):
			self.Columns = Columns
		elif(Columns < 1):
			self.Columns = 1
		else:
			print('10 columns - max')
			self.Columns = 10

	def SetNumFormat(self, NumFormat):
		if(0 < NumFormat < 5):
			self.NumFormat = NumFormat

	def SetByteSize(self, ByteSize):
		if(0 < ByteSize < 5):
			self.ByteSize = ByteSize