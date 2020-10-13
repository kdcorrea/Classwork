#Kristy D. Correa
#CIS245: Introduction to Programming
#October 5, 2020
#Wk8 Assignment - Directories
#References:
	#Python Crash Course (2nd ed.) by Eric Matthes
	#Python - OS Module by TutuorialsTeachers.com (https://www.tutorialsteacher.com/python/os-module)
	#Wk8 PDF Presentation
	#Example code by DiscDiver (https://github.com/discdiver/os-examples/commit/56ff1a4a040ab607520d500081bb98a3763e9214)
	#Example code by magmichal (https://github.com/magmichal/Python-Renaming-Script/blob/master/script.py)
	#Hands on Python Tutorial by Dr. Andrew N Harringtion (http://anh.cs.luc.edu/handsonPythonTutorial/files.html)
	#https://www.guru99.com/python-check-if-file-exists.html

#Imports the OS library
import os

filePath = '/users/kristycorrea/Desktop/python_work/'
fileName = 'example_run.py'
completePath = filePath + fileName
if os.path.isfile(fileName):
	print('File Exists')
if os.path.isdir(filePath):
	print('Directory Exists')
if os.path.exists(completePath):
	print('Complete path exists')
print('Complete path', completePath)
with open(completePath, 'w') as fileHandle:
	fileHandle.write('I love programming and Python.')
with open(completePath, 'r') as fileHandle:
	data = fileHandle.read()
user_prompt = input('Enter your name, address, and phone number:')
print(user_prompt)
with open(completePath, 'a+') as fileHandle:
	data = fileHandle.read(user_prompt)