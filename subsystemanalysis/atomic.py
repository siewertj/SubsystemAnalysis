import json


class AtomicComponent:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


	@classmethod
	def from_dictionary(cls, dct):
		x = cls(dct.get('name', None))
		x.type = dct.get('type', None)
		x.weight = dct.get('weight', 0)
		x.cost = dct.get('cost', 0)
		return x

'''
	def to_json(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def json_loadhook(dct):
	if 'type' in dct:
		return AtomicComponent.from_dictionary(dct)
	return dct


with open('atomic.json', 'r') as fp:
	jsondata = json.load(fp, object_hook=json_loadhook)

for x in jsondata['atomic_components']:
	print(x)
	print(x.to_json())
'''