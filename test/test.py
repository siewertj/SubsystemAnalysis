import subsystemanalysis.analyze as analyze
import json

with open('components.json', 'r') as fp:
	jsondata = json.load(fp, object_hook=analyze.json_loadhook)

for x in jsondata['complex_components']:
	print(x)
	#print(x.to_json())