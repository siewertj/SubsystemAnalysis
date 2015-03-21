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
