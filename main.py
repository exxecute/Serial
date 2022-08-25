import serial
import os
import Flags as Flag
import defs as Def

ser = serial.Serial()
ser.bytesize = serial.EIGHTBITS
ser.stopbits = serial.STOPBITS_ONE
ser.baudrate = 115200
ser.rtscts = False
ser.dsrdtr = False
ser.timeout = 1.0
ser.write_timeout= 1.0

def Init_Serial():
	while(Flag.Init== False):
		print('''
			Enter COM port to close (ex COM8)
			''')
		Enter= input(Def.EnterString)
		if(Enter[0: 3]== "COM"):
			ser.port = Enter
			try:
				ser.open()
			except:
				print('Serial port is closed try again')
			else:
				Flag.Init= True
		elif(Enter== Def.ExitCommand1 or Enter== Def.ExitCommand2 or Enter== Def.ExitCommand3 or Enter== Def.ExitCommand4):
			print('')
			break
		else:
			print('Failed enter, try again')

# def Check_Ports():
# 	Enter= input('enter amount of ports')
# 	for i in range(Enter):
# 		ser.port= 'COM' + str(Enter)

def Options():
	clear()
	print(Def.OptionsList)
	Enter= input(Def.EnterString)
	if(Enter== Def.ColumnsCommand):
		print('		Enter num of columns')
		Enter== input(Def.EnterString)
		Flag.Columns= int(Enter)
	elif(Enter== Def.FormatCommand):
		print(Def.FormatList)
		Enter== input(Def.EnterString)
		Flag.NumFormat= int(Enter)

def Read():
	print('to stop conversation use ^C')
	Flag.Read= True
	while Flag.Read:
		try:
			data= ser.readline(1)
		except:
			Flag.Read= False
			ser.close()
			try:
				ser.open()
			except:
				Flag.Init= False
			else:
				break
		else:
			if(data!= b''):
				DataLine= ''
				for i in data:
					print(i)

def Close_Port():
	Flag.Close= True
	while Flag.Close:
		print('''
			Enter COM port to close (ex COM8)
			''')
		Enter= input(Def.EnterString)
		if(Enter[0: 3]== "COM"):
			ser.port = Enter
			try:
				ser.close()
			except:
				print('Serial port is closed try again')
			else:
				Flag.Close= False
				Flag.Init= False
		elif(Enter== Def.ExitCommand1 or Enter== Def.ExitCommand2 or Enter== Def.ExitCommand3 or Enter== Def.ExitCommand4):
			print('')
			break
		else:
			print('Failed enter, try again')


if __name__ == '__main__':
	global clear
	if(os.name== 'nt'):
		clear = lambda: os.system('cls')
	else:
		clear = lambda: os.system('clear')
	while(True):
		clear()
		print('''
			serial Reader ''' + Def.version)
		if(Flag.Init== True):
			print('port initialised')
		Enter= input(Def.EnterString)
		if(Enter== Def.HelpCommand1 or Enter== Def.HelpCommand2 or Enter== Def.HelpCommand3 or Enter== Def.HelpCommand4):
			clear()
			print(Def.HelpList)
			Enter= input('')
		elif(Enter== Def.InitCommand1 or Enter== Def.InitCommand2 or Enter== Def.InitCommand3 or Enter== Def.InitCommand4):
			Init_Serial()
		elif(Enter== Def.OptionCommand1 or Enter== Def.OptionCommand2 or Enter== Def.OptionCommand3 or Enter== Def.OptionCommand4):
			Options()
		elif(Enter== Def.ReadCommand1 or Enter== Def.ReadCommand2 or Enter== Def.ReadCommand3 or Enter== Def.ReadCommand4):
			if(Flag.Init== True):
				Read()
			else:
				print('u have to init ur port :)')
				Enter= input('')	
		elif(Enter== Def.CloseCommand1 or Enter== Def.CloseCommand2 or Enter== Def.CloseCommand3 or Enter== Def.CloseCommand4):
			Close_Port()
		elif(Enter== Def.ExitCommand1 or Enter== Def.ExitCommand2 or Enter== Def.ExitCommand3 or Enter== Def.ExitCommand4):
			break