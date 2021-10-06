#----- intro -----

"""
This is just to add certain print functions I want to use in programs - final print (just to show it's meant to be in the final version of the program), 
clear (clear terminal window), inline().
"""

#----- import stuff -----

import os
import sys
from custom_errors import errorCreator

#----- code -----

class finalCommands():

    def __init__(self, dev_mode):
        
        #only thing that needs to be set up is an internal ticker for whether dev mode is enabled or not - this allows for certain functions that only occur in the final version and not while in dev mode
        self.dev_mode = dev_mode
        self.errorCreator = errorCreator()

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

    #printing a line that's either the length of the terminal or the length of the longest string in a set of strings
    def dashedFormattedLine(self, string_list):
        #sanity check to ensure that we have received a list of length >= 1
        if type(string_list) != "list" or not len(string_list) >= 1:
            self.errorCreator.printError("TypeError", "finalCommands:dashedFormmatedLine()", "expected a list of at least length 1, either didn't get a list or got an empty one", "something has gone wrong, please inform the creator of the program", "", exit=True)
        
        #determine if the maximum length of a string in string_list is less than the width of the terminal and print the dashed line accordingly
        max_string_length = max(string_list)
        terminal_width = os.get_terminal_size["columns"]
        line_width = max(max_string_length, terminal_width)
        temp_line = ""
        for i in range(0, line_width):
            temp_line.append("-")
        print(temp_line)

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