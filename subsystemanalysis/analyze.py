from . import atomic
from . import complex

import json


def obj_to_json_simple_(cls):
	return json.dumps(cls, default=lambda o: o.__dict__, sort_keys=True, indent=2)


def json_loadhook(dct):
	if 'type' in dct:
		if dct['type'] == "atomic":
			print('found atomic component')
			return atomic.AtomicComponent.from_dictionary(dct)

		elif dct['type'] == "complex":
			print('found complex component')
			return complex.ComplexComponent.from_dictionary(dct)
		
	return dct