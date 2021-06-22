#----- intro -----

"""
This is just to add certain print functions I want to use in programs - final print (just to show it's meant to be in the final version of the program), 
clear (clear terminal window), inline().
"""

#----- import stuff -----

import os
import sys

#----- code -----

def finalPrint(content):
    print(content)

def clear():
    #for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    #for mac and linux (os.name is 'posix') 
    else: 
        _ = os.system('clear') 

def inline(content):
    sys.stdout.write("\033[2K\033[1G")
    print(content)