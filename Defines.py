#num defines
EightBytesNum =				8
MinDataLine =				10000000

#reading format
NoHex = 					1
NoDec = 					2
NoOct = 					3
NoBin = 					4

#strings
EnterString = 'enter: '

#help commands
HelpCommand1 =				'Help'
HelpCommand2 =				'help'
HelpCommand3 =				'H'
HelpCommand4 =				'h'

#init commands
InitCommand1 =				'Init'
InitCommand2 =				'init'
InitCommand3 =				'I'
InitCommand4 =				'i'

#options commands
OptionCommand1 =			'Options'
OptionCommand2 =			'options'
OptionCommand3 =			'O'
OptionCommand4 =			'o'

#commands in options
ColumnsCommand =			'1'
FormatCommand =				'2'
BytesizeCommand =			'3'

#command bytesize
EightBytes =				1
SixteenBytes =				2
TwentyFourBytes =			3
ThirtyTwoBytes =			4

#read commands
ReadCommand1 =				'Read'
ReadCommand2 =				'read'
ReadCommand3 =				'R'
ReadCommand4 =				'r'

#exit commands
ExitCommand1 =				'Exit'
ExitCommand2 =				'exit'
ExitCommand3 =				'E'
ExitCommand4 =				'e'

#close commands
CloseCommand1 =				'Close'
CloseCommand2 =	 			'close'
CloseCommand3 =				'C'
CloseCommand4 =				'c'

#find commands
FindCommand1 =				'Find'
FindCommand2 =				'find'
FindCommand3 =				'F'
FindCommand4 =				'f'

#strings
HelpList = '''
		command list:
		enter: Help/ help/ H/ h
		- to have command list

		enter: Init/ init/ I/ i
		- to init ur port

		enter: Options/ options/ O/ o
		- to set options

		enter: Read/ read/ R/ r
		- to read port

		enter: Close/ close/ C/ c
		- to close port

		enter: Exit/ exit/ E/ e
		- to exit

		enter: Find/ find/ F/ f
		- to find serial port'''

OptionsList = '''
		options:
		1 - to edit num of columns
		2 - to edit num format 
		3 - to edit num size

		e - exit'''

FormatList = '''
		formats:
		1 - hex
		2 - dec
		3 - oct
		4 - bin'''

SizeList = '''
		sizes:
		1 - 8 bytes
		2 - 16 bytes
		3 - 24 bytes
		4 - 32 bytes'''

Tabs = '			'