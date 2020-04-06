fileRead = open('C:/Users/Jumbo/Desktop/FTL Modding/GameData/data/dlcBlueprints.xml')
xml = fileRead.readlines()
fileRead.close()

missileWeapons = []

weapon = False
weaponName = ''

for x in range(0, len(xml)):
	if '</weaponBlueprint>' in xml[x]:
		weapon = False
	if '<weaponBlueprint' in xml[x] and 'name="' in xml[x]:
		weapon = True
		missileWeapons.append(xml[x][xml[x].index('name="')+6:xml[x].index('"', xml[x].index('"')+1)])
	if '<power>' in xml[x] and weapon is True:
		missileWeapons[-1] = missileWeapons[-1] + '|P' + xml[x][xml[x].index('<power>')+7:xml[x].index('<power>')+8]
			
print(missileWeapons)
input()