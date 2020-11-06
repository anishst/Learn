import fileinput                                   #  1
for line in fileinput.input(inplace=True):         #  2
	line = line.rstrip()                              #  3
	num = fileinput.lineno()                          #  4
	print('{:<50} # {:2d}'.format(line,num))          #  5
                                                   #  6
# run this like 'python numberlines.py numberlines.py' #  7
