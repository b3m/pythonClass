
""" Begin Patron Interaction """

def newPatron(firstName, lastName, numberOfBooks):
	"""Need to strip spaces."""
	"""Adds new patron to patronFile.txt"""  
	# books = [book.replace('/',' ') for book in books]
	# bookString = '/'.join(books)
	patronFile = open('patronFile.txt', 'a')
	patronFile.write((','.join([firstName,lastName,numberOfBooks]) + '\n'))
	patronFile.close()

def removePatron(patronInfo):
	patronFile = open('patronFile.txt', 'r')
	lines = patronFile.readlines()
	patronFile.close()
	patronFile = open('patronFile.txt', 'w')
	for line in lines:
		line = line.split(',')
		if line[0] != patronInfo[0] or line[1] != patronInfo[1]:
			line = ','.join(line)
			patronFile.write(line)
	patronFile.close()

def checkForPatron(firstName='', lastName=''):
	"""Checks file for existing patron."""
	patronFile = open('patronFile.txt', 'r')
	for line in patronFile:
		line = line.rstrip('\n').split(',')
		if line[1] == lastName and line[0] == firstName:
			patronFile.close()
			return line
	patronFile.close()
	return False

def updatePatron(patronInfo):
	patronFile = open('patronFile.txt','r')
	lines = patronFile.readlines()
	patronFile.close()
	patronFile = open('patronFile.txt','w')
	for line in lines:
		line = line.split(',')
		if line[0] != patronInfo[0] or line[1] != patronInfo[1]:
			line = ','.join(line)
			patronFile.write(line)
	patronFile.write(','.join(patronInfo) + '\n')
	patronFile.close()

""" End Patron Interaction """



""" Begin Book Interaction """

def checkForBook(title, author):
	bookFile = open('bookFile.txt', 'r')
	for line in bookFile:
		line = line.rstrip('\n').split('|')
		if line[0] == title.lower() and line[1] == author.lower():
			bookFile.close()
			return line
	bookFile.close()
	return False

def addBook(bookObject):
	bookFile = open('bookFile.txt', 'a')
	bookFile.write('|'.join(bookObject) + '\n')
	bookFile.close()

def removeBook(bookObject):
	bookFile = open('bookFile.txt', 'r')
	lines = bookFile.readlines()
	bookFile.close()
	bookFile = open('bookFile.txt', 'w')
	for line in lines:
		line = line.split('|')
		if line[0] != bookObject[0] or line[1] != bookObject[1]:
			line = '|'.join(line)
			bookFile.write(line)
	bookFile.close()

def updateBook(bookObject):
	bookFile = open('bookFile.txt', 'r')
	lines = bookFile.readlines()
	bookFile.close()
	bookFile = open('bookFile.txt', 'w')
	for line in lines:
		line = line.split('|')
		if line[0] != bookObject[0] or line[1] != bookObject[1]:
			line = '|'.join(line)	
			bookFile.write(line)
	bookFile.write('|'.join(bookObject) + '\n')
	bookFile.close()



""" End Book Interaction """