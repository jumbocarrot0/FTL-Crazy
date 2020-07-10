#!/usr/bin/env pythonfrom tkinter import *from programAssets import Randomiserfrom shutil import make_archive, moveimport osfrom pathlib import PathinfoTxt = open('programAssets/info.txt', 'r')info = infoTxt.readlines(100000)infoTxt.close()for x in range(0, len(info)):	if '\n' in info[x]:		info[x] = info[x][:-1]print(info)absolPath = Path(os.path.abspath('FTLRand.py'))print('Mod will be generated in: ' + str(absolPath.parent))		def extraOptions():	def togglePower():		global equipPower		equipPower = not equipPower		if equipPower is True:			btnPower.config(text='X')		else:			btnPower.config(text=' ')		print(equipPower)	def toggleDamage():		global equipDamage		equipDamage = not equipDamage		if equipDamage is True:			btnDamage.config(text='X')		else:			btnDamage.config(text=' ')		print(equipDamage)			win_options = Tk()	win_options.geometry('370x300')	win_options.title('More Options')	win_options.resizable(0, 0)	fr_main = Frame(win_options, width=400, height=600, relief='raised', borderwidth=0)	fr_main.grid(row=0, column=0)	fr_main.grid_propagate(0)	menuModText = StringVar(win_options)	menuModText.set(info[0])	monoFont = 'Courier 12'	lblFont = '48'	lblPower = Label(fr_main, text='Change Equipment Power', font=lblFont)	btnPower = Button(fr_main, text='X', font=monoFont, command=togglePower)	lblDamage = Label(fr_main, text='Change Weapon Damage', font=lblFont)	btnDamage = Button(fr_main, text='X', font=monoFont, command=toggleDamage)		lblPower.grid(row=0, column=0, sticky=(W + E), pady=5, padx=2)	btnPower.grid(row=0, column=1, pady=5, padx=2)	lblDamage.grid(row=1, column=0, sticky=(W + E), pady=5, padx=2)	btnDamage.grid(row=1, column=1, pady=5, padx=2)		win_options.mainloop()def btnGenerateMod():	print('Seed: ' + str(entrySeed.get()))	Randomiser.generateRandMod(menuModText.get(), balanced, entrySeed.get(), extraEquipment, randShip, equipPower, equipDamage)		Mod = menuModText.get()	make_archive('FTLRand' + Mod, 'zip', 'compiledFiles')	print('Archived')		if os.path.exists(str(absolPath.parent) + '/' + 'FTLRand' + Mod + '.ftl') is True:		os.remove(str(absolPath.parent) + '/' + 'FTLRand' + Mod + '.ftl')		print('Existing Archive Removed')			p = Path('FTLRand' + Mod + '.zip')	p.rename(p.with_suffix('.ftl'))	print('Renamed')		#move('FTLRand' + Mod + '.ftl', absolPath.parent)	print('Done!')		print("Saved to executable's parent directory, mod located at " + str(absolPath.parent))		infoTxt = open('programAssets/info.txt', 'w')	infoTxt.write(str(menuModText.get()) + '\n')	infoTxt.write(str(balanced) + '\n')	infoTxt.write(str(randShip) + '\n')	infoTxt.close()def btnQuit():	main.quit()def toggleBalance():	global balanced	balanced = not balanced	if balanced is True:		btnBalance.config(text='X')	else:		btnBalance.config(text=' ')def toggleExtra():	global extra	extra = not extra	if extra is True:		btnExtra.config(text='X')	else:		btnExtra.config(text=' ')def toggleEquipment():	global extraEquipment	extraEquipment = not extraEquipment	if extraEquipment is True:		btnEquipment.config(text='X')	else:		btnEquipment.config(text=' ')	print(extraEquipment)def toggleHyperspace():	global hyperspace	hyperspace = not hyperspace	if hyperspace is True:		btnHyp.config(text='X')	else:		btnHyp.config(text=' ')def toggleShip():	global randShip	randShip = not randShip	if randShip is True:		btnShip.config(text='X')	else:		btnShip.config(text=' ')main = Tk()main.geometry('370x350')main.title('FTL:Crazy')main.resizable(0, 0)fr_main = Frame(main, width=400, height=600, relief='raised', borderwidth=0)#fr_img = Frame(main, width=400, height=600, relief='raised', borderwidth=0)fr_main.grid(row=0, column=0)fr_main.grid_propagate(0)#fr_img.grid(row=0, column=1)#fr_img.grid_propagate(0)'''image = 'programAssets/miniship_kestral_' + str(randint(4, 6)) + '.png'background_image = PhotoImage(file=image)backgroundLbl = Label(fr_img, image=background_image)backgroundLbl.grid(row=0, column=0)'''menuModText = StringVar(main)menuModText.set(info[0])monoFont = 'Courier 12'lblFont = '48'mod_options = []for (dirpath, dirnames, filenames) in os.walk('source\compatibility'):	del dirnames[dirnames.index('Global')]	mod_options.extend(dirnames)	break#menuMod = OptionMenu(fr_main, menuModText, 'Vanilla', 'Stations Job', 'CE', 'Arsenal+', 'SMPK')menuMod = OptionMenu(fr_main, menuModText, *mod_options)menuMod.config(borderwidth=2, font='48')lblBalance = Label(fr_main, text='Balanced', font=lblFont)btnBalance = Button(fr_main, text='X', font=monoFont, command=toggleBalance)btnGen = Button(fr_main, text='Generate Mod', command=btnGenerateMod, font='72', height=2, width=15)lblSeed = Label(fr_main, text='Random Seed:', font=lblFont)entrySeed = Entry(fr_main, font=lblFont)lblShip = Label(fr_main, text='Randomize Player Ships', font=lblFont)btnShip = Button(fr_main, text='X', font=monoFont, command=toggleShip)#lblExtra = Label(fr_main, text='Warped Space', font=lblFont)#btnExtra = Button(fr_main, text=' ', font=monoFont, command=toggleExtra)lblEquipment = Label(fr_main, text='Extra Packs', font=lblFont)btnEquipment = Button(fr_main, text=' ', font=monoFont, command=toggleEquipment)btnOptions = Button(fr_main, text='More Options', command=extraOptions, font='72')menuMod.grid(row=0, column=0, columnspan=2, sticky=(W + E), pady=5, padx=2)lblBalance.grid(row=1, column=0, sticky=(W + E), pady=5, padx=2)btnBalance.grid(row=1, column=1, pady=5, padx=2)lblSeed.grid(row=3, column=0, sticky=(W + E), pady=5, padx=2)entrySeed.grid(row=3, column=1, sticky=(W + E), pady=5, padx=2)lblShip.grid(row=4, column=0, sticky=(W + E), pady=5, padx=2)btnShip.grid(row=4, column=1, pady=5, padx=2)#lblExtra.grid(row=5, column=0, sticky=(W + E), pady=5, padx=2)#btnExtra.grid(row=5, column=1, pady=5, padx=2)lblEquipment.grid(row=6, column=0, sticky=(W + E), pady=5, padx=2)btnEquipment.grid(row=6, column=1, pady=5, padx=2)btnGen.grid(row=7, column=0, columnspan=2, sticky=(W + E), pady=5, padx=2)btnOptions.grid(row=9, column=0, columnspan=2, sticky=(W + E), pady=5, padx=2)extra = FalseextraEquipment = Falsehyperspace = FalserandShip = FalseequipPower = TrueequipDamage = Trueif info[1] == 'True':	balanced = True	btnBalance.config(text='X')else:	balanced = False	btnBalance.config(text=' ')if info[2] == 'True':	randShip = True	btnShip.config(text='X')else:	randShip = False	btnShip.config(text=' ')main.mainloop()