# ----- intro -----

"""
<add introductory comments here> 
"""

# ----- import required libraries -----

# required for the base script
import time
import os

# other libraries

# ----- import tool libraries from pytools

# import the setup routine to be run
from pytools.module_setup import moduleSetup
import settings
from pytools.messager import messagerSetup, clear, horizontalRule

# ----- define developer mode setting -----

dev_mode = True

# ----- messager setup -----

messager = messagerSetup(dev_mode=True, run_erase=False)

# ----- module setup -----

# add in strings of require-install modules here
module_list = ["python-dotenv"]
module_setup(dev_mode, module_list)

# ----- load environment variables -----

settings = settings.getSettings()

# ----- completion message -----

clear()
time.sleep(1)
messager.info("setup complete.")
messager.info(f"----- new {os.path.basename(__file__)} run -----")

# ----- code -----


def main():  # main running function of the program
    pass

# ----- if this is meant to be a script, uncomment this section; otherwise, it is meant to be a library -----
#
# if __name__ == "__main__":
#     main()
#
# -----
