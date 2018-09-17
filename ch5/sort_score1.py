
#james=list()

try:
	with open("james.txt") as file:
		date=file.readline()
		james=date.strip().split(',')
	with open("julie.txt") as file:
		date=file.readline()
		julie=date.strip().split(',')
	with open("mikey.txt") as file:
		date=file.readline()
		mikey=date.strip().split(',')
	with open("sarah.txt") as file:
		date=file.readline()
		sarah=date.strip().split(',')
except Exception as e:
	print(e.str())
finally:
  file.close()

print(james)
print(julie)
print(mikey)
print(sarah)
