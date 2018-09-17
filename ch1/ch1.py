
# suite python代码块

cast = ['the holy grail', 'the life of brain', 'the moving of life']
year = [1975, 1979, 1983]

list1 = [0, 2, 4]
list2 = [0, 1, 2]

for i,j in zip(list1, list2):
	cast.insert(i, year[j])
print(cast) # [1975, 'the holy grail', 1979, 'the life of brain', 1983, 'the moving of life']




movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# python3默认递归深度不能超过100,可改变这个上限
#import sys;
#sys.setrecursionlimit(num);

def print_list(lst):
	for each in lst:
		if isinstance(each, list):
			print_list(each)
		else:
			print(each)


print_list(movies)

#The Holy Grail
#1975
#Terry Jones & Terry Gilliam
#91
#Graham Chapman
#Michael Palin
#John Cleese
#Terry Gilliam
#Eric Idle
#Terry Jones
