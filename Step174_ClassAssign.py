"""This is a very loose representation of an email and two associated files to
represent two classes that inherit from another class for Assignment Step 174.
The attributes are a loose representation of file metadata, not intended to link."""

class Email:
	dateRecd = 19991231
	recipName = 'John Doe'
	recipEmailAdd = 'jd@yahoo.com'
	sendName = 'Sally Field'
	sendEmailAdd = 'sfield@aol.com'
	subj = 'Check Out These Cute Cats!'

class Attach(Email):
	doctype = 'PowerPoint PPT Presentation'
	fileName = 'Step174_ClassAssign-img1.jpg'
	filePath = "C:\\Users\\ronnd\\Pictures\\img\\Step174_ClassAssign-img1.jpg"
	MD5Hash = '1f9b28cb3b83ade5228589642efb12dd'

class Embed(Email):
	doctype = 'Graphics Interchange Format'
	fileName = 'Step174_ClassAssign-img2.gif'
	filePath = "C:\\Users\\ronnd\\Pictures\\img\\Step174_ClassAssign-img2.gif"
	MD5Hash = 'fed3ec9946f427464b1a9f53e59af1b3'

print('Date Cat Content Received:')
print(Email.dateRecd)

print('\nCat Attachment Native Path:')
print(Attach.filePath)

print('\nCat Embedded Image Native Path:')
print(Embed.filePath)

from pathlib import Path
import webbrowser
import os

filename = Path(".\img\Step174_ClassAssign-img1.jpg")

iexplore = os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                        "Internet Explorer\\IEXPLORE.EXE")

browser = webbrowser.get(iexplore)

browser.open(filename.absolute().as_uri())

filename = Path(".\img\Step174_ClassAssign-img2.gif")

iexplore = os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                        "Internet Explorer\\IEXPLORE.EXE")

browser = webbrowser.get(iexplore)

browser.open(filename.absolute().as_uri())
