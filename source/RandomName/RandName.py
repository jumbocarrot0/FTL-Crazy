from random import *

readPhonetics = open('Phonetics.txt', 'r')
phonetics = readPhonetics.readlines(10000000)
readPhonetics.close()

for syllables in range(0, len(phonetics)):
	if '\n' in phonetics[syllables]:
		phonetics[syllables] = phonetics[syllables][:-1]
		

while 0 == 0:
	command = input('enter a command: ').lower()
	if command == 'generate':
		print('command received')
		phoneticLength = randint(3, 6)
		name = 'Name: '
		for repeats in range(0, phoneticLength):
			randomNum = randint(0, len(phonetics))
			name += str(phonetics[randomNum])
			
		print(name + '\n')
		
	elif command == 'phonetics':
		print('command received')
		print(phonetics)
		
	elif command == 'help':
		print('''	Commands:
generate: create a name based off the given phonetics
phonetics: show the list of phonetics
help: shows a list of commands.''')
		
	else:
		print('Invalid Command')