

def sanitizer(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []


#james=list()

try:
	with open("james.txt") as file:
		date=file.readline()
		james=date.strip().split(',')
		clean_james=[sanitizer(item) for item in james] #列表推导
		clean_james.sort()
	with open("julie.txt") as file:
		date=file.readline()
		julie=date.strip().split(',')
		clean_julie=[sanitizer(item) for item in julie]
		clean_julie.sort()
	with open("mikey.txt") as file:
		date=file.readline()
		mikey=date.strip().split(',')
		clean_mikey=[sanitizer(item) for item in mikey]
		clean_mikey.sort()
	with open("sarah.txt") as file:
		date=file.readline()
		sarah=date.strip().split(',')
		clean_sarah=[sanitizer(item) for item in sarah]
		clean_sarah.sort()
except Exception as e:
	print(e.str())
finally:
  file.close()

print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)
