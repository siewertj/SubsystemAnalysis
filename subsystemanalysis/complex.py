import json


class ComplexComponent:
	def __init__(self, name):
		self.name = str(name)

	def __str__(self):
		return self.name


	@classmethod
	def from_dictionary(cls, dct):
		x = cls(dct.get('name', None))
		x.type = str(dct.get('type', None))
		x.components = dct.get('components', None)
		return x

	def to_json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def json_loadhook(dct):
	if 'type' in dct and dct['type'] == "complex":
		print('found complex component')
		return ComplexComponent.from_dictionary(dct)
	return dct


with open('components.json', 'r') as fp:
	jsondata = json.load(fp, object_hook=json_loadhook)

for x in jsondata['complex_components']:
	print(x)
	tmp = x.to_json()
	print(tmp)
	#print(x.to_json())