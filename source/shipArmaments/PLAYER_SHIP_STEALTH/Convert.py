def weaponConvert():
	xmlLines = []
	f = open('VanillaWeapons.txt', 'r')
	for line in f:
		lineSplit = line.replace("\n", "").split('|')
		xmlLines.append('\t\t<weapon')
		if 'ST' in lineSplit or 'ST\n' in lineSplit:
			xmlLines[-1] += ' start="true"'
		if 'DLC' in lineSplit:
			xmlLines[-1] += ' rarity="' + lineSplit[2][-1] + '"'
		else:
			xmlLines[-1] += ' rarity="' + lineSplit[1][-1] + '"'
		xmlLines[-1] += '>' + lineSplit[0] + '</weapon>'
		print(xmlLines[-1])
	f.close()
	
def droneConvert():
	xmlLines = []
	f = open('VanillaDrones.txt', 'r')
	for line in f:
		lineSplit = line.replace("\n", "").split('|')
		xmlLines.append('\t\t<drone')
		if 'ST' in lineSplit or 'ST\n' in lineSplit:
			xmlLines[-1] += ' start="true"'
		if 'DLC' in lineSplit:
			xmlLines[-1] += ' rarity="' + lineSplit[2][-1] + '"'
		else:
			xmlLines[-1] += ' rarity="' + lineSplit[1][-1] + '"'
		xmlLines[-1] += '>' + lineSplit[0] + '</drone>'
		print(xmlLines[-1])
	f.close()
	
def augmentConvert():
	xmlLine = '\t<augList countRatio="'
	f = open('augCount.txt', 'r')
	for line in f:
		xmlLine += line.replace("\n", "") + '|'
	xmlLine = xmlLine[:-1] + '">'
	print(xmlLine)
	f.close()
	
	xmlLines = []
	f = open('VanillaAug.txt', 'r')
	for line in f:
		lineSplit = line.replace("\n", "").split('|')
		xmlLines.append('\t\t<augment')
		if 'ST' in lineSplit or 'ST\n' in lineSplit:
			xmlLines[-1] += ' start="true"'
		if 'DLC' in lineSplit:
			xmlLines[-1] += ' rarity="' + lineSplit[2][-1] + '"'
		else:
			xmlLines[-1] += ' rarity="' + lineSplit[1][-1] + '"'
		xmlLines[-1] += '>' + lineSplit[0] + '</augment>'
		print(xmlLines[-1])
	f.close()
	
def artilleryConvert():
	xmlLines = []
	f = open('VanillaArtillery.txt', 'r')
	for line in f:
		xmlLines.append('\t\t<artillery>' + line.replace("\n", "") + '</artillery>')
		print(xmlLines[-1])
	f.close()
	
def reactorConvert():
	xmlLine = '\t\t<reactorCount levelRatio="'
	f = open('reactorCount.txt', 'r')
	for line in f:
		xmlLine += line.replace("\n", "") + '|'
	xmlLine = xmlLine[:-1] + '"/>'
	print(xmlLine)
	f.close()
	
def systemConvert():
	xmlLine = '\t<systemsList countRatio="'
	f = open('systemCount.txt', 'r')
	for line in f:
		xmlLine += line.replace("\n", "") + '|'
	xmlLine = xmlLine[:-1] + '">'
	print(xmlLine)
	f.close()
	
	systemChances = {}
	f = open('VanillaSystems.txt')
	system = ''
	name = True
	for line in f:
		if name is True:
			system = line.replace("\n", "")
		elif name is False:
			systemChances[system] = line.replace("\n", "")
		name = not name
	f.close()
	
	xmlLines = []
	f = open('systemLevels.txt', 'r')
	name = True
	system = ''
	for line in f:
		if name is True:
			system = line.replace("\n", "")
		elif name is False:
			levels = []
			xmlLines.append('\t\t<system chance="' + systemChances[system] + '" levelRatio="')
			for x in line.replace("\n", ""):
				levels.append(int(x))
			for x in range(1, max(levels) + 1):
				xmlLines[-1] += str(levels.count(x)) + '|'
			xmlLines[-1] = xmlLines[-1][:-1] + '">' + system + '</system>'
			print(xmlLines[-1])
		
		name = not name
		
	f.close()

def crewConvert():
	xmlLines = []
	f = open('VanillaCrew.txt', 'r')
	for index, line in enumerate(f):
		if index == 0:
			levels = []
			xmlLines.append('\t<crewList countRatio="')
			for x in line[7:].replace("\n", ""):
				levels.append(int(x))
			for x in range(1, max(levels) + 1):
				xmlLines[-1] += str(levels.count(x)) + '|'
			xmlLines[-1] = xmlLines[-1][:-1] + '">'
			print(xmlLines[-1])
		else:
			lineSplit = line.replace("\n", "").split('|')
			xmlLines.append('\t\t<crew')
			if 'ST' in lineSplit or 'ST\n' in lineSplit:
				xmlLines[-1] += ' min="1"'
			elif 'DLC' in lineSplit:
				xmlLines[-1] += ' rarity="' + lineSplit[2][-1] + '"'
			else:
				xmlLines[-1] += ' rarity="' + lineSplit[1][-1] + '"'
			xmlLines[-1] += '>' + lineSplit[0] + '</crew>'
			print(xmlLines[-1])
	f.close()

print('''<shipArmament name="PLAYER_SHIP_ANAEROBIC">
	<!-- One item with 'start = "true"' is guaranteed to be selected, ensuring the ship is at least useable -->
	<weaponsList>''')
weaponConvert()
print('''	</weaponsList>
	<dronesList>''')
droneConvert()
print('''	</dronesList>
	<!-- Count ratio determined how many augments there will be, with the zero-based index of each number determining how many augments -->''')
augmentConvert()
print('''	</augList>
	
	<artilleryList>''')
artilleryConvert()
print('''	</artilleryList>
	
	<!-- countRatio is the ratio of how likely each number of crew is (i.e. for below 0% for 1 crew, 20% for 2, 50% for 3 and 30% for 4) Index determines # of crew -->''')
crewConvert()
print('''	</crewList>
	
	<!-- includes subsystems, 'chance' unlike rarity is percentage based. Index determined system count and levels for countRato and levelRatio respectively. Index is not zero-based for either -->''')
systemConvert()
print('''	</systemsList>
	<!-- this is zero-based -->''')
reactorConvert()
print('</shipArmament>')
input()