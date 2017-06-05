#Lore Generator v1.0.6 alpha

print("Loading... ")

import ctypes
import math
import random as r
import subprocess as sp
import turtle

ctypes.windll.kernel32.SetConsoleTitleW("Lore Generator")

#Prefix List

prefix = ["Ad", "Adr", "Adu", "Aeg", "Ad", "Agl", "Adl", "Ald", "Am", "Ama", "Amb", "Aml", "Amr", 
"An", "Anb", "Anc", "And", "Ang", "App", "Ar", "Arc", "Arg", "Ark", "Arn", "Art", "Arv", "Arw", 
"Ash", "Aul", "Ave", "Az", "Bai", "Bal", "Bam", "Ban", "Bar", "Be", "Bel", "Bem", "Ber", "Bet", 
"Bif", "Bil", "Bir", "Bof", "Bol", "Bom", "Bor", "Br", "Bro", "Bru", "Bry", "By", "Cai", "Cal", 
"Car", "Cas", "Cau", "Cav", "Cel", "Cem", "Ceo", "Cer", "Ch", "Cir", "Cit", "Cl", "Col", "Com", 
"Cor", "Cri", "Cur", "Da", "Dag", "Dal", "Dam", "Den", "Deo", "Der", "Di", "Dim", "Dir", "Dr", 
"Du", "Dun", "Dur", "Dw", "Ear", "Ecth", "Ed", "Eg", "Eil", "Elb", "Eld", "Elen", "Eles", "Ell", 
"Elr", "En", "Eom", "Er", "Erl", "Err", "Eth", "Fal", "Fang", "Far", "Fas", "Fe", "Fla", "Flo",
"For", "Fr", "Gal", "Gan", "Gh", "Gil", "Gl", "Gol", "Gon", "Goth", "Gr", "Gun", "Guth", "Gw", 
"Had", "Hal", "Har", "Hol", "Hur", "Hy", "Iml", "Imr", "Isil", "Lug", "Mar", "Mat", "Mau", "Mich", 
"Min", "Mor", "Na", "Nan", "Nel", "Num", "Nur", "Or", "Orth", "Pal", "Par", "Pel", "Pen", "Ra", 
"Reu", "Rhu", "Rid", "Riv", "Roh", "Rom", "Rop", "Sar", "Sau", "Sin", "Sil", "Sir", "Tar", "Tas", 
"Th", "Tum", "Tur", "Unb", "Ung", "Ur", "Val", "Vid", "Vil", "Vin", "Vor", "Wain", "Wal", "Zir"]

vowel = ["a", "e", "i", "o", "u"]

suffix = ["lome", "mir", "ndil", "in", "th", "rn", "un", "thas", "cil", "ll", "lmoth", "rdene", 
"bor", "rith", "ras", "dil", "lmir", "nd", "irn", "stur", "dhol", "red", "thil", "rin", "fel", 
"drim", "berg", "bault", "rad", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

title = ["Bold", "Strong", "Wise", "Kind", "Cruel", "Strange", "Temperate", "Traveller",
"Competitive", "Brave", "Honourable", "Deceitful", "Greedy", "Gluttonous", "Old", "Young",
"Tall", "Short", "Stout", "Large", "Gallant", "Builder", "Painter", "Cleric", "Musical",
"Enlightened", "Devious", "Charming", "Decrepit", "Paranoid", "Mystical", "Soft-Hearted"]

race = ["Elf", "Dwarf", "Human", "Halfling", "Orc"]

area = ["Forest", "Desert", "City", "Caves", "Plains"]

collective = ["City", "Army", "Horde", "Duchy", "Kingdom", "Empire"]

action = ["attacks", "invades", "falls to", "surrenders to", "makes peace with", "forms from"]

prefixCount = len(prefix)
suffixCount = len(suffix)
titleCount = len(title)
areaCount = len(area)
collectiveCount = len(collective)
actionCount = len(action)
raceCount = 5
vowelCount = 5

comboCount = prefixCount * vowelCount * suffixCount
comboCountTotal = comboCount * titleCount * raceCount

worldCreated = False
story = False
name = False
nameSelect = False
charCreate = False
historyDone = False
historyCreated = False
viewOver = False

tmp = sp.call('cls', shell = True)

print ("Prefixes: ", prefixCount)
print ("Suffixes: ", suffixCount)
print ("Titles: ", titleCount)
print ("Races: ", raceCount)
print ("Total unique names: ", comboCount)
print ("Total unique names w/ titles and races: ", comboCountTotal)
input("Press any key to continue.")

tmp = sp.call('cls', shell = True)

def characterGen(charCreate):
	
	prefixChoice = r.randint(0, 180) 
	vowelChoice = r.randint(0, 4)
	suffixChoice = r.randint(0, 54)
	titleChoice = r.randint(0, 21)
	raceChoice = r.randint(0, 4)
	
	if charCreate == True:
		
		heroRace = raceChoice
		charCreate = False
	
	return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
def newNameGen():
	
	print("What is your name?")
	regName = input(">> ")
	
	nameSelect = True
	x = 0
	
	while nameSelect == True:
	
		if regName[x] == "a":
		
			prefixChoice = r.randint(0, 30)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "b":
		
			prefixChoice = r.randint(31, 52)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "c":
		
			prefixChoice = r.randint(53, 71)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "d":
		
			prefixChoice = r.randint(72, 87)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "e":
		
			prefixChoice = r.randint(88, 104)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "f":
		
			prefixChoice = r.randint(105, 113)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "g":
		
			prefixChoice = r.randint(114, 125)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "h":
		
			prefixChoice = r.randint(126, 131)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
		elif regName[x] == "i":
		
			prefixChoice = r.randint(132, 134)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "l":
		
			prefixChoice = 135
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "m":
		
			prefixChoice = r.randint(136, 141)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "n":
		
			prefixChoice = r.randint(142, 146)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "o":
		
			prefixChoice = r.randint(147, 148)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "p":
		
			prefixChoice = r.randint(149, 152)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "r":
		
			prefixChoice = r.randint(153, 160)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "s":
		
			prefixChoice = r.randint(161, 165)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "t":
		
			prefixChoice = r.randint(166, 170)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "u":
		
			prefixChoice = r.randint(171, 173)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "v":
		
			prefixChoice = r.randint(174, 178)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "w":
		
			prefixChoice = r.randint(179, 180)
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		elif regName[x] == "z":
		
			prefixChoice = 181
			vowelChoice = r.randint(0, 4)
			suffixChoice = r.randint(0, 54)
			titleChoice = r.randint(0, 21)
			raceChoice = r.randint(0, 4)
			
			return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
		
		else:
			
			x += 1
			
			if x > len(regName):
				
				print("Error")
				break
	
def worldGen():

	prefixChoice = r.randint(0, 180)
	vowelChoice = r.randint(0, 4)
	suffixChoice = r.randint(0, 54)
		
	return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice]

	
