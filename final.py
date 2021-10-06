#----- intro -----

"""
This is just to add certain print functions I want to use in programs - final print (just to show it's meant to be in the final version of the program), 
clear (clear terminal window), inline().
"""

#----- import stuff -----

import os
import sys

#----- code -----

class finalCommands():

    def __init__(self, dev_mode):
        
        #only thing that needs to be set up is an internal ticker for whether dev mode is enabled or not - this allows for certain functions that only occur in the final version and not while in dev mode
        self.dev_mode = dev_mode

    #basic printing; mostly for clarity reasons
    def finalPrint(self, content):
        print(content)

    #printing, but ensuring that dev mode is disabled in order to do so - maybe this'll be used, maybe it won't
    def finalNoDevPrint(self, content):
        if not self.dev_mode:
            print(content)

    #clearing the terminal window
    def clear(self):
        #for windows 
        if os.name == 'nt': 
            _ = os.system('cls') 
  
        #for mac and linux (os.name is 'posix') 
        else: 
            _ = os.system('clear') 

    #printing blank lines
    def blankLine(self):
        print()

    #clearing the terminal window, but ensuring that dev mode is disabled in order to do so - see finalNoDevPrint()
    def noDevClear(self):
        if not self.dev_mode:
            #for windows 
        if os.name == 'nt': 
            _ = os.system('cls') 
  
        #for mac and linux (os.name is 'posix') 
        else: 
            _ = os.system('clear') 

    #inline printing on the terminal window
    def inline(self, content):
        sys.stdout.write("\033[2K\033[1G")
        print(content)