# -*- coding: utf-8 -*-
import json
from config import *

# --- Numero los partidos
for round_i in iter(range(1, numberOfRounds+1)):
	file_name = "round%d.json" % round_i
	json_f = json.load(open(file_name))

	for idx, match in enumerate(json_f["games"]):
		match["title"] = "R%d-%d" % (round_i, (idx+1))

	with open(file_name, 'w') as outfile:
		json.dump(json_f, outfile, sort_keys=True, indent=4)
