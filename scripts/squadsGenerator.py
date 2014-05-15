# -*- coding: utf-8 -*-
import re, sys, os, json

# Config
squadKeys = ["bra", "cmr", "cro", "mex", "aus", "chi", "ned", "esp", "col", "civ", "gre", "jpn", "crc", "eng", "ita", "uru", "ecu", "fra", "hon", "sui", "arg", "bih", "irn", "nga", "ger", "gha", "por", "usa", "alg", "bel", "rus", "kor"]
file = "squads.wiki"

# Patters config
playerPattern = "{{nat fs( g)? player.*$"
captainPattern = "(\'\')?\((\'\')?\[\[[C|c]aptain \(association football\)(\|.*)?\]\](\'\')?\)(\'\')?"
namePattern = "\|name\s*=\s*\[\[(.*\|)?(.+)\]\]\s*(%s)?\s*\|age" % captainPattern
numberPattern = "\|no\s*=\s*(\d+)\s*\|"
posPattern = "\|pos\s*=\s*(\w+)\s*\|"
capsPattern = "\|caps\s*=\s*(\d+)\s*\|"
coachPattern = "(Manager|Coach):.*\[\[(.*)\]\]"

if not os.path.exists("squads"):
    os.makedirs("squads")


# Init
squadPlayers = []
squadIndex = 0
squadCoach = None

for line in open(file).readlines():
	m = re.match(coachPattern, line)
	if m:
		if (len(squadPlayers) > 0):
			file_name = "squads/squad-%s.json" % squadKeys[squadIndex]
			with open(file_name, 'w') as outfile:
				json.dump({"coach": squadCoach, "players": squadPlayers}, outfile, sort_keys=True, indent=4)

			squadPlayers = []
			squadIndex = squadIndex + 1	

		squadCoach = m.group(2)			
		continue

	m = re.match(playerPattern, line)
	if m:
		player = {}		
		playerLine = m.group(0)

		m = re.search(namePattern, playerLine)
		if m:
			player["name"] = m.group(2)
			if m.group(3):
				player["captain"] = True
			else:
				player["captain"] = False
		else:
			print playerLine

		player["number"] = 0
		m = re.search(numberPattern, playerLine)
		if m:
			player["number"] = int(m.group(1))

		m = re.search(posPattern, playerLine)
		if m:
			player["position"]  = m.group(1)

		player["caps"] = 0
		m = re.search(capsPattern, playerLine)
		if m:
			player["caps"]  = int(m.group(1))			

		print "%s | %s | %s | %s | %s" % ( repr(player["number"]).rjust(2), player["position"], player["name"].ljust(30), "(C)" if player["captain"] else "   ", player["caps"] )

		squadPlayers.append(player)






