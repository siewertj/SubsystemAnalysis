from . import component

import json


def json_loadhook(dct):
	""" Logic that determines which class the json object is parsed as. """
	if 'type' in dct:
		if dct['type'] == "atomic":
			return component.Atomic.from_dictionary(dct)

		elif dct['type'] == "complex":
			return component.Complex.from_dictionary(dct)
		
	return dct


def json_loadfile(fp):
	""" Loads the json file described by 'fp'. """
	jsondata = json.load(fp, object_hook=json_loadhook)
	return jsondata


class Analyzer:
	""" Does analysis on the components. This is what takes the complex components
	and determines useful information about them (weight, cost, etc). """

	def __init__(self):
		pass

	def load(self, fp):
		""" Loads and parses the json file. """
		data = json_loadfile(fp)
		self.atomic = data['atomic_components']
		self.complex = data['complex_components']
