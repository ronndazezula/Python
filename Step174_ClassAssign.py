class Email:
	dateRecd = 19991231
	recipName = 'John Doe'
	recipEmailAdd = 'jd@yahoo.com'
	sendName = 'Sally Field'
	sendEmailAdd = 'sfield@aol.com'
	subj = 'Check Out These Cute Cats!'

class Attach(Email):
	doctype = 'PowerPoint PPT Presentation'
	fileName = 'CuteCats.ppt'
	filePath = 'C:\JD\Documents\CuteCats.ppt'

class Embed(Email):
	doctype = 'Graphics Interchange Format'
	fileName = 'Kitties.gif'
	filePath = 'C:\JD\Pictures\Kitties.gif'

print('Date Cat Content Received:')
print(Email.dateRecd)
print('\nCat Attachment:')
print(Attach.fileName)
print('\nCat Embedded Image:')
print(Embed.fileName)
