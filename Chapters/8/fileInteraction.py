def newPatron(firstName, lastName, books):
	"""Adds new patron to patronFile.txt"""  
	books = [book.replace('/',' ') for book in books]
	bookString = '/'.join(books)
	patronFile = open('patronFile.txt', 'a')
	patronFile.write(('|'.join([firstName,lastName,bookString]) + '\n'))
	patronFile.close()

def checkForPatron(firstName='', lastName=''):
	"""Checks file for existing patron."""
	patronFile = open('patronFile.txt', 'r')
	for line in patronFile:
		line = line.rstrip('\n').split(',')
		if line[2] == lastName and line[1] == firstName:
			patronFile.close()
			return line
	return False
