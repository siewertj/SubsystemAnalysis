import json


class Atomic:
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


class Complex:
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


