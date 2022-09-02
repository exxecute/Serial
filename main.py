import Flags as Flag
import defs as Def
import serial
import os

__version__ = 'v0.15 cmd'


ser = serial.Serial()
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.baudrate = 115200 
ser.rtscts = False
ser.dsrdtr = False
ser.timeout = None
ser.write_timeout= 1.0

# return string options
def StringOption(NumCommand, Command):
	Answer = ''

	# Size Commands
	if(NumCommand == Def.BytesizeCommand):
		if(Command == Def.EightBytes):
			Answer = 'Eight Byte Size'
		elif(Command == Def.SixteenBytes):
			Answer = 'Sixteen Byte Size'
		elif(Command == Def.TwentyFourBytes):
			Answer = 'Twenty Four Byte Size'
		elif(Command == Def.ThirtyTwoBytes):
			Answer = 'Thirty Two Byte Size'

	# Format Commands
	if(NumCommand == Def.FormatCommand):
		if(Command == Def.NoHex):
			Answer = 'Hex'
		elif(Command == Def.NoDec):
			Answer = 'Dec'
		elif(Command == Def.NoOct):
			Answer = 'Oct'
		elif(Command == Def.NoBin):
			Answer = 'Bin'

	return Answer

# main command to open serial port
def Init_Serial():
	while(Flag.Init == False):
		print('''
			Enter COM port to close (ex COM8)
			''')

		Enter = input(Def.EnterString)
		if(Enter[0 : 3] == "COM"):
			ser.port = Enter
			try:
				ser.open()
			except:
				print('Serial port is closed try again')
			else:
				Flag.Init = True
		elif(Enter == Def.ExitCommand1 or Enter == Def.ExitCommand2 or Enter == Def.ExitCommand3 or Enter == Def.ExitCommand4):
			print('')
			break
		else:
			print('Failed enter, try again')

# main command to find port that u can open
def Check_Ports():
	if Flag.Init:
		ser.close()
		print(1)
	PortsList = ''
	Cycle = 0
	Line = True

	for i in range(100):
		NowPort = 'COM' + str(i)
		ser.port = NowPort
		try:
			ser.open()
		except:
			print(NowPort + ' fail')
		else:
			ser.close()
			print(NowPort + ' ok')
			PortsList += NowPort + ' '
			Cycle += 1
			if(Cycle == 15):
				Line = False
				print('u can use: ' + PortsList)
				PortsList = ''
	if Line:
		print('u can use: ' + PortsList)
	else:
		print(PortsList)

	Enter = input('ok')

# main command to edit formats columns etc
def Options():
	EnterLoop = True
	while EnterLoop:
		clear()
		print(Def.OptionsList)

		print('Columns = ', Flag.Columns, 
		    '\nFormat Data = ', StringOption(Def.FormatCommand, Flag.NumFormat),
		    '\nByte Size = ', StringOption(Def.BytesizeCommand, Flag.ByteSize))
		print()
		Enter = input(Def.EnterString)

		if(Enter == Def.ColumnsCommand):
			print('		Enter num of columns')
			Enter = input(Def.EnterString)
			Flag.Columns = int(Enter)

		elif(Enter == Def.FormatCommand):
			print(Def.FormatList)
			Enter = input(Def.EnterString)
			Flag.NumFormat = int(Enter)

		elif(Enter == Def.BytesizeCommand):
			print(Def.SizeList)
			Enter = input(Def.EnterString)
			Flag.ByteSize = int(Enter)

		elif(Enter == Def.ExitCommand1 or Enter == Def.ExitCommand2 or 
			 Enter == Def.ExitCommand3 or Enter == Def.ExitCommand4):
			EnterLoop = False

# main command to read port that u open
def Read():
	print('to stop conversation use ^C')
	Flag.Read = True

	while Flag.Read:
		Cycle = 0
		DataLine = ''

		while(Cycle != Flag.Columns):
			try:
				recivedata = ser.readline(Flag.ByteSize)
				data = 0
				for Dec in recivedata:
					data = (data << 8) + Dec
			except:
				Flag.Read = False
				ser.close()
				try:
					ser.open()
				except:
					Flag.Init = False
				else:
					break
			else:

				if  (Flag.NumFormat== Def.NoHex):
					DataLine += str(hex(data)) + '	'
					if(data < 10000000): 
						DataLine += '	'

				elif(Flag.NumFormat== Def.NoDec):
					DataLine += str(data) + '	'
					if(data < 10000000): 
						DataLine += '	'

				elif(Flag.NumFormat== Def.NoOct):
					DataLine += str(oct(data)) + '	'
					if(data < 10000000): 
						DataLine += '	'

				elif(Flag.NumFormat== Def.NoBin):
					DataLine += str(bin(data)) + '	'
					if(data < 10000000): 
						DataLine += '	'

			Cycle += 1
		if(DataLine != ''):
			print(DataLine)

# main command to close any port
def Close_Port():
	Flag.Close = True

	while Flag.Close:
		print('''
			Enter COM port to close (ex COM8)
			''')

		Enter = input(Def.EnterString)
		if(Enter[0 : 3] == "COM"):
			ser.port = Enter
			try:
				ser.close()
			except:
				print('Serial port is closed try again')
			else:
				Flag.Close = False
				Flag.Init = False
		elif(Enter == Def.ExitCommand1 or Enter == Def.ExitCommand2 or Enter == Def.ExitCommand3 or Enter == Def.ExitCommand4):
			print('')
			break
		else:
			print('Failed enter, try again')


if __name__ == '__main__':
	global clear

	if(os.name == 'nt'):
		clear = lambda: os.system('cls')
	else:
		clear = lambda: os.system('clear')

	while(True):
		clear()

		print('''		serial Reader ''' + __version__)

		if(Flag.Init == True):
			print('port initialised')

		Enter = input(Def.EnterString)
		if(Enter == Def.HelpCommand1 or Enter == Def.HelpCommand2 or Enter == Def.HelpCommand3 or Enter == Def.HelpCommand4):
			clear()
			print(Def.HelpList)
			Enter = input('')
		elif(Enter == Def.InitCommand1 or Enter == Def.InitCommand2 or Enter == Def.InitCommand3 or Enter == Def.InitCommand4):
			Init_Serial()
		elif(Enter == Def.OptionCommand1 or Enter == Def.OptionCommand2 or Enter == Def.OptionCommand3 or Enter == Def.OptionCommand4):
			Options()
		elif(Enter == Def.ReadCommand1 or Enter == Def.ReadCommand2 or Enter == Def.ReadCommand3 or Enter == Def.ReadCommand4):
			if(Flag.Init== True):
				Read()
			else:
				print('u have to init ur port :)')
				Enter = input('ok')	
		elif(Enter == Def.CloseCommand1 or Enter == Def.CloseCommand2 or Enter == Def.CloseCommand3 or Enter == Def.CloseCommand4):
			Close_Port()
		elif(Enter == Def.ExitCommand1 or Enter == Def.ExitCommand2 or Enter == Def.ExitCommand3 or Enter == Def.ExitCommand4):
			break
		elif(Enter == Def.FindCommand1 or Enter == Def.FindCommand2 or Enter == Def.FindCommand3 or Enter == Def.FindCommand4):
			Check_Ports()
		# elif(Enter == 'd'):
		# 	debug()
