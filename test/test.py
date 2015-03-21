import subsystemanalysis.analyze as analyze


if __name__ == '__main__':
	analyzer = analyze.Analyzer()
	with open('components.json', 'r') as fp:
		analyzer.load(fp)

	print("Complex:")
	for x in analyzer.complex:
		print(x.json())
		#print(analyze.obj_to_json_simple_(x))

	print("Atomic:")
	for x in analyzer.atomic:
		print(x.json())
		#print(analyze.obj_to_json_simple_(x))
