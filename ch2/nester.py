def print_list(lst):
	for each in lst:
		if isinstance(each, list):
			print_list(each)
		else:
			print(each)

