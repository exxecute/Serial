import serial
import os
import Flags as Flag
import defs as Def

version= 'v0.1'

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
		print('')
		print('Enter COM port to init (ex COM8)')
		Enter= input("enter: ")
		if(Enter[0: 3]== "COM"):
			ser.port = Enter
			try:
				ser.open()
			except:
				print('Serial port is closed try again')
			else:
				Flag.Init= True
		elif(Enter== 'Exit' or Enter== 'exit' or Enter== 'E' or Enter== 'e'):
			print('')
			break
		else:
			print('Failed enter, try again')

# def Check_Ports():
# 	Enter= input('enter amount of ports')
# 	for i in range(Enter):
# 		ser.port= 'COM' + str(Enter)

def Options():
	print('')
	print('options')

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
				ser.open()
				break
		else:
			if(data!= b''):
				for i in data:
					print(i)

def Close_Port():
	Flag.Close= True
	while Flag.Close:
		print('')
		print('Enter COM port to close (ex COM8)')
		Enter= input("enter: ")
		if(Enter[0: 3]== "COM"):
			ser.port = Enter
			try:
				ser.close()
			except:
				print('Serial port is closed try again')
			else:
				Flag.Close= False
				Flag.Init= False
		elif(Enter== 'Exit' or Enter== 'exit' or Enter== 'E' or Enter== 'e'):
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
		print('serial Reader ' + version)
		if(Flag.Init== True):
			print('port initialised')
		Enter= input('enter: ')
		if(Enter== 'help' or Enter== 'h' or Enter== 'Help' or Enter== 'H'):
			clear()
			print('command list:')
			print('enter: Help/ help/ H/ h')
			print('- to have command list')
			print('')
			print('enter: Init/ init/ I/ i')
			print('- to init ur port')
			print('')
			print('enter: Options/ options/ O/ o')
			print('- to set options')
			print('')
			print('enter: Read/ read/ R/ r')
			print('- to read port')
			print('')
			print('enter: Close/ close/ C/ c')
			print('- to close port')
			Enter= input('')
		elif(Enter== 'Init' or Enter== 'init' or Enter== 'I' or Enter== 'i'):
			Init_Serial()
		elif(Enter== 'Options' or Enter== 'options' or Enter== 'O' or Enter== 'o'):
			Options()
		elif(Enter== 'Read' or Enter== 'read' or Enter== 'R' or Enter== 'r'):
			if(Flag.Init== True):
				Read()
			else:
				print('u have to init ur port :)')
				Enter= input('')	
		elif(Enter== 'Close' or Enter== 'close' or Enter== 'C' or Enter== 'c'):
			Close_Port()
		elif(Enter== 'Exit' or Enter== 'exit' or Enter== 'E' or Enter== 'e'):
			break