def historyGen(worldName):

	year = 1
	history = []
	
	print("How many years of history shall be generated?")
	endYear = input(">> ")
	
	while year <= int(endYear):
	
		collectiveChoice = r.randint(0, 5)
		prefixChoice = r.randint(0, 180) 
		vowelChoice = r.randint(0, 4)
		suffixChoice = r.randint(0, 54)
		
		main = "The " + collective[collectiveChoice] + " of " + prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice]
		
		collectiveChoice = r.randint(0, 5)
		prefixChoice = r.randint(0, 180) 
		vowelChoice = r.randint(0, 4)
		suffixChoice = r.randint(0, 54)
		
		next = "The " + collective[collectiveChoice] + " of " + prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice]
		
		actionChoice = r.randint(0, 5)
		
		historyPart = main + " " + action[actionChoice] + " " + next
		
		print (str(year) + ": " + historyPart)
		
		history.append(historyPart)
			
		year += 1
	
	print ("Generation complete.")
	print ("Database constructed.")
			
	historyCreated = True
			
	return history
		
def storyStart(worldName, heroName):
	
	print("Welcome, ", heroName, " to the world of ", worldName, ".")
	print("")
	input("Press key to continue")
	
	clear()
	
	areaRand = r.randint(0, 3)
	areaChoice = area[areaRand]
	
	prefixChoice = r.randint(0, 180)
	vowelChoice = r.randint(0, 4)
	suffixChoice = r.randint(0, 54)
	areaName = prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice]
	
	print("You begin in the ", areaChoice, " of ", areaName, ".")
	print("")
	input("Press key to continue")
	
	clear()

def clear():
	
	sp.call('cls', shell = True)

while True:

	tmp = clear()
	cmd = input(">> ")

	if cmd == "create person" or cmd == "cp":
		
		name = characterGen(False)
		print(name)
		print("")
		input("Press key to continue")
		
	if cmd == "make name" or cmd == "mn":
	
		name = newNameGen()
		print(name)
		print("")
		input("Press key to continue")

	if cmd == "create world" or cmd == "cw":
		
		worldCreated = True
		worldName = worldGen()
		
	while worldCreated == True:
	
		tmp = clear()

		if name == False:
		
			print("The World of " + worldName)
			print("")
			cmd = input(">> ")
			
		if name == True:
		
			print("The World of " + worldName)
			print("")
			print("You are", heroName, ", the ", heroRace)
			cmd = input(">> ")
		
		if cmd == "create history" or cmd == "chis":
			
			totalLore = historyGen(worldName)
			
			print("History created.")
			print("")
			input("Press key to continue")
		
		if (cmd == "view history" or cmd == "vh") and historyCreated == True:
		
			while viewOver == False:
			
				tmp = clear()
				
				print("Enter year")
				cmd = input(">> ")
				
				if cmd == "over":
					
					viewOver = True
		
				year = str(cmd)
				
				print(history[year])
				print("")
				input("Press key to continue")
				
		if cmd == "create hero" or cmd == "chero":
		
			print("Custom or random name?")
			nameQ = input(">> ")
			
			if nameQ == "custom":
				
				print("Enter name:")
				heroName = input(">> ")
				
				print("Choose race:")
				print("")
				print("1: Elf")
				print("2: Dwarf")
				print("3: Human")
				print("4: Halfling")
				print("5: Orc")
				
				userRace = input(">> ")
				
				if userRace == "1":
					
					heroRace = "Elf"
				
				elif userRace == "2":
					
					heroRace = "Dwarf"
				
				elif userRace == "3":
					
					heroRace = "Human"
				
				elif userRace == "4":
					
					heroRace = "Halfling"
				
				elif userRace == "5":
					
					heroRace = "Orc"
				
				else:
					
					print("Error")
					break
				
				name = True
				
				print("You are", heroName, ", the ", heroRace)
				print("")
				input("Press key to continue")
			
			elif nameQ == "random":
				
				heroName = characterGen(True)
				
				name = True
				
				print("You are ", heroName, ".")
				print("")
				input("Press key to continue")
			
			else:
				
				print("Error")
				break
