logo = '''
     _______________   _______________    _____
    |               | |               |  |     |
    |      _________| |____       ____|  |     |
    |     |                |     |       |     |
    |     |______          |     |       |     |
    |            |         |     |       |     |
    |      ______|         |     |       |     |
    |     |                |     |       |     |
    |     |                |     |       |     |________            
    |     |                |     |       |              |
    |_____|                |_____|       |______________|

          _____   _____   _____   _____   _   _
         |  ___| |  _  | |  _  | |___  | | |_| |
         | |___  |    _| |  _  |  __/ /  |_   _|
         |_____| |_|\_\  |_| |_| |_____|   |_|


         A Randomizer for FTL: Faster Than Light
'''

print(logo)



from random import *
import shutil
import os
from sys import maxsize
import xml.etree.ElementTree as ET

def generateRandMod(Mod="Vanilla", balanced=False, modSeed = '', extraEquipmentCheck=False, randShipCheck=True, equipPower=True, equipDamage=True, hyperspace=False):

	if modSeed != '':
		modSeed = modSeed.encode('utf-8')
		seed(int(modSeed.hex(), 16))
		print('Effective Seed: ' + str(int(modSeed.hex(), 16)))
	else:
		modSeed = randrange(maxsize)
		seed(modSeed)
		print('Seed: ' + str(modSeed))
		
	
	print('Shuffling Values')
	
	if balanced is False:
		randomCycleCrew = ['human', 'engi', 'mantis', 'slug', 'rock', 'crystal', 'energy', 'anaerobic']
		if Mod=="CE" or Mod=='Arsenal+':
			randomCycleCrew.append('ghost')
	else:
		randomCycleCrew = []
	shuffle(randomCycleCrew)
	randomCycleCrew.append('debug')
	randomCycleCrew.insert(0, 'debug')
	
	randomCycleTitle = ['bp_MUS_TitleScreen.ogg', 'bp_MUS_MilkyWayEXPLORE.ogg', 'bp_MUS_EngiEXPLORE.ogg', 'bp_MUS_ColonialBATTLE.ogg', 'bp_MUS_LastStand.ogg', 'bp_MUS_ShrikeEXPLORE.ogg', 'bp_MUS_SlugBATTLE.ogg', 'bp_MUS_LostShipBATTLE.ogg']
	if Mod == 'Arsenal+':
		randomCycleTitle += ['bp_MUS_Calm_Explore.ogg', 'bp_MUS_Demiurge.ogg', 'bp_MUS_Incursor.ogg', 'bp_MUS_Infinity_Explore.ogg', 'bp_MUS_NewTerranRepublic_Explore.ogg']
	shuffle(randomCycleTitle)
	randomCycleTitle.append('debug')
	randomCycleTitle.insert(0, 'debug')
	
	randomCycleBossArtillery = ['ARTILLERY_BOSS_1', 'ARTILLERY_BOSS_2', 'ARTILLERY_BOSS_3', 'ARTILLERY_BOSS_4']
	if Mod == "Arsenal+":
		randomCycleBossArtillery += ['ARTILLERY_BOSS_1_HARD', 'ARTILLERY_BOSS_2_HARD', 'ARTILLERY_BOSS_3_HARD', 'ARTILLERY_BOSS_4_HARD', 'ARTILLERY_BOSS_1_EASY', 'ARTILLERY_BOSS_2_EASY', 'ARTILLERY_BOSS_3_EASY', 'ARTILLERY_BOSS_4_EASY', 'FR_BOSS_MISSILES_HULL', 'FR_BOSS_BOMB', 'FR_BOSS_BEAM_BIO', 'FR_BOSS_BEAM_FIRE', 'FR_BOSS_BEAM_FOCUS', 'FR_BOSS_BEAM_HULL', 'FR_BOSS_BEAM_INDUSTRIAL', 'FR_BOSS_BEAM_HULL', 'FR_BOSS_EFFECTOR', 'FR_BOSS_ION_FLAK', 'FR_BOSS_ION_HEAVY', 'FR_BOSS_ION_PHASE', 'FR_BOSS_ION_STUN', 'FR_BOSS_LASER_ARTILLERY', 'FR_BOSS_LASER_BURST_SCATTER', 'FR_BOSS_LASER_HEAVY', 'FR_BOSS_LASER_HULL', 'FR_BOSS_LASER_LIGHT_ARTILLERY', 'FR_BOSS_MINES', 'FR_BOSS_MISSILES_BREACH', 'FR_BOSS_MISSILES_FIRE', 'FR_BOSS_MISSILES_SWARM', 'FR_BOSS_PLASMA', 'FR_BOSS_SHOTGUN']
	shuffle(randomCycleBossArtillery)
	randomCycleBossArtillery.append('debug')
	randomCycleBossArtillery.insert(0, 'debug')
	
	randomCycleMinimumSector = []
	for x in range(1,7):
		randomCycleMinimumSector.append(str(x))
	shuffle(randomCycleMinimumSector)
	randomCycleMinimumSector.append('debug')
	randomCycleMinimumSector.insert(0, 'debug')
	
	randomCycleBlueprintRarity = []
	for x in range(1,6):
		randomCycleBlueprintRarity.append(str(x))
	shuffle(randomCycleBlueprintRarity)
	randomCycleBlueprintRarity.append('debug')
	randomCycleBlueprintRarity.insert(0, 'debug')
	
	randomCycleSectorEventMax = []
	for x in range(1,13):
		randomCycleSectorEventMax.append(str(x))
	shuffle(randomCycleSectorEventMax)
	randomCycleSectorEventMax.append('debug')
	randomCycleSectorEventMax.insert(0, 'debug')
		
	randomCycleHealth = []
	if balanced is False:
		for x in range(1,41):
			randomCycleHealth.append(str(x))
		shuffle(randomCycleHealth)
		randomCycleHealth.append('debug')
		randomCycleHealth.insert(0, 'debug')
	else:
		for x in range(0, 5):
			randomCycleHealth.append([])
			for y in range(8*(x+1) - 7, 8*(x+1)+1):
				randomCycleHealth[x].append(y)
				shuffle(randomCycleHealth[x])
			randomCycleHealth[x].append('debug' + str(x))
			randomCycleHealth[x].insert(0, 'debug' + str(x))
		randomCycleHealth = randomCycleHealth[0] + randomCycleHealth[1] + randomCycleHealth[2] + randomCycleHealth[3] + randomCycleHealth[4]
	
	randomCycleAug = ['DRONE_SPEED', 'SYSTEM_CASING', 'ION_ARMOR', 'CLOAK_FIRE', 'REPAIR_ARM', 'SCRAP_COLLECTOR', 'ADV_SCANNERS', 'AUTO_COOLDOWN', 'SHIELD_RECHARGE', 'WEAPON_PREIGNITE', 'FTL_BOOSTER', 'FTL_JUMPER', 'DRONE_RECOVERY', 'FTL_JAMMER', 'STASIS_POD', 'O2_MASKS', 'EXPLOSIVE_REPLICATOR', 'FIRE_EXTINGUISHERS', 'FLEET_DISTRACTION', 'TELEPORT_HEAL', 'BATTERY_BOOSTER', 'DEFENSE_SCRAMBLER', 'BACKUP_DNA', 'HACKING_STUN', 'LIFE_SCANNER', 'ZOLTAN_BYPASS']
	if balanced is False:
		randomCycleAug += ['ROCK_ARMOR', 'CRYSTAL_SHARDS', 'ENERGY_SHIELD', 'NANO_MEDBAY', 'SLUG_GEL', 'CREW_STIMS']
	if Mod=="CE":
		randomCycleAug += ['AE_ADV_THRUSTERS', 'AE_FUEL_RECYCLE', 'AE_AMMO_MANUFACTURER', 'AE_DRONE_MANUFACTURER', 'AE_HOLOGRAM_GENERATOR', 'AE_SECTOR_SCANNER', 'AE_SECTOR_MAPPING', 'AE_CLONE_LAB', 'AE_PRODUCTION', 'AE_HOLOGRAM_GENERATOR', 'AE_TRADE_BOOSTER', 'AE_SCIENCE', 'AE_BEACON_KIT', 'AE_REPAIR_KIT', 'AE_REQUISITION', 'AE_COMBAT_SIMULATOR', 'AE_BOUNTYHUNTER', 'AE_WEAPON_JAMMER', 'AE_DRONE_JAMMER', 'AE_TELEPORTER_JAMMER', 'AE_SHIELD_JAMMER', 'AE_IRRADIATOR', 'AE_ADV_EFFECTOR', 'AE_NEBULA_SCANNER', 'AE_MIND_SHIELD', 'AE_FIREWALL', 'AE_ASB', 'AE_AUG_GENERATOR']
		if balanced is False:
			randomCycleAug += ["TE_GOODS_CIVILIAN_CONSUMER", "TE_GOODS_CIVILIAN_LUXURY", "TE_GOODS_CIVILIAN_FOOD", "TE_GOODS_ENGI_MEDICINE", "TE_GOODS_ENGI_ELECTRONICS", "TE_GOODS_ENGI_MACHINES", "TE_GOODS_ZOLTAN_BEACONS", "TE_GOODS_ZOLTAN_CODEX", "TE_GOODS_ZOLTAN_SHIELDS", "TE_GOODS_ROCK_LITERATURE", "TE_GOODS_ROCK_ORE", "TE_GOODS_ROCK_HULLS", "TE_GOODS_MANTIS_ENGINES", "TE_GOODS_MANTIS_WEAPONS", "TE_GOODS_MANTIS_BOUNTY", "TE_GOODS_SLUG_DRUGS", "TE_GOODS_SLUG_ART", "TE_GOODS_SLUG_ANIMALS", "TE_GOODS_NEBULA_GAS", "TE_GOODS_PIRATE_ARMS", "TE_GOODS_REBEL_CONTRABAND", "TE_GOODS_CRYSTAL_ARTIFACTS", "TE_GOODS_FED_WRECK", "TE_GOODS_HAZARD_ELEMENTS", "TE_GOODS_FED_WRECK", "TE_GOODS_AI_DATA", "TE_GOODS_AI_NANOBOTS", "TE_GOODS_QUARANTINE_DISEASE", "TE_GOODS_INDUSTRIAL_TERRAFORMING", "TE_GOODS_INDUSTRIAL_REACTOR", "TE_GOODS_LANIUS_POLYMERS", "TE_GOODS_GIRDERS", "TE_GOODS_CHEMICALS", "TE_GOODS_TEXTILES", "TE_GOODS_ORGANISMS", "TE_GOODS_O2", "TE_GOODS_H2O", "TE_GOODS_SEEDS", "TE_GOODS_CONDUITS", "TE_GOODS_PRODUCE", "TE_GOODS_ANTIMATTER", "TE_GOODS_GAMES", "TE_GOODS_SENSORS", "TE_GOODS_LIFESUPPORT", "TE_GOODS_ROBOTS", "TE_GOODS_RESEARCH", "TE_GOODS_SOLAR", "TE_GOODS_RELICS", "TE_GOODS_CLONES", "TE_GOODS_AMBRA", "TE_GOODS_GEMS", "TE_GOODS_GLANDS"]
	if Mod=="Arsenal+":
		randomCycleAug += ['TULLY_BOX']
		if balanced is False:
			randomCycleAug += ['INJECTOR_PRC', 'INJECTOR_FRC', 'INJECTOR_BRC', 'INJECTOR_CLD', 'INJECTOR_POW', 'INJECTOR_UNI']
	shuffle(randomCycleAug)
	randomCycleAug.append('debug')
	randomCycleAug.insert(0, 'debug')
	
	
	randomCyclePower = []
	if balanced is False:
		for x in range(0, 20):
			randomCyclePower.append(str(x))
		shuffle(randomCyclePower)
		randomCyclePower.append('debug')
		randomCyclePower.insert(0, 'debug')
	else:
		for x in range(0, 4):
			randomCyclePower.append([])
			for y in range(4*x, 4*(x+1)):
				randomCyclePower[x].append(y)
				shuffle(randomCyclePower[x])
			randomCyclePower[x].append('debug' + str(x))
			randomCyclePower[x].insert(0, 'debug' + str(x))
		randomCyclePower = randomCyclePower[0] + randomCyclePower[1] + randomCyclePower[2] + randomCyclePower[3]
	
	randomCycleRarity = []
	for x in range(1,6):
		randomCycleRarity.append(str(x))
	shuffle(randomCycleRarity)
	randomCycleRarity.append('debug')
	randomCycleRarity.insert(0, 'debug')
	
	randomCycleCost = []
	if balanced is False:
		for x in range(1,211):
			randomCycleCost.append(str(x))
		shuffle(randomCycleCost)
		randomCycleCost.append('debug')
		randomCycleCost.insert(0, 'debug')
	else:
		for x in range(0, 4):
			randomCycleCost.append([])
			for y in range(50*(x+1)+10 - 49, 50*(x+1)+1+10):
				randomCycleCost[x].append(y)
				shuffle(randomCycleCost[x])
		randomCycleCost.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
		shuffle(randomCycleCost[-1])
		randomCycleCost[x].append('debug' + str(x))
		randomCycleCost[x].insert(0, 'debug' + str(x))
		randomCycleCost = randomCycleCost[0] + randomCycleCost[1] + randomCycleCost[2] + randomCycleCost[3] + randomCycleCost[4]
	
	if randShipCheck is True:
		
		playerImgOrder = []
		shipTypeId = []
		
		print('Importing random ship data')
		playerShipOrder = ['PLAYER_SHIP_HARD', 'PLAYER_SHIP_CIRCLE', 'PLAYER_SHIP_FED', 'PLAYER_SHIP_ENERGY', 'PLAYER_SHIP_MANTIS', 'PLAYER_SHIP_JELLY', 'PLAYER_SHIP_ROCK', 'PLAYER_SHIP_STEALTH', 'PLAYER_SHIP_CRYSTAL', 'PLAYER_SHIP_ANAEROBIC', 'PLAYER_SHIP_HARD_2', 'PLAYER_SHIP_CIRCLE_2', 'PLAYER_SHIP_FED_2', 'PLAYER_SHIP_ENERGY_2', 'PLAYER_SHIP_MANTIS_2', 'PLAYER_SHIP_JELLY_2', 'PLAYER_SHIP_ROCK_2', 'PLAYER_SHIP_STEALTH_2', 'PLAYER_SHIP_CRYSTAL_2', 'PLAYER_SHIP_ANAEROBIC_2', 'PLAYER_SHIP_HARD_3', 'PLAYER_SHIP_CIRCLE_3', 'PLAYER_SHIP_FED_3', 'PLAYER_SHIP_ENERGY_3', 'PLAYER_SHIP_MANTIS_3', 'PLAYER_SHIP_JELLY_3', 'PLAYER_SHIP_ROCK_3', 'PLAYER_SHIP_STEALTH_3']
		if os.path.exists('source/compatibility/'+str(Mod)+'/playerImgOrder.xml') is True:
			tree = ET.parse('source/compatibility/'+str(Mod)+'/playerImgOrder.xml')
		else:
			tree = ET.parse('source/compatibility/Vanilla/playerImgOrder.xml')
		root = tree.getroot()
		for child in root:
			if child.tag == 'img':
				playerImgOrder.append(child.text)
			if child.tag == 'shipTypeID':
				if 'preset' in child.attrib:
					if child.attrib['preset'] == 'abc':
						shipTypeId = []
						for letter in range(0, 26):
							shipTypeId.append('_' + chr(letter+97))
					if child.attrib['preset'] == '123':
						shipTypeId = []
						for letter in range(1, 26):
							shipTypeId.append('_' + str(letter))
				else:
					for child_suffix in child:
						if child_suffix.tag == 'suffix':
							if child_suffix.text is None:
								shipTypeId.append('')
							else:
								shipTypeId.append(child_suffix.text)
				
		randomCyclePlayerHull = []
		for x in range(0, len(playerImgOrder)):
			randomCyclePlayerHull.append([])
		for x in range(0, len(playerImgOrder)):
			if x >= 8:
				imgCheck = 3
			else:
				imgCheck = 4
			while (os.path.exists('source/compatibility/Global/img/ship/' + str(playerImgOrder[x]) + str(shipTypeId[imgCheck-1]) + '_base.png') is True or os.path.exists('source/compatibility/'+str(Mod)+'/img/ship/' + str(playerImgOrder[x]) + str(shipTypeId[imgCheck-1]) + '_base.png') is True) and imgCheck < len(shipTypeId):
				imgCheck += 1
			for y in range(1, imgCheck):
				randomCyclePlayerHull[x].append(str(y))
			shuffle(randomCyclePlayerHull[x])
		
		allNames = [[], [], 'skip', [], [], [], [], 'skip', [], 'skip']
		
		namesOrder = ['ship_PLAYER_SHIP_BIRD', 'ship_PLAYER_SHIP_CIRCLE', 'skip', 'ship_PLAYER_SHIP_ENERGY', 'ship_PLAYER_SHIP_MANTIS', 'ship_PLAYER_SHIP_JELLY', 'ship_PLAYER_SHIP_ROCK', 'skip', 'ship_PLAYER_SHIP_CRYSTAL', 'skip', ]
		
		tree = ET.parse('source/names/names.xml')
		root = tree.getroot()
		for index, type in enumerate(namesOrder):
			if type != 'skip':
				for child in root:
					try:
						if child.tag == 'nameList' and child.attrib['type'] == type:
							for name in child:
								if name.tag == 'name':
									allNames[index].append(name.text)
					except ET.KeyError:
						print('Error in parsing names.xml, undefined "type" attribute.')
					except:
						raise
				
		for x in range(0, len(allNames)):
			if allNames[x] != 'skip':
				shuffle(allNames[x])
			else:
				allNames[x] = allNames[0][(4 - allNames.count('skip'))*3:] + allNames[0][:(4 - allNames.count('skip'))*3]
		
		allLayouts = [[], [], [], [], [], [], [], [], [], []]
		for x in range(0, len(allLayouts)):
			layoutCheck = 1
			crashCheck = 0
			if os.path.exists('source/layouts/'+str(Mod)) is True:
				while os.path.exists('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])+'/'+str(playerImgOrder[x])+str(shipTypeId[layoutCheck])+'.xml') is True and os.path.exists('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])+'/'+str(playerImgOrder[x])+str(shipTypeId[layoutCheck])+'.txt') is True and crashCheck < 100:
					layoutCheck += 1
					crashCheck += 1
			else:
				while os.path.exists('source/layouts/Vanilla/'+str(playerShipOrder[x])+'/'+str(playerImgOrder[x])+str(shipTypeId[layoutCheck])+'.xml') is True and os.path.exists('source/layouts/Vanilla/'+str(playerShipOrder[x])+'/'+str(playerImgOrder[x])+str(shipTypeId[layoutCheck])+'.txt') is True and crashCheck < 100:
					layoutCheck += 1
					crashCheck += 1
			for y in range(0, layoutCheck):
				allLayouts[x].append(playerImgOrder[x]+str(shipTypeId[y]))
			shuffle(allLayouts[x])
		
	randomCycleWeaponDamage = []
	if balanced is False and equipDamage is True:
		for x in range(1,5):
			randomCycleWeaponDamage.append(str(x))
		shuffle(randomCycleWeaponDamage)
		randomCycleWeaponDamage.append('debug')
		randomCycleWeaponDamage.insert(0, 'debug')
	else:
		randomCycleWeaponDamage = []
	
	randomCycleWeaponCooldown = []
	if balanced is False:
		for x in range(1,301):
			if x%10 == 0:
				randomCycleWeaponCooldown.append(str(x//10))
			else:
				randomCycleWeaponCooldown.append(str(x/10))
		shuffle(randomCycleWeaponCooldown)
		randomCycleWeaponCooldown.append('debug')
		randomCycleWeaponCooldown.insert(0, 'debug')
	else:
		for x in range(0, 6):
			randomCycleWeaponCooldown.append([])
			for y in range(50*(x+1) - 49, 50*(x+1)+1):
				if y%10 == 0:
					randomCycleWeaponCooldown[x].append(str(y//10))
				else:
					randomCycleWeaponCooldown[x].append(str(y/10))
			shuffle(randomCycleWeaponCooldown[x])
			randomCycleWeaponCooldown[x].append('debug'+str(x))
			randomCycleWeaponCooldown[x].insert(0, 'debug'+str(x))
		randomCycleWeaponCooldown = randomCycleWeaponCooldown[0] + randomCycleWeaponCooldown[1] + randomCycleWeaponCooldown[2] + randomCycleWeaponCooldown[3] + randomCycleWeaponCooldown[4] + randomCycleWeaponCooldown[5]
		
	randomCycleWeaponSP = []
	if balanced is False:
		for x in range(-2,5):
			randomCycleWeaponSP.append(str(x))
		for z in range(0, 3):
			for x in range(0,5):
				randomCycleWeaponSP.append(str(x))
		shuffle(randomCycleWeaponSP)
		randomCycleWeaponSP.append('debug')
		randomCycleWeaponSP.insert(0, 'debug')
	else:
		randomCycleWeaponSP = []
	
	randomCycleWeaponSpeed = []
	if balanced is False:
		for x in range(1, 101):
			randomCycleWeaponSpeed.append(str(x))
		shuffle(randomCycleWeaponSpeed)
		randomCycleWeaponSpeed.append('debug')
		randomCycleWeaponSpeed.insert(0, 'debug')
	else:
		for x in range(0, 5):
			randomCycleWeaponSpeed.append([])
			for y in range(20*x+1, 20*(x+1)+1):
				randomCycleWeaponSpeed[x].append(str(y))
			shuffle(randomCycleWeaponSpeed[x])
			randomCycleWeaponSpeed[x].append('debug'+str(x))
			randomCycleWeaponSpeed[x].insert(0, 'debug'+str(x))
		randomCycleWeaponSpeed = randomCycleWeaponSpeed[0] + randomCycleWeaponSpeed[1] + randomCycleWeaponSpeed[2] + randomCycleWeaponSpeed[3] + randomCycleWeaponSpeed[4]
	
	randomCycleWeaponBreach = []
	if balanced is False:
		for x in range(0, 11):
			randomCycleWeaponBreach.append(str(x))
		shuffle(randomCycleWeaponBreach)
		randomCycleWeaponBreach.append('debug')
		randomCycleWeaponBreach.insert(0, 'debug')
	else:
		for x in range(0, 3):
			randomCycleWeaponBreach.append([])
			for y in range(4*x, 4*(x+1)):
				if y > 10:
					randomCycleWeaponBreach[x].append(str(10))
				else:
					randomCycleWeaponBreach[x].append(str(y))
			shuffle(randomCycleWeaponBreach[x])
			randomCycleWeaponBreach[x].append('debug'+str(x))
			randomCycleWeaponBreach[x].insert(0, 'debug'+str(x))
		randomCycleWeaponBreach = randomCycleWeaponBreach[0] + randomCycleWeaponBreach[1] + randomCycleWeaponBreach[2]
	
	randomCycleWeaponFire = []
	if balanced is False:
		for x in range(0, 11):
			randomCycleWeaponFire.append(str(x))
		shuffle(randomCycleWeaponFire)
		randomCycleWeaponFire.append('debug')
		randomCycleWeaponFire.insert(0, 'debug')
	else:
		for x in range(0, 3):
			randomCycleWeaponFire.append([])
			for y in range(4*x, 4*(x+1)):
				if y > 10:
					randomCycleWeaponFire[x].append(str(10))
				else:
					randomCycleWeaponFire[x].append(str(y))
			shuffle(randomCycleWeaponFire[x])
			randomCycleWeaponFire[x].append('debug'+str(x))
			randomCycleWeaponFire[x].insert(0, 'debug'+str(x))
		randomCycleWeaponFire = randomCycleWeaponFire[0] + randomCycleWeaponFire[1] + randomCycleWeaponFire[2]
	
	randomCycleWeaponStun = []
	if balanced is False:
		for x in range(0, 11):
			randomCycleWeaponStun.append(str(x))
		shuffle(randomCycleWeaponStun)
		randomCycleWeaponStun.append('debug')
		randomCycleWeaponStun.insert(0, 'debug')
	else:
		for x in range(0, 3):
			randomCycleWeaponStun.append([])
			for y in range(4*x, 4*(x+1)):
				if y > 10:
					randomCycleWeaponStun[x].append(str(10))
				else:
					randomCycleWeaponStun[x].append(str(y))
			shuffle(randomCycleWeaponStun[x])
			randomCycleWeaponStun[x].append('debug'+str(x))
			randomCycleWeaponStun[x].insert(0, 'debug'+str(x))
		randomCycleWeaponStun = randomCycleWeaponStun[0] + randomCycleWeaponStun[1] + randomCycleWeaponStun[2]
	
	randomCycleAugValue = []
	if balanced is False:
		for x in range(1,100):
			randomCycleAugValue.append(str(x/100))
		shuffle(randomCycleAugValue)
		randomCycleAugValue.append('debug')
		randomCycleAugValue.insert(0, 'debug')
	else:
		for x in range(0, 5):
			randomCycleAugValue.append([])
			for y in range(20*(x+1) - 19, 20*(x+1)+1):
				randomCycleAugValue[x].append(y/100)
				shuffle(randomCycleAugValue[x])
			randomCycleAugValue[x].append('debug'+str(x))
			randomCycleAugValue[x].insert(0, 'debug'+str(x))
		randomCycleAugValue = randomCycleAugValue[0] + randomCycleAugValue[1] + randomCycleAugValue[2] + randomCycleAugValue[3] + randomCycleAugValue[4]
	
	randomCycleDroneSpeed = []
	if balanced is False:
		for x in range(1,31):
					randomCycleDroneSpeed.append(str(x))
		shuffle(randomCycleDroneSpeed)
		randomCycleDroneSpeed.append('debug')
		randomCycleDroneSpeed.insert(0, 'debug')
	else:
		for x in range(0, 5):
			randomCycleDroneSpeed.append([])
			for y in range(6*(x+1) - 5, 6*(x+1)+1):
				randomCycleDroneSpeed[x].append(y)
				shuffle(randomCycleDroneSpeed[x])
			randomCycleDroneSpeed[x].append('debug'+str(x))
			randomCycleDroneSpeed[x].insert(0, 'debug'+str(x))
		randomCycleDroneSpeed = randomCycleDroneSpeed[0] + randomCycleDroneSpeed[1] + randomCycleDroneSpeed[2] + randomCycleDroneSpeed[3] + randomCycleDroneSpeed[4]
	
	randomCycleDroneCooldown = []
	if balanced is False:
		for x in range(1,2001):
			randomCycleDroneCooldown.append(str(x))
		shuffle(randomCycleDroneCooldown)
		randomCycleDroneCooldown.append('debug')
		randomCycleDroneCooldown.insert(0, 'debug')
	else:
		for x in range(0, 6):
			randomCycleDroneCooldown.append([])
			for y in range(500*(x+1) - 499, 500*(x+1)+1):
				randomCycleDroneCooldown[x].append(y)
			shuffle(randomCycleDroneCooldown[x])
			randomCycleDroneCooldown[x].append('debug'+str(x))
			randomCycleDroneCooldown[x].insert(0, 'debug'+str(x))
		randomCycleDroneCooldown = randomCycleDroneCooldown[0] + randomCycleDroneCooldown[1] + randomCycleDroneCooldown[2] + randomCycleDroneCooldown[3] + randomCycleDroneCooldown[4] + randomCycleDroneCooldown[5]
	
	randomCycleWeaponPower = []
	if balanced is False and equipPower is True:
		for x in range(1, 5):
			randomCycleWeaponPower.append(str(x))
		shuffle(randomCycleWeaponPower)
		randomCycleWeaponPower.append('debug')
		randomCycleWeaponPower.insert(0, 'debug')
	
	extraEquipment = []
	
	if extraEquipmentCheck is True:
		print('Selecting extra packs')
		
		tree = ET.parse('source/Extra Packs/packsInfo.xml')
		root = tree.getroot()
		
		for pack in root:
			try:
				if os.path.exists('source/Extra Packs/' + pack.attrib['name']) is True and ((hyperspace is False and 'hyperspaceReq' not in [elem.tag for elem in pack.iter() if elem is not pack]) or hyperspace is True):
					chance = 0
					for child in pack:
						if child.tag == 'chance':
							chance = child.text
					if chance is None:
						chance = 0
					print(chance)
					if int(chance) >= randint(0, 100) > 0:
						extraEquipment.append(pack.attrib['name'])
				else:
					print('No ' + pack.attrib['name'] + ' directory in Extra Packs')
			except KeyError:
				print('Missing name attribute in packsInfo.xml')
			except:
				raise
		
		print('Included packs:')
		print(extraEquipment)
	
	#Ship Creation
	
	blueprints_ships = ''''''
	
	if randShipCheck is True:
	
		print('Importing random ship data')
		
		systemNames = [[], [], [], [], [], [], [], [], [], []]
		systemRarities = [[], [], [], [], [], [], [], [], [], []]
		systemLevelWeights = [[], [], [], [], [], [], [], [], [], []]
		
		shipWeapons = [[], [], [], [], [], [], [], [], [], []]
		
		STshipWeapons = [[], [], [], [], [], [], [], [], [], []]
		
		shipDrones = [[], [], [], [], [], [], [], [], [], []]
		
		STshipDrones = [[], [], [], [], [], [], [], [], [], []]
		
		shipAug = [[], [], [], [], [], [], [], [], [], []]
		
		STshipAug = [[], [], [], [], [], [], [], [], [], []]
		
		augCountRarities = [[], [], [], [], [], [], [], [], [], []]
		
		CrewCountRarities = [[], [], [], [], [], [], [], [], [], []]
		STCrewRarities = [[], [], [], [], [], [], [], [], [], []]
		CrewRarities = [[], [], [], [], [], [], [], [], [], []]
		
		ArtilleryChoices = [[], [], [], [], [], [], [], [], [], []]
		
		systemCountRarities = [[], [], [], [], [], [], [], [], [], []]
					
			
		if os.path.exists('source/shipArmaments/'+str(Mod)+'Armaments.xml') is True:
			tree = ET.parse('source/shipArmaments/'+str(Mod)+'Armaments.xml')
		else:
			tree = ET.parse('source/shipArmaments/VanillaArmaments.xml')
		root = tree.getroot()
		
		for y in range(0, len(extraEquipment)):
			if os.path.exists('source/Extra Packs/'+str(extraEquipment[y])+'/AppendArmaments.xml') is True:
				treeExtra = ET.parse('source/Extra Packs/'+str(extraEquipment[y])+'/AppendArmaments.xml')
				rootExtra = tree.getroot()
				root.extend(rootExtra)
				
		missileWeapons = []
		dlcItems = []
		itemPowers = {}
		for blueprintList in root:
			try:
				if blueprintList.attrib['name'] == 'all_weapons':
					for weapon in blueprintList:
						if len(randomCycleWeaponPower) > 2:
							# print('Changing weapon power')
							itemPowers[weapon.text] = randomCycleWeaponPower[randomCycleWeaponPower.index(weapon.attrib['power']) - 1]
							if itemPowers[weapon.text] == 'debug':
								itemPowers[weapon.text] = randomCycleWeaponPower[-2]
						else:
							itemPowers[weapon.text] = weapon.attrib['power']
						try:
							if weapon.attrib['type'] in ['missile', 'bomb']:
								missileWeapons.append(weapon.text)
						except:
							pass
						try:
							if weapon.attrib['dlc'] == 'true':
								dlcItems.append(weapon.text)
						except:
							pass
			except KeyError:
				print('Error in VanillaArmaments.xml, no "name" attribute')
			except:
				raise
				
			try:
				if blueprintList.attrib['name'] == 'all_drones':
					for weapon in blueprintList:
						itemPowers[weapon.text] = weapon.attrib['power']
						try:
							if weapon.attrib['dlc'] == 'true':
								dlcItems.append(weapon.text)
						except:
							pass
			except KeyError:
				print('Error in VanillaArmaments.xml, no "name" attribute')
			except:
				raise
				
			try:
				if blueprintList.attrib['name'] == 'all_augments':
					for weapon in blueprintList:
						try:
							if weapon.attrib['dlc'] == 'true':
								dlcItems.append(weapon.text)
						except:
							pass
			except KeyError:
				print('Error in VanillaArmaments.xml, no "name" attribute')
			except:
				raise
				
			try:
				if blueprintList.attrib['name'] == 'all_crew':
					for weapon in blueprintList:
						try:
							if weapon.attrib['dlc'] == 'true':
								dlcItems.append(weapon.text)
						except:
							pass
			except KeyError:
				print('Error in VanillaArmaments.xml, no "name" attribute')
			except:
				raise
				
			try:
				if blueprintList.attrib['name'] == 'all_systems':
					for weapon in blueprintList:
						try:
							if weapon.attrib['dlc'] == 'true':
								dlcItems.append(weapon.text)
						except:
							pass
			except KeyError:
				print('Error in VanillaArmaments.xml, no "name" attribute')
			except:
				raise
		
		
		if os.path.exists('source/shipArmaments/' + Mod + 'Armaments.xml') is True:
			tree = ET.parse('source/shipArmaments/' + Mod + 'Armaments.xml')
		else:
			tree = ET.parse('source/shipArmaments/VanillaArmaments.xml')
		root = tree.getroot()
		for x in range(0, 10):
			for child in root:
				if child.tag == 'shipArmament' and child.attrib['name'] == playerShipOrder[x]:
					shipRoot = child
					break
			
			for child in shipRoot:
				if child.tag == 'weaponsList':
					for weachild in child:
						for i in range(0, 6 - int(weachild.attrib['rarity'])):
							shipWeapons[x].append(weachild.text)
							try:
								if weachild.attrib['start'] == 'true':
									STshipWeapons[x].append(weachild.text)
							except:
								pass
				if child.tag == 'dronesList':
					for drochild in child:
						for i in range(0, 6 - int(drochild.attrib['rarity'])):
							shipDrones[x].append(drochild.text)
							try:
								if drochild.attrib['start'] == 'true':
									STshipDrones[x].append(drochild.text)
							except:
								pass
				if child.tag == 'augList':
					augCountRarities[x] = [int(i) for i in child.attrib['countRatio'].split('|')]
					for augchild in child:
						for i in range(0, 6 - int(augchild.attrib['rarity'])):
							shipAug[x].append(augchild.text)
						try:
							if augchild.attrib['start'] == 'true':
								STshipAug[x].append(augchild.text)
						except:
							pass
				if child.tag == 'crewList':
					for index, i in enumerate(child.attrib['countRatio'].split('|')):
						for y in range(0, int(i)):
							CrewCountRarities[x].append(index)
					for crewchild in child:
						for i in range(0, 6 - int(crewchild.attrib['rarity'])):
							CrewRarities[x].append(crewchild.text)
						try:
							if int(crewchild.attrib['min']) > 0:
								for y in range(0, int(crewchild.attrib['min'])):
									STCrewRarities[x].append(crewchild.text)
						except:
							pass
				if child.tag == 'systemsList':
					systemCountRarities[x] = [int(i) for i in child.attrib['countRatio'].split('|')]
					for syschild in child:
						weights = [int(i) for i in syschild.attrib['levelRatio'].split('|')]
						systemLevelWeights[x].append([])
						for power, count in enumerate(weights):
							for i in range(0, int(count)):
								systemLevelWeights[x][-1].append(str(int(power) + 1))
						systemNames[x].append(syschild.text)
						systemRarities[x].append(int(syschild.attrib['chance']))
				if child.tag == 'artilleryList':
					for artchild in child:
						ArtilleryChoices[x].append(artchild.text)
					
		print('Generating random ships')
		for x in range(0, len(playerShipOrder)):
				
			trueX = x
			print('making ' + str(playerShipOrder[trueX]))
			
			if balanced is False:
				x = randint(0, 27)
				
			crewList = []
			if balanced is True:
				crewList += STCrewRarities[x%10]
			
			crewCount = int(choice(CrewCountRarities[x%10]))
			
			while len(crewList) < crewCount:
				shuffle(CrewRarities[x%10])
				if CrewRarities[x%10][0] in dlcItems and (x == 9 or x >= 19 or balanced is False):
					crewList.append(CrewRarities[x%10][0][:-4])
				if CrewRarities[x%10][0] not in dlcItems:
					crewList.append(CrewRarities[x%10][0])
				
			if os.path.exists('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[trueX%10])+'/'+str(allLayouts[trueX%10][trueX//10])+'_blue.xml') is True:
				xmlRead = open('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[trueX%10])+'/'+str(allLayouts[trueX%10][trueX//10])+'_blue.xml', 'r')
			else:
				xmlRead = open('source/layouts/Vanilla/'+str(playerShipOrder[trueX%10])+'/'+str(allLayouts[trueX%10][trueX//10])+'_blue.xml', 'r')
			blueprints_ships += str(xmlRead.read(100000)) 
			xmlRead.close()
			
			probCount = 0
			systemCount = 8
			for y in range(0, len(systemCountRarities[x%10])):
				probCount += int(systemCountRarities[x%10][y])
				if randint(0, sum(systemCountRarities[x%10])) < probCount:
					systemCount = y
					break
					
			systems = []
				
			crashCount = 0
			while len(systems) != systemCount and crashCount < 100:
				if len(systems) < systemCount:
					for y in range(0, len(systemNames[x%10])):
						if systemRarities[x%10][y] >= randint(0, 100) > 0 and systemNames[x%10][y] not in systems and (systemNames[x%10][y] not in dlcItems or x == 9 or x >= 19 or balanced is False):
							systems.append(systemNames[x%10][y])
				if len(systems) > systemCount:
					for y in range(0, len(systems)):
						if systemRarities[x%10][systemNames[x%10].index(systems[y])] < randint(0, 100):
							systems[y] = 'delete'
					while 'delete' in systems:
						systems.remove('delete')
				crashCount += 1
			
			if balanced is False:
				if randint(0, 1) == 1:
					if 'medbay' in systems:
						systems[systems.index('medbay')] = 'clonebay'		
			elif x == 9 or x >= 19:
				if balanced is True:
					if 'medbay' in systems:
						systems[systems.index('medbay')] = 'clonebay'
					
			
			systemCount = len(systems)
				
				
			systemLevels = []
				
			for y in range(0, len(systems)):
				systemLevels.append(choice(systemLevelWeights[x%10][systemNames[x%10].index(systems[y])]))
			
			weapons = []
			
			try:
				weaponSystemLevel = int(systemLevels[systems.index("weapons")]) 
			except ValueError:
				print('Adding weapons system')
				weaponSystemLevel = 1
				systemLevels.append(1)
				systems.append('weapons')
			except:
				raise
			
			weaponDebuffPool = [-1, 0, 0, 0, 0, 0, 0, 1]
			
			if 'teleporter' in systems:
				weaponDebuffPool.append(1)
			
			if int(systemLevels[systems.index('weapons')]) == 4:
				weaponDebuffPool.append(1)
		
		
			shuffle(weaponDebuffPool)
			weaponsPowerSum = weaponDebuffPool[0]
		
			if weaponsPowerSum < 0:
				weaponsPowerSum = 0
			
			crashCheckWeapon = 0
			
			while weaponsPowerSum < weaponSystemLevel and crashCheckWeapon < 10000:
				
				if balanced is True and len(weapons) == 0:
					shuffle(STshipWeapons[x%10])
					for y in range(0, len(STshipWeapons[x%10])):
						if int(itemPowers[STshipWeapons[x%10][y]]) <= weaponSystemLevel - weaponsPowerSum and (STshipWeapons[x%10][y] not in weapons or balanced is False) and (STshipWeapons[x%10][y] not in dlcItems or x == 9 or x >= 19 or balanced is False):
							weapons.append(STshipWeapons[x%10][y])
							weaponsPowerSum += int(itemPowers[STshipWeapons[x%10][y]])
							break
				else:
					shuffle(shipWeapons[x%10])
					for y in range(0, len(shipWeapons[x%10])):
						if int(itemPowers[shipWeapons[x%10][y]]) <= weaponSystemLevel - weaponsPowerSum and (shipWeapons[x%10][y] not in weapons or balanced is False) and (shipWeapons[x%10][y] not in dlcItems or x == 9 or x >= 19 or balanced is False):
							weapons.append(shipWeapons[x%10][y])
							weaponsPowerSum += int(itemPowers[shipWeapons[x%10][y]])
							break
				
								
				crashCheckWeapon += 1
			
			drones = []
		
			
			if 'drones' in systems:
				
				crashCheckDrone = 0
			
				droneSystemLevel = int(systemLevels[systems.index("drones")])
				
				dronesPowerSum = 0
				while dronesPowerSum < droneSystemLevel + randint(-1, 1)  and crashCheckDrone < 1000:
					if balanced is True and len(drones) == 0:
						shuffle(STshipDrones[x%10])
						for y in range(0, len(STshipDrones[x%10])):
							if int(itemPowers[STshipDrones[x%10][y]]) <= droneSystemLevel - dronesPowerSum and (STshipDrones[x%10][y] not in drones or balanced is False) and (STshipDrones[x%10][y] not in dlcItems or x == 9 or x >= 19 or balanced is False):
								drones.append(STshipDrones[x%10][y])
								dronesPowerSum += int(itemPowers[STshipDrones[x%10][y]])
								break
					else:
						shuffle(shipDrones[x%10])
						for y in range(0, len(shipDrones[x%10])):
							if int(itemPowers[shipDrones[x%10][y]]) <= droneSystemLevel - dronesPowerSum and (shipDrones[x%10][y] not in drones or balanced is False) and (shipDrones[x%10][y] not in dlcItems or x == 9 or x >= 19 or balanced is False):
								drones.append(shipDrones[x%10][y])
								dronesPowerSum += int(itemPowers[shipDrones[x%10][y]])
								break
									
					crashCheckDrone += 1
					
			
			artilleryWeapon = ''
			if trueX%10==2:
				artilleryWeapon = choice(ArtilleryChoices[trueX%10])
			else:
				artilleryWeapon = choice(ArtilleryChoices[x%10])
				
			
			augmentList = []
			
			shuffle(STshipAug[x%10])
			for y in range(0, len(STshipAug[x%10])):
				if STshipAug[x%10][y] not in dlcItems or x == 9 or x >= 19 or balanced is False:
					augmentList.append(STshipAug[x%10][y])
				
			probCount = 0
			randNumb = randint(0, sum(augCountRarities[x%10]))
			for y in range(0, len(augCountRarities[x%10])):
				probCount += int(augCountRarities[x%10][y])
				if randNumb <= probCount:
					augmentCount = y
					break
			
			crashCheck = 0
			
			while len(augmentList) < augmentCount and crashCheck < 100:
				shuffle(shipAug[x%10])
				for y in range(0, len(shipAug[x%10])):
				
					if len(augmentList) >= augmentCount:
						break
					
					if shipAug[x%10][y] not in augmentList and (shipAug[x%10][y] not in dlcItems or x == 9 or x >= 19 or balanced is False):
						augmentList.append(shipAug[x%10][y])
						
				crashCheck += 1
				
			powerTotal = 0
			
			crashCount = 0
			
			for y in range(0, len(systems)):
				if systems[y] != 'pilot' and systems[y] != 'battery' and systems[y] != 'doors' and systems[y] != 'sensors' and systems[y] != 'medbay':
					if systems[y] == 'clonebay':
						powerTotal += randint(0, int(systemLevels[y]))
					elif systems[y] == 'oxygen':
						powerTotal += randint(1, int(systemLevels[y]))
					elif systems[y] == 'shields':
						powerTotal += int(systemLevels[y])//2*2
					elif systems[y] == 'weapons':
						powerTotal += int(weaponsPowerSum)
					elif systems[y] == 'drones':
						powerTotal += int(dronesPowerSum)
					else:
						powerTotal += int(systemLevels[y])
					
			reactorCount = powerTotal - crewList.count('energy') - systems.count('battery') * 4
			
			blueprints_ships += '''
<mod:findLike limit="1" reverse="true"> 
	<mod:setAttributes name="'''+str(playerShipOrder[trueX])+'''"/>
	<mod:setAttributes layout="'''+str(allLayouts[trueX%10][trueX//10])+'''"/>
	<mod:setAttributes img="'''+str(playerImgOrder[trueX%10]) + str(shipTypeId[int(randomCyclePlayerHull[trueX%10][trueX//10])-1])+'''"/>
	<mod-overwrite:name>''' + str(allNames[trueX%10][trueX//10]) + '''</mod-overwrite:name>
	<mod-overwrite:desc id="ship_'''+str(playerShipOrder[trueX])+'''_desc"/>
	<mod-overwrite:unlock id="ship_'''+str(playerShipOrder[trueX])+'''_unlock"/>
	<mod-overwrite:floorImage>'''+allLayouts[trueX%10][trueX//10]+'''</mod-overwrite:floorImage>
	<mod-overwrite:cloakImage>'''+str(playerImgOrder[trueX%10])+'''</mod-overwrite:cloakImage>
	<mod-overwrite:shieldImage>'''+str(playerImgOrder[trueX%10])+'''</mod-overwrite:shieldImage>
	<mod:findLike type="systemList">
		<mod:findComposite>
		<mod:par op="OR">
			<mod:findLike type="battery"/>
			<mod:findLike type="cloaking"/>
			<mod:findLike type="clonebay"/>
			<mod:findLike type="doors"/>
			<mod:findLike type="drones"/>
			<mod:findLike type="engines"/>
			<mod:findLike type="hacking"/>
			<mod:findLike type="medbay"/>
			<mod:findLike type="mind"/>
			<mod:findLike type="oxygen"/>
			<mod:findLike type="pilot"/>
			<mod:findLike type="sensors"/>
			<mod:findLike type="shields"/>
			<mod:findLike type="teleporter"/>
			<mod:findLike type="weapons"/>
			<mod:findLike type="artillery"/>
		</mod:par>
			
		<mod:setAttributes start="false"/>
	
		</mod:findComposite>'''
			
			if 'artillery' not in systems:
				blueprints_ships+='''
		<mod:findLike type="artillery">
			<mod:setAttributes weapon="'''+str(artilleryWeapon)+'''"/>
		</mod:findLike>
'''
				
			for y in range(0, len(systems)):
				blueprints_ships+='''
		<mod:findLike type="'''+str(systems[y])+'''">
			<mod:setAttributes start="true"/>
			<mod:setAttributes power="'''+str(systemLevels[y])+'''"/>'''
		
				if systems[y] == 'artillery':
					blueprints_ships+='''
			<mod:setAttributes weapon="'''+str(artilleryWeapon)+'''"/>'''
			
		
				blueprints_ships+='''
		</mod:findLike>
'''
				
			blueprints_ships+='''
	</mod:findLike>
'''
			
			if x%10 == 7 or x%10 == 4:
				blueprints_ships += '''
	<mod-append:weaponSlots>3</mod-append:weaponSlots>
	<mod-append:droneSlots>2</mod-append:droneSlots>
'''
				
			elif x%10 == 1:
				blueprints_ships += '''
	<mod-append:weaponSlots>3</mod-append:weaponSlots>
	<mod-append:droneSlots>3</mod-append:droneSlots>
'''
				
			else:
				blueprints_ships += '''
	<mod-append:weaponSlots>4</mod-append:weaponSlots>
	<mod-append:droneSlots>2</mod-append:droneSlots>
'''
		
			missileWeaponsCheck = 0
	
			if balanced is True:
				for y in range(0, len(weapons)):
					if weapons[y] in missileWeapons:
						missileWeaponsCheck += 1
			
			else:
				missileWeaponsCheck = randint(0, 4)
					
					
			blueprints_ships += '''
	<mod-append:weaponList count="'''+str(len(weapons))+'''" missiles="'''+str(missileWeaponsCheck*randint(12, 16))+'''">
	</mod-append:weaponList>
'''
			
			blueprints_ships += '''
	<mod:findLike type="weaponList">
'''
			for y in range(0, len(weapons)):
				blueprints_ships += '''
		<mod-append:weapon name="'''+str(weapons[y])+'''"/>
	'''
			blueprints_ships += '''
	</mod:findLike>
'''
		
			if balanced is True:
				blueprints_ships += '''
	<mod-append:droneList count="'''+str(len(drones))+'''" drones="'''+str(randint(len(drones)*8, (len(drones)+1)*8) + systems.count('hacking')*randint(6, 12))+'''">
	</mod-append:droneList>
'''
			else:
				blueprints_ships += '''
	<mod-append:droneList count="'''+str(len(drones))+'''" drones="'''+str(randint(0, 16))+'''">
	</mod-append:droneList>
'''
			
			
			blueprints_ships += '''
	<mod:findLike type="droneList">
'''
			for y in range(0, len(drones)):
				blueprints_ships += '''
		<mod-append:drone name="'''+str(drones[y])+'''"/>
	'''
			blueprints_ships += '''
	</mod:findLike>
'''
		
			for y in range(0, len(augmentList)):
				blueprints_ships += '''
	<mod-append:aug name="'''+str(augmentList[y])+'''"/>
'''
	
		
			for y in range(0, len(crewList)):
				blueprints_ships += '''
	<mod-append:crewCount amount = "1" class="'''+str(crewList[y])+'''"/>
'''
			
			blueprints_ships += '''
	<mod-append:health amount="'''+str(randint(20, 40))+'''"/>
	<mod-append:maxPower amount="'''+str(reactorCount)+'''"/>
		
</mod:findLike>
'''		
		# Ship Stuff - Crew, Augments, Reactor power and Health.
		
	print('Writing Code')
	blueprints_1 = '''
<mod:findComposite>
	<mod:par op="OR">
		<mod:findWithChildLike type="shipBlueprint" child-type="enemyShip"/>
	</mod:par>
	
	<!-- Crew Variety -->
	<!--''' + str(randomCycleCrew) + ''' --> '''
		
	for x in range(1, len(randomCycleCrew)):
		blueprints_1 += '''
	<mod:findLike type="crewCount">
		<mod:selector class="''' + str(randomCycleCrew[x-1]) + '''"/>
		<mod:setAttributes class="a"/>
	</mod:findLike>
	<mod:findLike type="crewCount">
		<mod:selector class="''' + str(randomCycleCrew[x]) + '''"/>
		<mod:setAttributes class="''' + str(randomCycleCrew[x-1]) + '''"/>
	</mod:findLike>
	<mod:findLike type="crewCount">
		<mod:selector class="a"/>
		<mod:setAttributes class="''' + str(randomCycleCrew[x]) + '''"/>
	</mod:findLike>'''
	
	blueprints_1 += '''			
	<!-- Min and Max Sector -->
	<!--''' + str(randomCycleMinimumSector) + ''' --> '''
		
		
	for x in range(1, len(randomCycleMinimumSector)):
		blueprints_1 += '''
	<mod:findLike type="maxSector">
		<mod:selector>''' + str(randomCycleMinimumSector[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="maxSector">
		<mod:selector>''' + str(randomCycleMinimumSector[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleMinimumSector[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="maxSector">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleMinimumSector[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	for x in range(1, len(randomCycleMinimumSector)):
		blueprints_1 += '''
	<mod:findLike type="minSector">
		<mod:selector>''' + str(randomCycleMinimumSector[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="minSector">
		<mod:selector>''' + str(randomCycleMinimumSector[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleMinimumSector[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="minSector">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleMinimumSector[x]) + '''</mod:setValue>
	</mod:findLike>'''
		
	
	blueprints_1 += '''			
	<!-- Starting Power -->
	<!--''' + str(randomCyclePower) + ''' --> '''
		
		
	for x in range(1, len(randomCyclePower)):
		blueprints_1 += '''
	<mod:findLike type="maxPower">
		<mod:selector amount="''' + str(randomCyclePower[x-1]) + '''"/>
		<mod:setAttributes amount="a"/>
	</mod:findLike>
	<mod:findLike type="maxPower">
		<mod:selector amount="''' + str(randomCyclePower[x]) + '''"/>
		<mod:setAttributes amount="''' + str(randomCyclePower[x-1]) + '''"/>
	</mod:findLike>
	<mod:findLike type="maxPower">
		<mod:selector amount="a"/>
		<mod:setAttributes amount="''' + str(randomCyclePower[x]) + '''"/>
	</mod:findLike>'''
	
	blueprints_1 += '''
	
	<!-- Augmentations -->
	<!--''' + str(randomCycleAug) + ''' --> '''
	
	for x in range(1, len(randomCycleAug)):
		blueprints_1 += '''
<mod:findLike type="aug">
	<mod:selector name="''' + str(randomCycleAug[x-1]) + '''"/>
	<mod:setAttributes name="a"/>
</mod:findLike>
<mod:findLike type="aug">
	<mod:selector name="''' + str(randomCycleAug[x]) + '''"/>
	<mod:setAttributes name="''' + str(randomCycleAug[x-1]) + '''"/>
</mod:findLike>
<mod:findLike type="aug">
	<mod:selector name="a"/>
	<mod:setAttributes name="''' + str(randomCycleAug[x]) + '''"/>
</mod:findLike>'''
	
	blueprints_1 += '''
	
	<!-- Ship Health -->
	<!--''' + str(randomCycleHealth) + ''' --> '''
	
	for x in range(1, len(randomCycleHealth)):
		blueprints_1 += '''
<mod:findLike type="health">
	<mod:selector amount="''' + str(randomCycleHealth[x-1]) + '''"/>
	<mod:setAttributes amount="a"/>
</mod:findLike>
<mod:findLike type="health">
	<mod:selector amount="''' + str(randomCycleHealth[x]) + '''"/>
	<mod:setAttributes amount="''' + str(randomCycleHealth[x-1]) + '''"/>
</mod:findLike>
<mod:findLike type="health">
	<mod:selector amount="a"/>
	<mod:setAttributes amount="''' + str(randomCycleHealth[x]) + '''"/>
</mod:findLike>'''
		
	blueprints_1 += '''
</mod:findComposite>'''
		
		
	blueprints_2 = '''
	
<!-- Item Rarity -->
<!--''' + str(randomCycleRarity) + ''' --> 
	
<mod:findComposite>
<mod:par op="OR">
	<mod:findWithChildLike type="weaponBlueprint" child-type="rarity"/>
	<mod:findWithChildLike type="droneBlueprint" child-type="rarity"/>
	<mod:findWithChildLike type="augBlueprint" child-type="rarity"/>
	<mod:findWithChildLike type="crewBlueprint" child-type="rarity"/>
	<mod:findWithChildLike type="systemBlueprint" child-type="rarity"/>
</mod:par>
	
'''
		
	for x in range(1, len(randomCycleRarity)):
		blueprints_2 += '''
	<mod:findLike type="rarity">
		<mod:selector>''' + str(randomCycleRarity[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="rarity">
		<mod:selector>''' + str(randomCycleRarity[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleRarity[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="rarity">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleRarity[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_2 += '''
</mod:findComposite>'''
		
		
	blueprints_3 = '''
	
<!-- Item Costs -->
<!--''' + str(randomCycleCost) + ''' -->
	
<mod:findComposite>
<mod:par op="OR">
	<mod:findWithChildLike type="weaponBlueprint" child-type="cost"/>
	<mod:findWithChildLike type="droneBlueprint" child-type="cost"/>
	<mod:findWithChildLike type="augBlueprint" child-type="cost"/>
	<mod:findWithChildLike type="crewBlueprint" child-type="cost"/>
	<mod:findWithChildLike type="systemBlueprint" child-type="cost"/>
	<mod:findWithChildLike type="itemBlueprint" child-type="cost"/>
</mod:par>'''
		
	for x in range(1, len(randomCycleCost)):
		blueprints_3 += '''
	<mod:findLike type="cost">
		<mod:selector>''' + str(randomCycleCost[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="cost">
		<mod:selector>''' + str(randomCycleCost[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleCost[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="cost">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleCost[x]) + '''</mod:setValue>
	</mod:findLike>'''
		
	blueprints_3 += '''
<!-- System Level Costs -->
<!-- Uses same cost cycle as above -->
	
	<mod:findComposite>
	<mod:par op="OR">
		<mod:findWithChildLike type="upgradeCost" child-type="level"/>
	</mod:par>'''
		
	for x in range(1, len(randomCycleCost)):
		blueprints_3 += '''
	<mod:findLike type="level">
		<mod:selector>''' + str(randomCycleCost[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="level">
		<mod:selector>''' + str(randomCycleCost[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleCost[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="level">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleCost[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_3 += '''
	</mod:findComposite>
</mod:findComposite>'''
		
	blueprints_5 = '''
<!-- Weapon Unique -->
<mod:findComposite>
	<mod:par op="OR">
	<mod:findLike type="weaponBlueprint"/>
	</mod:par>
	
	<!-- Damage and Ion Damage -->
	<!--''' + str(randomCycleWeaponDamage) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponDamage)):
		blueprints_5 += '''
	<mod:findLike type="damage">
		<mod:selector>''' + str(randomCycleWeaponDamage[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="damage">
		<mod:selector>''' + str(randomCycleWeaponDamage[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponDamage[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="damage">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponDamage[x]) + '''</mod:setValue>
	</mod:findLike>
	
	<mod:findLike type="ion">
		<mod:selector>''' + str(randomCycleWeaponDamage[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="ion">
		<mod:selector>''' + str(randomCycleWeaponDamage[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponDamage[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="ion">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponDamage[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_5 += '''
<!-- Shield Piercing -->
	<!--''' + str(randomCycleWeaponSP) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponSP)):
		blueprints_5 += '''
	<mod:findLike type="sp">
		<mod:selector>''' + str(randomCycleWeaponSP[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="sp">
		<mod:selector>''' + str(randomCycleWeaponSP[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponSP[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="sp">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponSP[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_5 += '''
<!-- Breach Chance -->
	<!--''' + str(randomCycleWeaponBreach) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponBreach)):
		blueprints_5 += '''
	<mod:findLike type="breachChance">
		<mod:selector>''' + str(randomCycleWeaponBreach[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="breachChance">
		<mod:selector>''' + str(randomCycleWeaponBreach[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponBreach[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="breachChance">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponBreach[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_5 += '''
<!-- Projectile Speed -->
	<!--''' + str(randomCycleWeaponSpeed) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponSpeed)):
		blueprints_5 += '''
	<mod:findLike type="Speed">
		<mod:selector>''' + str(randomCycleWeaponSpeed[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="Speed">
		<mod:selector>''' + str(randomCycleWeaponSpeed[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponSpeed[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="Speed">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponSpeed[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_5 += '''
<!-- Fire Chance -->
	<!--''' + str(randomCycleWeaponFire) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponFire)):
		blueprints_5 += '''
	<mod:findLike type="fireChance">
		<mod:selector>''' + str(randomCycleWeaponFire[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="fireChance">
		<mod:selector>''' + str(randomCycleWeaponFire[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponFire[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="fireChance">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponFire[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_5 += '''
<!-- Stun Chance -->
	<!--''' + str(randomCycleWeaponStun) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponStun)):
		blueprints_5 += '''
	<mod:findLike type="stunChance">
		<mod:selector>''' + str(randomCycleWeaponStun[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="stunChance">
		<mod:selector>''' + str(randomCycleWeaponStun[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponStun[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="stunChance">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponStun[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_5 += '''
<!-- Weapon Power -->
	<!--''' + str(randomCycleWeaponPower) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponPower)):
		blueprints_5 += '''
	<mod:findLike type="power">
		<mod:selector>''' + str(randomCycleWeaponPower[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="power">
		<mod:selector>''' + str(randomCycleWeaponPower[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponPower[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="power">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponPower[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	for x in range(1, len(randomCycleWeaponCooldown)):
		blueprints_5 += '''
	<mod:findLike type="cooldown">
		<mod:selector>''' + str(randomCycleWeaponCooldown[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="cooldown">
		<mod:selector>''' + str(randomCycleWeaponCooldown[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponCooldown[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="cooldown">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponCooldown[x]) + '''</mod:setValue>
	</mod:findLike>'''
		
	blueprints_5 += '''
</mod:findComposite>'''
	

	blueprints_5 += '''
<!-- Chain Cooldown -->
	
	<!--''' + str(randomCycleWeaponCooldown) + ''' --> '''
		
	for x in range(0, len(randomCycleWeaponCooldown)):
		if "debug" not in randomCycleWeaponCooldown[x]:
			for y in range(1, 6):
				blueprints_5 += '''

<mod:findWithChildLike type="weaponBlueprint" child-type="cooldown">
	<mod:selector type="chain">'''+str(randomCycleWeaponCooldown[x])+'''</mod:selector>
	<mod:findWithChildLike type="boost" child-type="count">
		<mod:selector>'''+str(y)+'''</mod:selector>
		<mod-overwrite:amount>''' + str(float(randomCycleWeaponCooldown[x])/y-uniform(0, float(randomCycleWeaponCooldown[x])/y)*10//1/10) + '''</mod-overwrite:amount>
	</mod:findWithChildLike>
</mod:findWithChildLike>'''
		
	
	blueprints_6 = '''
	
<!-- Augment Unique -->
	<!--''' + str(randomCycleAugValue) + ''' -->
	
<mod:findComposite>
	<mod:par op="OR">
		<mod:findLike type="augBlueprint"/>
	</mod:par>
		'''
		
	for x in range(1, len(randomCycleAugValue)):
		blueprints_6 += '''
	<mod:findLike type="value">
		<mod:selector>''' + str(randomCycleAugValue[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="value">
		<mod:selector>''' + str(randomCycleAugValue[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleAugValue[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="value">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleAugValue[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_6 += '''
</mod:findComposite>'''
		
		
	blueprints_7 = '''
<!-- Drones Unique -->
	
<mod:findComposite>
	<mod:par op="OR">
		<mod:findLike type="droneBlueprint"/>
	</mod:par>
	<!-- Drone Cooldown
	''' + str(randomCycleDroneCooldown) + '''-->'''
		
	for x in range(1, len(randomCycleDroneCooldown)):
		blueprints_7 += '''
	<mod:findLike type="cooldown">
		<mod:selector>''' + str(randomCycleDroneCooldown[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="cooldown">
		<mod:selector>''' + str(randomCycleDroneCooldown[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleDroneCooldown[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="cooldown">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleDroneCooldown[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_7 += '''<!-- Drone Speed
	''' + str(randomCycleDroneSpeed) + '''-->
		'''
		
	for x in range(1, len(randomCycleDroneSpeed)):
		blueprints_7 += '''
	<mod:findLike type="speed">
		<mod:selector>''' + str(randomCycleDroneSpeed[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="speed">
		<mod:selector>''' + str(randomCycleDroneSpeed[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleDroneSpeed[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="speed">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleDroneSpeed[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_7 += '''
		<!-- Drone Power -->
	<!--''' + str(randomCycleWeaponPower) + ''' --> '''
		
	for x in range(1, len(randomCycleWeaponPower)):
		blueprints_7 += '''
	<mod:findLike type="power">
		<mod:selector>''' + str(randomCycleWeaponPower[x-1]) + '''</mod:selector>
		<mod:setValue>a</mod:setValue>
	</mod:findLike>
	<mod:findLike type="power">
		<mod:selector>''' + str(randomCycleWeaponPower[x]) + '''</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponPower[x-1]) + '''</mod:setValue>
	</mod:findLike>
	<mod:findLike type="power">
		<mod:selector>a</mod:selector>
		<mod:setValue>''' + str(randomCycleWeaponPower[x]) + '''</mod:setValue>
	</mod:findLike>'''
	
	blueprints_7 += '''
</mod:findComposite>'''
		
		
		# bosses.xml - Artillery Randomisation
		
	bosses_1 = '''
<mod:findComposite>
	<mod:par op="OR">
		<mod:findLike type="shipBlueprint"/>
	</mod:par>
	
	<!-- Boss Artillery -->
	<!--''' + str(randomCycleBossArtillery) + ''' --> '''
		
	for x in range(1, len(randomCycleBossArtillery)):
		bosses_1 += '''
	<mod:findLike type="artillery">
		<mod:selector weapon="''' + str(randomCycleBossArtillery[x-1]) + '''"/>
		<mod:setAttributes weapon="a"/>
	</mod:findLike>
	<mod:findLike type="artillery">
		<mod:selector weapon="''' + str(randomCycleBossArtillery[x]) + '''"/>
		<mod:setAttributes weapon="''' + str(randomCycleBossArtillery[x-1]) + '''"/>
	</mod:findLike>
	<mod:findLike type="artillery">
		<mod:selector weapon="a"/>
		<mod:setAttributes weapon="''' + str(randomCycleBossArtillery[x]) + '''"/>
	</mod:findLike>
	'''
	
	bosses_1 += '''	
</mod:findComposite>'''
	
	
		# events_ship.xml - Crew randomisation
		
	events_ship_1 = '<!--' + str(randomCycleCrew) + '''-->
<mod:findComposite>
	<mod:par op="OR">
		<mod:findWithChildLike type="ship" child-type="crew"/>
	</mod:par>
	
<!-- Player Ship Crew Encryption -->
	<mod:findLike type="crew">'''
		
	for x in range(1, len(randomCycleCrew)):
		events_ship_1 += '''
	<mod:findLike type="crewMember">
		<mod:selector type="''' + str(randomCycleCrew[x-1]) + '''"/>
		<mod:setAttributes type="a"/>
	</mod:findLike>
	<mod:findLike type="crewMember">
		<mod:selector type="''' + str(randomCycleCrew[x]) + '''"/>
		<mod:setAttributes type="''' + str(randomCycleCrew[x-1]) + '''"/>
	</mod:findLike>
	<mod:findLike type="crewMember">
		<mod:selector type="a"/>
		<mod:setAttributes type="''' + str(randomCycleCrew[x]) + '''"/>
	</mod:findLike>'''	
	
	events_ship_1 += '''
	</mod:findLike>
</mod:findComposite>'''
		
		
		# sector_data.xml - Crew randomisation
		
	sector_data_1 = '<!--' + str(randomCycleMinimumSector) + '''-->
<!-- minimum sector appearances -->'''
		
	for x in range(1, len(randomCycleMinimumSector)):
		events_ship_1 += '''
	<mod:findLike>
		<mod:selector minSector="''' + str(randomCycleMinimumSector[x-1]) + '''"/>
		<mod:setAttributes minSector="a"/>
	</mod:findLike>
	<mod:findLike>
		<mod:selector minSector="''' + str(randomCycleMinimumSector[x]) + '''"/>
		<mod:setAttributes minSector="''' + str(randomCycleMinimumSector[x-1]) + '''"/>
	</mod:findLike>
	<mod:findLike>
		<mod:selector minSector="a"/>
		<mod:setAttributes minSector="''' + str(randomCycleMinimumSector[x]) + '''"/>
	</mod:findLike>
	'''	
		
		
		# Event occurrences and sector rarities
		
	sector_data_2 = '<!-- MaxCycle:' + str(randomCycleSectorEventMax) + ' RarityCycle:' + str(randomCycleBlueprintRarity) + '''-->
<mod:findComposite>
	<mod:par op="OR">
		<mod:findLike type="sectorDescription"/>
	</mod:par> '''
		
	for x in range(1, len(randomCycleMinimumSector)):
		sector_data_2 += '''
	<mod:findLike type="event">
		<mod:selector max="''' + str(randomCycleMinimumSector[x-1]) + '''"/>
		<mod:setAttributes max="a"/>
	</mod:findLike>
	<mod:findLike type="event">
		<mod:selector max="''' + str(randomCycleMinimumSector[x]) + '''"/>
		<mod:setAttributes max="''' + str(randomCycleMinimumSector[x-1]) + '''"/>
	</mod:findLike>
	<mod:findLike type="event">
		<mod:selector max="a"/>
		<mod:setAttributes max="''' + str(randomCycleMinimumSector[x]) + '''"/>
	</mod:findLike>
	'''	
		
	sector_data_2 += '''
</mod:findComposite>'''
		
		# sounds.xml - Title Music randomisation
		
	sounds_1 = '<!--' + str(randomCycleTitle) + '''-->
<mod:findLike type="music">
	
	<mod:findWithChildLike type="track" child-type="name">
		<mod:selector>title</mod:selector>'''
		
	for x in range(1, len(randomCycleTitle)):
		sounds_1 += '''
		<mod:findLike type="explore">
			<mod:selector>''' + str(randomCycleTitle[x-1]) + '''</mod:selector>
			<mod:setValue>a</mod:setValue>
		</mod:findLike>
		<mod:findLike type="explore">
			<mod:selector>''' + str(randomCycleTitle[x]) + '''</mod:selector>
			<mod:setValue>''' + str(randomCycleTitle[x-1]) + '''</mod:setValue>
		</mod:findLike>
		<mod:findLike type="explore">
			<mod:selector>a</mod:selector>
			<mod:setValue>''' + str(randomCycleTitle[x]) + '''</mod:setValue>
		</mod:findLike>'''	
	
	sounds_1 += '''
	</mod:findWithChildLike>
</mod:findLike>
		
		'''
		
	blueprintsRandShipFix2 = '''<!-- Player Ship Stuff -->

<mod:findComposite>
    <mod:par op="OR">    
		<mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_ANAEROBIC" /></mod:findLike>
		<mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_ANAEROBIC_2" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_HARD_3" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_STEALTH_3" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_MANTIS_3" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_CIRCLE_3" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_FED_3" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_JELLY_3" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_ROCK_3" /></mod:findLike>
        <mod:findLike type="shipBlueprint"><mod:selector name="PLAYER_SHIP_ENERGY_3" /></mod:findLike>
    </mod:par>
    <mod:removeTag />
</mod:findComposite>
'''
		

	print("Removing Files")
	
	deleteFiles = []
	
	for file in os.walk("compiledFiles"):
		deleteFiles.append(list(file))
		
	for x in range(0, len(deleteFiles)):
		for y in range(0, len(deleteFiles[x][2])):
			if deleteFiles[x][2][y] not in ['metadata.xml']:
				os.remove(deleteFiles[x][0]+'/'+deleteFiles[x][2][y])
	
	for file in os.walk("compiledFiles/img"):
		for x in range(0, len(file[2])):
			os.remove(file[0]+'/'+file[2][x])
	
	extraEquipmentFileTransfer = []
	
	tree = ET.parse('source/Extra Packs/packsInfo.xml')
	root = tree.getroot()
	
	if extraEquipmentCheck:
		print('Copying extra packs')
		for x in range(0, len(extraEquipment)):
			extraEquipmentFileTransfer.append([])
			
			if extraEquipment[x] in [elem.attrib['name'] for elem in root if 'patchAfter' not in [elem2.tag for elem2 in elem if elem2 is not elem]]:
				for file in os.walk("source/Extra Packs/"+extraEquipment[x]):
					extraEquipmentFileTransfer[x].append(list(file))
			
				for z in range(0, len(extraEquipmentFileTransfer[x])):
					extraEquipmentFileTransfer[x][z][0] = extraEquipmentFileTransfer[x][z][0].replace('\\', '/').replace('//', '/')
			
	if os.path.exists('compiledFiles/data') == False:
		os.makedirs('compiledFiles/data')
		
	xml = open("compiledFiles/data/blueprints.xml.append", "w")
	xml.close()
	xml = open("compiledFiles/data/dlcBlueprints.xml.append", "w")
	xml.close()
	xml = open("compiledFiles/data/dlcBlueprintsOverwrite.xml.append", "w")
	xml.close()
	xml = open("compiledFiles/data/autoBlueprints.xml.append", "w")
	xml.close()
	xml = open("compiledFiles/data/animations.xml.append", "w")
	xml.close()
	
	for z in range(0, len(extraEquipmentFileTransfer)):
		for x in range(0, len(extraEquipmentFileTransfer[z])):
			for y in range(0, len(extraEquipmentFileTransfer[z][x][2])):
				if extraEquipmentFileTransfer[z][x][2][y][-11:] == '.xml.append':
					fileAppenda = open(extraEquipmentFileTransfer[z][x][0]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'r')
					fileAppendb = open('compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'a')
		
					fileAppendb.write(fileAppenda.read(10000000))
		
					fileAppenda.close()
					fileAppendb.close()
				elif extraEquipmentFileTransfer[z][x][2][y] != 'AppendArmaments.xml' and extraEquipmentFileTransfer[z][x][2][y].split('.') not in ['pdn', 'xcf']:
					if extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):][:1] == '/':
						if os.path.exists('compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):]) == False:
							os.makedirs('compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):])
						shutil.copy(extraEquipmentFileTransfer[z][x][0]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):])
					else:
						if os.path.exists('compiledFiles/' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0])-1:]) == False:
							os.makedirs('compiledFiles/' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0])-1:])
						shutil.copy(extraEquipmentFileTransfer[z][x][0]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'compiledFiles/' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0])-1:])
	
	transferMod = Mod
	if os.path.exists("source/compatibility/"+transferMod) is False:
		transferMod = 'Vanilla'
	
	print('Copying source files')
	for repeat in range(0, 4):

		transferFiles = []
	
		if repeat == 0:
			for file in os.walk("source/compatibility/Global"):
				transferFiles.append(list(file))
		elif repeat == 1:
			for file in os.walk("source/compatibility/"+transferMod):
				transferFiles.append(list(file))
		elif repeat == 2:
			randNumb = randint(1, 13)
			print('Boss layout: ' + str(randNumb))
			for file in os.walk('source/boss/layouts/'+str(randNumb)):
				transferFiles.append(list(file))
		elif repeat == 3:
			for file in os.walk('source/boss/systems/'+str(randint(1, 3))):
				transferFiles.append(list(file))
	
		for x in range(0, len(transferFiles)):
			transferFiles[x][0] = transferFiles[x][0].replace('\\', '/').replace('//', '/')
			for z in range (0, len(transferFiles[x][2])):
				transferFiles[x][2][z] = transferFiles[x][2][z].replace('\\', '/').replace('//', '/')
				
		#input()
		
		if os.path.exists('compiledFiles/img/ship') == False:
			os.makedirs('compiledFiles/img/ship')
		
		if randShipCheck is True:
			for x in range(0, 10):
				for y in range(0, 2 + int(x<8)):
					if os.path.exists('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'.txt') is True:
						shutil.copy('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'.txt', 'compiledFiles/data')
					else:
						shutil.copy('source/layouts/Vanilla/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'.txt', 'compiledFiles/data')
	
			for x in range(0, 10):
				for y in range(0, 2 + int(x<8)):
					if os.path.exists('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'.xml') is True:
						shutil.copy('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'.xml', 'compiledFiles/data')
					else:
						shutil.copy('source/layouts/Vanilla/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'.xml', 'compiledFiles/data')

	
			for x in range(0, 10):
				if os.path.exists('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])) is True:
					for y in range(0, 2 + int(x<8)):
						shutil.copy('source/layouts/'+str(Mod)+'/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'_floor.png', 'compiledFiles/img/ship')
				else:
					for y in range(0, 2 + int(x<8)):
						shutil.copy('source/layouts/Vanilla/'+str(playerShipOrder[x])+'/'+str(allLayouts[x][y])+'_floor.png', 'compiledFiles/img/ship')
		
		for x in range(0, len(transferFiles)):
			for y in range(0, len(transferFiles[x][2])):
				if transferFiles[x][2][y].split('.')[-1] not in ['pdn', 'xcf'] and transferFiles[x][2][y] not in ['playerImgOrder.xml']:
					if transferFiles[x][2][y][-11:] == '.xml.append':
						if 'boss' in transferFiles[x][2][y]:
							fileAppenda = open(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'r')
							fileAppendb = open('compiledFiles/data/' + transferFiles[x][0][len(transferFiles[0][0]):]+'/'+transferFiles[x][2][y], 'a')
			
							fileAppendb.write(fileAppenda.read(10000000))
			
							fileAppenda.close()
							fileAppendb.close()
						
						else:
							fileAppenda = open(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'r')
							fileAppendb = open('compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0]):]+'/'+transferFiles[x][2][y], 'a')
			
							fileAppendb.write(fileAppenda.read(10000000))
			
							fileAppenda.close()
							fileAppendb.close()
					elif 'boss' in transferFiles[x][2][y] and transferFiles[x][2][y][-4:] == '.txt':
						shutil.copy(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'compiledFiles/data' + transferFiles[x][0][len(transferFiles[0][0]):]+'/'+transferFiles[x][2][y])
					elif ('_shields1' in transferFiles[x][2][y] or '_base' in transferFiles[x][2][y] or '_gib' in transferFiles[x][2][y] or 'miniship' in transferFiles[x][2][y]) and 'boss' not in transferFiles[x][2][y]:
						if randShipCheck is True:
							for z in range(0, len(randomCyclePlayerHull)):
								if str(playerImgOrder[z]) in transferFiles[x][2][y]:
									for a in range(1, len(randomCyclePlayerHull[z])+1):
										if str(a) in randomCyclePlayerHull[z][:3 - int(z > 7)] and str(shipTypeId[a-1]) in transferFiles[x][2][y][:-5] and '_gib' in transferFiles[x][2][y]:
											if transferFiles[x][0][len(transferFiles[0][0]):][:1] == '/':
												if os.path.exists('compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):]) == False:
													os.makedirs('compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):])
												shutil.copy(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):])
											else:
												if os.path.exists('compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0]):]) == False:
													os.makedirs('compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0]):])
												shutil.copy(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0]):])
										elif str(a) in randomCyclePlayerHull[z][:3 - int(z > 7)] and str(shipTypeId[a-1]) in transferFiles[x][2][y] and '_gib' not in transferFiles[x][2][y]:
											if transferFiles[x][0][len(transferFiles[0][0]):][:1] == '/':
												if os.path.exists('compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):]) == False:
													os.makedirs('compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):])
												shutil.copy(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):])
											else:
												if os.path.exists('compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0])-1:]) == False:
													os.makedirs('compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0])-1:])
												shutil.copy(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0])-1:])
					else:
						if transferFiles[x][0][len(transferFiles[0][0]):][:1] == '/':
							if os.path.exists('compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):]) == False:
								os.makedirs('compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):])
							shutil.copy(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'compiledFiles' + transferFiles[x][0][len(transferFiles[0][0]):])
						else:
							if os.path.exists('compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0])-1:]) == False:
								os.makedirs('compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0])-1:])
							shutil.copy(transferFiles[x][0]+'/'+transferFiles[x][2][y], 'compiledFiles/' + transferFiles[x][0][len(transferFiles[0][0])-1:])
		
	
	print('Exporting written code')
	xml = open("source/boss/layouts/bosses.xml", "r")
	bosses_0 = str(xml.read(100000))
	xml.close()
	
	xml = open("compiledFiles/data/bosses.xml.append", "w")
	xml.writelines(bosses_0)
	xml.writelines(bosses_1)
	xml.close()
	
	xml = open("compiledFiles/data/sounds.xml.append", "w")
	xml.writelines(sounds_1)
	xml.close()
	
	xml = open("compiledFiles/data/events_ships.xml.append", "w")
	xml.writelines(events_ship_1)
	xml.close()
	
	xml = open("compiledFiles/data/sector_data.xml.append", "w")
	xml.writelines(sector_data_1)
	xml.writelines(sector_data_2)
	xml.close()
	
	xml = open("compiledFiles/data/autoBlueprints.xml.append", "a")
	xml.writelines(blueprints_1)
	xml.close()
	
	xml = open("compiledFiles/data/blueprints.xml.append", "a")
	
	xml.writelines(blueprints_ships)
	
	xml.writelines(blueprints_1)
	xml.writelines(blueprints_2)
	xml.writelines(blueprints_3)
	xml.writelines(blueprints_5)
	xml.writelines(blueprints_6)
	xml.writelines(blueprints_7)
	
	xml.close()
	
	xml = open("compiledFiles/data/dlcBlueprints.xml.append", "a")
	
	if randShipCheck is True:
		xml.writelines(blueprintsRandShipFix2)
	
	xml.writelines(blueprints_1)
	xml.writelines(blueprints_2)
	xml.writelines(blueprints_3)
	xml.writelines(blueprints_5)
	xml.writelines(blueprints_6)
	xml.writelines(blueprints_7)
	
	xml.close()
	
	xml = open("compiledFiles/data/dlcBlueprintsOverwrite.xml.append", "a")
	
	if randShipCheck is True:
		xml.writelines(blueprintsRandShipFix2)
	
	xml.writelines(blueprints_1)
	xml.writelines(blueprints_2)
	xml.writelines(blueprints_3)
	xml.writelines(blueprints_5)
	xml.writelines(blueprints_6)
	xml.writelines(blueprints_7)
	
	xml.close()
	
	extraEquipmentFileTransfer = []
		
	if extraEquipmentCheck:
		print('Copying more extra packs')
		for x in range(0, len(extraEquipment)):
			extraEquipmentFileTransfer.append([])
			
			if extraEquipment[x] in [elem.attrib['name'] for elem in root if 'patchAfter' in [elem2.tag for elem2 in elem if elem2 is not elem]]:
				for file in os.walk("source/Extra Packs/"+extraEquipment[x]):
					extraEquipmentFileTransfer[x].append(list(file))
			
				for z in range(0, len(extraEquipmentFileTransfer[x])):
					extraEquipmentFileTransfer[x][z][0] = extraEquipmentFileTransfer[x][z][0].replace('\\', '/').replace('//', '/')
		
		for z in range(0, len(extraEquipmentFileTransfer)):
			for x in range(0, len(extraEquipmentFileTransfer[z])):
				for y in range(0, len(extraEquipmentFileTransfer[z][x][2])):
					if extraEquipmentFileTransfer[z][x][2][y][-11:] == '.xml.append':
						fileAppenda = open(extraEquipmentFileTransfer[z][x][0]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'r')
						fileAppendb = open('compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'a')
			
						fileAppendb.write(fileAppenda.read(10000000))
			
						fileAppenda.close()
						fileAppendb.close()
					elif extraEquipmentFileTransfer[z][x][2][y] != 'AppendArmaments.xml' and extraEquipmentFileTransfer[z][x][2][y].split('.') not in ['pdn', 'xcf']:
						if extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):][:1] == '/':
							if os.path.exists('compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):]) == False:
								os.makedirs('compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):])
							shutil.copy(extraEquipmentFileTransfer[z][x][0]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'compiledFiles' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0]):])
						else:
							if os.path.exists('compiledFiles/' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0])-1:]) == False:
								os.makedirs('compiledFiles/' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0])-1:])
							shutil.copy(extraEquipmentFileTransfer[z][x][0]+'/'+extraEquipmentFileTransfer[z][x][2][y], 'compiledFiles/' + extraEquipmentFileTransfer[z][x][0][len(extraEquipmentFileTransfer[z][0][0])-1:])
	

print("loaded!")



