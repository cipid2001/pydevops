#!/usr/bin/python

l=[[1,2],[3,4,5,6],[7,8,9,10,11]]

def loop_function():
	count = 1
	for i in l:
	     print ("Sublist",i)
	     if i==[1,2]:
				print ("Testing pass")
				pass
				count = count + 1
				print("Hello pass",count)
	     elif i==[7,8,9,10,11]:
	            print ('Testing continue')
	            continue
	            count = count +1
	            print ("Continue",count)
	     elif i==[3,4,5,6]:
				print ("match If")
				print(i[0])
				print ("last count:",count)
				#break

loop_function()