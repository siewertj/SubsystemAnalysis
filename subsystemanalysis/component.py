
class Atomic:
	""" Represents a part that is not broken up into smaller components.
	Essentially an atomic component is a part that is bought. """

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	@classmethod
	def from_dictionary(cls, dct):
		""" Reads the required components from a dictionary (python map). This
		works seamlessly with pythons built in json parser. """
		x = cls(dct.get('name', None))
		x.type = dct.get('type', None)
		x.weight = dct.get('weight', 0)
		x.cost = dct.get('cost', 0)
		return x


class Complex:
	""" A component that is made up of one or more other components. This
	allows easy pricing, weight, etc information to be deemed from the item
	based on what it is made out of. """

	def __init__(self, name):
		self.name = str(name)

	def __str__(self):
		return self.name

	@classmethod
	def from_dictionary(cls, dct):
		""" Reads the required components from a dictionary (python map). This
		works seamlessly with pythons built in json parser. """
		x = cls(dct.get('name', None))
		x.type = str(dct.get('type', None))
		x.components = dct.get('components', None)
		return x


