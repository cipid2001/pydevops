#!/usr/bin/python

def test_func(i=None):
	if i==None: 
		i=1
	print("Double",i*2)
	return i*2

#val=test_func([1,2])
val=test_func()
print (val)
