#----- intro -----

"""
<add introductory comments here> 
"""

#----- setup dev stuff -----

#module setup
from python_dev_tools import module_setup #import the setup routine to be run
module_list = ["python-dotenv"] #add in strings of require-install modules here
module_setup.main(module_list)

#classes for functions relating to printing things
from python_dev_tools.dev import devCommands
from python_dev_tools.final import finalCommands

dev_mode = True
dev_commands_object = devCommands(dev_mode)

final_commands_object = finalCommands(dev_mode)

#----- load environment variables -----

import settings
settings = settings.getSettings()

#----- import required modules -----

#----- code -----