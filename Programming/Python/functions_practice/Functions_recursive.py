movies = ['matrix', '1979', ['brooks', 'anish']]


for each_item in movies:
	if isinstance(nested_item, list):
		for nested_item in each_item:

			for deeper_item in nested_item:
				print(deeper_item)
		else:
			print(nested_item)
