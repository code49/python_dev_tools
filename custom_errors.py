"""
This file is meant to define a class to help create standardised custom error messages.
"""

#----- import necessary modules -----

import os

#----- import other dev tools -----

from dev import devCommands
from final import finalCommands

#----- create the error creator -----
class errorCreator():

    def __init__(self, dev_mode):
        
        self.dev_mode = dev_mode

        self.devCommands = devCommands(dev_mode)
        self.finalCommands = finalCommands(dev_mode)

    def printError(self, type, source, description, final_append, error_message, exit=False)->None:
        """
        Prints a standardised error message according to given parameters. Exits the program if requested.
        
        Parameters:
        -----------

        type: str
            string denoting the 'type' of error encountered (e.g. "TypeError")

        source: str
            string denoting the 'source' of the error, or where the error was encountered (e.g. "fooFunction()")
        
        description: str
            string with a description of what the error entails (e.g. "expected parameter of type str, but instead received int")

        final_append: str
            string denoting what to do if encountering the error while dev_mode is disabled

        error_message: str
            string containing the python traceback of the error, if applicable (mostly for try + except statements)
        
        exit (opt): bool
            True if the program should exit upon handling this error, False if not

        Returns:
        --------
        
        None
        """

        #----- pre-generate the error lines to print -----
        line_to_print = f"{type} - {source}: {description}"
        error_message_1 = f"{source}: the error message is as follows: "
        error_message_2 = f"{error_message}"
        final_append = f"{source}: {final_append}"

        #----- figure out how long the bars around the content have to be ----
        if self.dev_mode:
            line_length_list = [len(line_to_print), len(error_message_1), len(error_message_2)]
        else:
            line_length_list = [len(line_to_print), len(final_append)]
        bar_length = min(max(line_length_list), os.get_terminal_size.lines)

        #----- generate the bars -----
        bar_string = ""
        for i in range(0, bar_length):
            bar_string += "-"

        #----- print out the error information -----
        self.finalCommands.blankLine()
        self.finalCommands.finalPrint(bar_string)

        #if dev_mode is enabled, print specific traceback information
        self.devCommands.devPrint(error_message_1)
        self.devCommands.devPrint(error_message_2)

        #if dev_mode is disabled, print "final user" information
        self.finalCommands.finalNoDevPrint(final_append)

        self.finalCommands.finalPrint(bar_string)

        #----- if requested, exit the program -----
        if exit:
            quit()

    def printWarning(self, source, description)->None:
        """
        Prints a warning message to the end user (for example, if they write invalid input). Meant to be a version of printError,
        but for less severe issues as opposed to program-breaking errors.

        Parameters:
        -----------

        source: str
            string denoting the 'source' of the error, or where the error was encountered (e.g. "fooFunction()")
        
        description: str
            string with a description of what the error entails (e.g. "expected parameter of type str, but instead received int")

        Returns:
        --------

        None
        """

        #----- pre-generate warning line -----

        warning_line = f"warning: {source}: {description}"

        #----- generate the bars -----
        bar_string = ""
        for i in range(0, bar_length):
            bar_string += "-"

        #----- figure out how long the bars around the content have to be ----
        bar_length = min(len(warning_line), os.get_terminal_size.lines)

        #----- print out the error information -----
        self.finalCommands.blankLine()
        self.finalCommands.finalPrint(bar_string)
        self.finalCommands.finalPrint(warning_line)
        self.finalCommands.finalPrint(bar_string)
        self.finalCommands.blankLine()