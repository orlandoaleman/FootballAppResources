# -*- coding: utf-8 -*-
import json
from config import *

for i in iter(range(1, numberOfRounds+1)):
	file_name = "round%d.json" % i
	json_f = json.load(open(file_name))
	json_f['games'] = sorted(json_f['games'],key=lambda x: x['play_at'])

	with open(file_name, 'w') as outfile:
  		json.dump(json_f, outfile, sort_keys=True, indent=4)
