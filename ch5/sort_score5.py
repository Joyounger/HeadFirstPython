

def get_coach_data(filename):
	lst=list()
	try:
		with open(filename, 'r') as file:
			data = file.readline()
		lst = data.strip().split('.')
		return lst
	except IOException as error:
		printf("file error: " + str(error))
		return(None)
	finally:
		pass
