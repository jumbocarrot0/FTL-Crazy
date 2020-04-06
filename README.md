#	 _______________   _______________    _____
#	|               | |               |  |     |
#	|      _________| |____       ____|  |     |
#	|     |                |     |       |     |
#	|     |______          |     |       |     |
#	|            |         |     |       |     |
#	|      ______|         |     |       |     |
#	|     |                |     |       |     |
#	|     |                |     |       |     |________            
#	|     |                |     |       |              |
#	|_____|                |_____|       |______________|
#
#	        _____   _____   _____   _____   _   _
#	       |  ___| |  _  | |  _  | |___  | | |_| |
#	       | |___  |    _| |  _  |  __/ /  |_   _|
#	       |_____| |_|\_\  |_| |_| |_____|   |_|
#


##Contents

- Acknowledgements
- What is This
- How to Use
- Customisation


##Acknowledgements

Thanks to Gencool, for his Sensory Deprivation mod that gave me the idea in the first place.
Thanks to Kix, for lending me some of his Federation and Slug player ship hulls.


##What is This

FTL: Crazy is a randomising tool for FTL:Faster than Light, inspired mainly by the layout randomiser in Gencool's Sensory Deprivation mod.


##How to Use

This is not a conventional .ftl mod, but it is instead a randomiser that creates a .ftl file that can be used as a standard mod.
To use, simply execute the FTLRand file. It should load up a window with a simple user interface. Here, you can change various settings, including balance and extra additions.
Versions for various Overhaul mods are also avaliable, however the randomiser should be able to generate a mod that can be used alongside most smaller mods. Simply just put this mod ahead of any mods that you want to be randomised.
Clicking the Generate button will create a .ftl file. Patch this file into the game with Slipstream Mod Manager. If there is already a copy of that .ftl in this directory, it will be overwritten.
The source files this the mod can be seen in the compiledFiles folder. The other folders are for the functionality of the randomiser and shouldn't be tinkered with unless you know what you're doing.


##Customisation

This randomiser is also designed to be customisable by the user to add new content that can appear. The source folder contains all the possible assets that could be used in a randomised mod, all contained within various subfolders. 
The following is a list of each subfolder in alphabetical order, their utility and how they can be customised. The information regarding each subfolder can also be seen in the said subfolder.

####Compatability
This contains several subfolders, most relating to a specific overhaul that this randomiser has a compatibility variation for. It also contains Vanilla, used for vanilla versions, and Global, which is always used. The randomiser takes all the images in the certain folder relating to which overhaul it's set to and all images from Global.
If an overhaul is not listed, the randomiser will use vanilla.
Each subfolder is formated like a standard mod.
If you want to add to an overhaul that does not currently have a designated subfolder, you have to create it before adding on to it. The created folder has to have the same name as the one listed in the overhauls dropdown menu on the program, case sensitive
To add onto this section, simply add onto the required subfolder like you would in a standard mod.

####Extra Events
Contains several folders. Each contain the source of certain additional mods that can be added into the randomised mod. Generally, these include new events, new races or factions, but can technically contain anything. The randomiser will randomly pick some of these to be included in the randomised mod if the Extra Events toggle is on.
To add onto this section, simply add a new subfolder in the Extra Events folder, and include any files you need for the mod to function in that subfolder. This should be organised similarly to a normal mod, with audio, data, fonts and img folders included if used.

####Extra Equipment
Like Extra Events, except these mods include additional ship equipment, and is only included if the Extra Equipment toggle is on. The difference is that each subfolder include a shipArmaments folder alongside the standard mod folders. This folder works like the shipArmaments folder under the source folder. How the shipArmaments folder works will be explained later in this document.
Adding on to this section works like with Extra Events, excpet that you can also include a shipArmaments folder with the relevent files included.

####Hyperspace
The contents of this folder are added onto the randomised mod if the Hyperspace Features toggle is on.
To add on to this section, simply edit the contents of the folder like with a standard mod.

####layouts
This contains 10 subfolders, each relating to each ship type. Each of these subfolders contains the relevent data for new ship layouts. Each ship layout required 4 files, which are copied into the randomised mod. 
The .txt file is the ship layout file. It is formatted exactly the same as in the game files.
The xml file ending in _blue contains the ship blueprint. This is copied into the randomised mod as well. The ship blueprint in these files only contains the systems tag, the desc tag and the name tag, and will be mostly overwritten. This file is only for defining which system goes into which room and their interior difference.
The xml file not ending in _blue is the other ship layout file, formatted like in the game files.
The .img file is the floor image.
All of these files are fomatted 'kestral_X' at the start, with the ship name instead of kestral and X replaced with a certain number.
To add onto this section, simply include the relevant files and rename them to the required format.

####names
This section contains several text files including possible names for each ship type. 'bird.txt' is the only unclear one, which is used for Kestel, Federation, Stealth and Lanius cruisers.
To add onto this section, simply add the new names on the end of the relevent text files.


