from SerialPy import CSerial
import Defines as Def

class CMenu(object):

	def __init__(self):
		self.__version__ = 'v0.2 cmd'
	
	def MainMenu(self):
		while True:
			print(Def.Tabs + self.__version__)
			if Serial.GetPortStatus():
				print('Port ' + Serial.GetPortName() + ' open')
			Enter = input(Def.EnterString)	
			if(Enter == Def.HelpCommand1 or Enter == Def.HelpCommand2 or Enter == Def.HelpCommand3 or Enter == Def.HelpCommand4):
				print(Def.HelpList)
			elif(Enter == Def.InitCommand1 or Enter == Def.InitCommand2 or Enter == Def.InitCommand3 or Enter == Def.InitCommand4):
				self.OpenPort()
			elif(Enter == Def.OptionCommand1 or Enter == Def.OptionCommand2 or Enter == Def.OptionCommand3 or Enter == Def.OptionCommand4):
				self.Options()
			elif(Enter == Def.ReadCommand1 or Enter == Def.ReadCommand2 or Enter == Def.ReadCommand3 or Enter == Def.ReadCommand4):
				self.Read()
			elif(Enter == Def.CloseCommand1 or Enter == Def.CloseCommand2 or Enter == Def.CloseCommand3 or Enter == Def.CloseCommand4):
				self.Close()
			elif(Enter == Def.ExitCommand1 or Enter == Def.ExitCommand2 or Enter == Def.ExitCommand3 or Enter == Def.ExitCommand4):
				break
			elif(Enter == Def.FindCommand1 or Enter == Def.FindCommand2 or Enter == Def.FindCommand3 or Enter == Def.FindCommand4):
				self.CheckPorts()

	def CheckPorts(self):
		if Serial.GetPortStatus():
			Serial.ClosePort()
		PortsList = ''
		Cycle = 0
		Line = True

		for i in range(100):
			NowPort = 'COM' + str(i)
			if Serial.CheckPort(NowPort):
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

	def Close(self):
		if Serial.GetPortStatus():
			Serial.ClosePort()

	def OpenPort(self):
		LoopFlag = True
		while LoopFlag:
			Enter = input('enter port "COM8"/"/dev/ttyUSB*": ')
			if(Enter[0 : 3] == "COM" or Enter[0 : 11] == "/dev/ttyUSB"):
				Status = Serial.OpenPort(Enter)
				if Status:
					LoopFlag = False
			else:
				print('Not properly enter, trt again')

	def Options(self):
		LoopFlag = True
		while LoopFlag:
			print(Def.OptionsList)
			print('Columns = ', Serial.GetColumns(), 
		    '\nFormat Data = ', Serial.GetNumFormat(),
		    '\nByte Size = ', Serial.GetByteSize(), '\n')

			Enter = input(Def.EnterString)
			if(Enter == Def.ColumnsCommand):
				print(Def.Tabs + 'Enter num of columns')
				Enter = input(Def.EnterString)
				Serial.SetColumns(int(Enter))

			elif(Enter == Def.FormatCommand):
				print(Def.FormatList)
				Enter = input(Def.EnterString)
				Serial.SetNumFormat(int(Enter))

			elif(Enter == Def.BytesizeCommand):
				print(Def.SizeList)
				Enter = input(Def.EnterString)
				Serial.SetByteSize(int(Enter))

			elif(Enter == Def.ExitCommand1 or Enter == Def.ExitCommand2 or 
				 Enter == Def.ExitCommand3 or Enter == Def.ExitCommand4):
				LoopFlag = False

	def Read(self):
		if Serial.GetPortStatus():
			Serial.ReadPort()
		else:
			print('u have to init ur port :)')
			Enter = input('Oki')

if __name__ == '__main__':
	Serial = CSerial()
	Menu = CMenu()
	Menu.MainMenu()