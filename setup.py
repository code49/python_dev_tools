#----- intro -----

"""
This is just meant to be a place to aggregate all of the various setup functions needed for a specific project
(so they can be imported all at once instead of individually), think things like ensuring all modules 
are installed properly.
"""

#----- import various setup files -----

from python_dev_tools import module_setup

#----- run various functions from setup files -----

module_setup.module_setup()