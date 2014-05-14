# -*- coding: utf-8 -*-
import json
from config import *

groups = {"A": [], 
		  "B": [],
		  "C": [], 
		  "D": []}
usedKey = "team1_title"	  

for round_i in iter(range(1, roundsInGroupPhase+1)):
	file_name = "round%d.json" % round_i
	json_f = json.load(open(file_name))

	for match in iter(json_f["games"]):
		for groupName, teams in groups.iteritems():			
		    if match[usedKey] in teams:
		    	match.update({"group": groupName})
		        break

	with open(file_name, 'w') as outfile:
		json.dump(json_f, outfile, sort_keys=True, indent=4)
