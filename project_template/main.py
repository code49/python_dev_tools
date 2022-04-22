# ----- intro -----

"""
<add introductory comments here> 
"""

# ----- setup dev stuff -----

# module setup
import settings
from python_dev_tools.final import finalCommands
from python_dev_tools.dev import devCommands
from python_dev_tools import module_setup  # import the setup routine to be run
# add in strings of require-install modules here
module_list = ["python-dotenv"]
module_setup.main(module_list)

# classes for functions relating to printing things

dev_mode = True
dev_commands_object = devCommands(dev_mode)

final_commands_object = finalCommands(dev_mode)

# ----- load environment variables -----

settings = settings.getSettings()

# ----- import required modules -----

# ----- code -----


def main():  # main running function of the program
    pass

# ----- if this is meant to be a script, uncomment this section; otherwise, it is meant to be a library -----
#
# if __name__ == __main__():
#     main()
#
# -----
