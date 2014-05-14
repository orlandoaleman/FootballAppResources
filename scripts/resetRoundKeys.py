# -*- coding: utf-8 -*-
import json
from config import *

# --- Anado las claves faltantes
for i in iter(range(1, numberOfRounds+1)):
	file_name = "round%d.json" % i
	json_f = json.load(open(file_name))

	# Key-Default
	addKeys = {'team1_slot': None, 'team2_slot': None, "title": None, "score2p": None}
	
	# Key-NewValue
	updateKeys = {}

	# Keys
	removeKeys = []

	for match in iter(json_f["games"]):
		for key, value in addKeys.iteritems():			
			if key not in match:
				match[key] = value		

		for key, value in updateKeys.iteritems():			
			match[key] = value

		for key in removeKeys:	
			match.pop(key, None)

	with open(file_name, 'w') as outfile:
  		json.dump(json_f, outfile, sort_keys=True, indent=4)
