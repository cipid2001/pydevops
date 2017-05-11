#!/usr/bin/python

l=[[1,2],[3,4,5,6],[7,8,9,10,11]]

def loop_function(count=None):
	if count == None:
		print ("3")
	else: 
		for i in range(count):
			print(i)
	  
def error_handling():
	try:
		f=open('hello')
	except	IOError:
		print "Ops! no file"

error_handling()

#if no error handling the execution of program is stopped.
#if error handling the program continues
loop_function()