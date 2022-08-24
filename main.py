import serial

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
	Flag_Init= False
	while(Flag_Init== False):
		print('')
		print('Enter COM port (ex COM8)')
		Enter= input("enter: ")
		if(Enter[0: 3]== "COM"):
			ser.port = EnterCom
			if(ser.isOpen()):
				ser.open()
				Flag_Init= True
			else:
				print('Serial port is closed try again')
		elif(Enter== 'Exit' or Enter== 'exit' or Enter== 'E' or Enter== 'e'):
			print('')
			break
		else:
			print('Failed enter, try again')

# def Check_Ports():
# 	Enter= input('enter amount of ports')
# 	for i in range(Enter):
# 		ser.port= 'COM' + str(Enter)


if __name__ == '__main__':
	while(True):
		print('serial Reader ' + version)
		Enter= input('enter: ')
		if(Enter== 'help' or Enter== 'h' or Enter== 'Help' or Enter== 'H'):
			print('')
			print('command list')
			print('enter: Help/ help/ H/ h')
			print('to have command list')
			print('')
		elif(Enter== 'Init' or Enter== 'init' or Enter== 'I' or Enter== 'i'):
			Init_Serial()
		elif(Enter== 'Exit' or Enter== 'exit' or Enter== 'E' or Enter== 'e'):
			break