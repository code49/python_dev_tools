#----- intro -----

"""
<add introductory comments here> 
"""

#----- setup dev stuff -----

from python_dev_tools import dev, final, module_setup #import the dev tool files, run setup routine
module_list = ["python-dotenv"] #add in strings of require-install modules here
module_setup.main()

dev_mode = True

#----- load environment variables -----

import settings
settings = settings.getSettings()

#----- import required modules -----

#----- code -----