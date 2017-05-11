#!/usr/bin/python 

import subprocess

actual_file = subprocess.check_output(['ls']).split('\n')
actual_file.pop()
print (actual_file) 
  


		