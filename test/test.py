import subsystemanalysis.atomic as atomic
import subsystemanalysis.complex as complex
import json

with open('atomic.json', 'r') as fp:
	jsondata = json.load(fp, object_hook=complex.json_loadhook)

for x in jsondata['complex_components']:
	print(x)
	print(x.to_json())