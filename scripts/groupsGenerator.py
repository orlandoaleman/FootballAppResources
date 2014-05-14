# -*- coding: utf-8 -*-
import json
from config import *

groups = {}  

# --- Saco los grupos
for i in iter(range(1, roundsInGroupPhase+1)):
	file_name = "round%d.json" % i
	json_f = json.load(open(file_name))	

	for match in iter(json_f["games"]):
		group = match["group"]
		if group not in groups:
			groups[group] = []

		team_key = match['team1_key']
		if team_key not in groups[group]:
			groups[group].append(team_key)

		team_key = match['team2_key']
		if team_key not in groups[group]:
			groups[group].append(team_key)


file_name = "groups.json"
with open(file_name, 'w') as outfile:
	json.dump({"groups": groups}, outfile, sort_keys=True, indent=4)