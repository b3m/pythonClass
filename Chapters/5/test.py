

table = [['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'], 
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|X|', '|X|', '|_|', '|X|']]

# Finds value and returns list index of value.
x = 0
for i in xrange((len(table) -1),-1,-1):
	b = [item for item in range(len(table[i])) if table[i][item] == '|X|']
	print b
