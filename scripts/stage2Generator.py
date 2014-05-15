# -*- coding: utf-8 -*-
import json
from config import *

pairings = []

file_name = "round%d.json" % (roundsInGroupPhase+1)
json_f = json.load(open(file_name))

for match in iter(json_f["games"]):
	slot1 = match["team1_slot"]
	slot2 = match["team2_slot"]	
	pairings.append((slot1, slot2))

file_name = "stage2-pairings.json"
with open(file_name, 'w') as outfile:
	json.dump({"pairings": pairings}, outfile, sort_keys=True, indent=4)
