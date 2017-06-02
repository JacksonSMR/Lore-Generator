#Lore Generator v1.0.2 alpha

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

area = ["forest", "desert", "city", "cave"]

prefixCount = len(prefix)
suffixCount = len(suffix)
titleCount = len(title)
areaCount = len(area)
raceCount = 5
vowelCount = 5

comboCount = prefixCount * vowelCount * suffixCount
comboCountTotal = comboCount * titleCount * raceCount

worldCreated = False

print ("Prefixes: ", prefixCount)
print ("Suffixes: ", suffixCount)
print ("Titles: ", titleCount)
print ("Races: ", raceCount)
print ("Total unique names: ", comboCount)
print ("Total unique names w/ titles and races: ", comboCountTotal)
input("Press any key to continue.")

tmp = sp.call('cls', shell = True)

def characterGen():
	
	prefixChoice = r.randint(0, 180) 
	vowelChoice = r.randint(0, 4)
	suffixChoice = r.randint(0, 54)
	titleChoice = r.randint(0, 21)
	raceChoice = r.randint(0, 4)
	
	return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice] + " the " + title[titleChoice] + ", " + race[raceChoice]
	
def worldGen():

	prefixChoice = r.randint(0, 180)
	vowelChoice = r.randint(0, 4)
	suffixChoice = r.randint(0, 54)
		
	return prefix[prefixChoice] + vowel[vowelChoice] + suffix[suffixChoice]

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
		
		name = characterGen()
		print(name)

	if cmd == "create world" or cmd == "cw":
		
		filename = worldName + ".dat"
		worldfile = open(filename, "w")
		worldfile.close()
		
		worldCreated = True
		
	while worldCreated == True:
	
		tmp = cls()

		print("The World of " + worldName)
		print("")
		cmd = input(">> ")
		
		if cmd == "create hero" or cmd == "ch":
		
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
					
					break
					
				worldfile.write("hero")
				worldfile.write(heroName, heroRace)
				
				print("You are ", heroName, ", the ", heroRace)
			
			elif nameQ == "random":
				
				heroName = characterGen()
				worldfile.write("hero")
				worldfile.write(heroName)
				
				print("You are ", heroName, ".")
			
			else:
				
				print("Error")
				break
		
		worldfile = open(filename, "r")
		
		if (cmd == "begin story" or cmd == "bs") and worldfile.read(1) == "hero":
			
			story = True
			x = 0
			
		
		while story == True:
			
			if x == 0:
				
				storyStart()
			
