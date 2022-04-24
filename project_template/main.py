# ----- intro -----

"""
<add introductory comments here> 
"""

# ----- import required libraries -----

import time

# ----- messager setup -----

from pytools import module_setup  # import the setup routine to be run
import settings
from pytools.messager import messagerSetup, clear, horizontalRule
logger = messagerSetup()

# ----- module setup -----

# add in strings of require-install modules here
module_list = ["python-dotenv"]
module_setup.main(module_list)

# ----- load environment variables -----

settings = settings.getSettings()

# ----- completion message -----

time.sleep(1)
logger.info("setup complete.")

# ----- code -----


def main():  # main running function of the program
    pass

# ----- if this is meant to be a script, uncomment this section; otherwise, it is meant to be a library -----
#
# if __name__ == "__main__":
#     main()
#
# -----
