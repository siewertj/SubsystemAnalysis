from . import component

import json


def obj_to_json_simple_(cls):
	""" converts a class object to a json object. This is pretty generic in that
	it just makes a json object based on the class member vars. """
	return json.dumps(cls, default=lambda o: o.__dict__, sort_keys=True, indent=2)


def json_loadhook(dct):
	""" Logic that determines which class the json object is parsed as. """
	if 'type' in dct:

		if dct['type'] == "atomic":
			print('found atomic component')
			return component.Atomic.from_dictionary(dct)

		elif dct['type'] == "complex":
			print('found complex component')
			return component.Complex.from_dictionary(dct)
		
	return dct


class Analyzer:
	""" Does analysis on the components. This is what takes the complex components
	and determines useful information about them (weight, cost, etc). """

	def __init__(self):
		pass