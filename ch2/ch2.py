
# PyPI:Python Package Index python包索引 


import nester

cast = ['plain', 'cleese', 'idle', 'jones']


# 主python程序中(以及idle shell中)的代码与一个名为__main__的命名空间管理.
# 将代码放在某个单独模块中时,python会自动创建一个与模块同名的命名空间.
nester.print_lol(cast)


# BIF函数属于__builtins__命名空间,但会自动导入__main__命名空间.


def print_list(lst, isindent):
	for each in lst:
		if isinstance(each, list):
			if isindent:
				print('    ')
			print_list(each)
		else:
			print(each)

