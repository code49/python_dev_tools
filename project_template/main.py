#----- intro -----

"""
<add introductory comments here> 
"""

#----- setup dev stuff -----

from python_dev_tools import dev, final, module_setup #import the dev tool files, run setup routine
module_setup.main()

#----- load environment variables -----

import settings
settings = settings.getSettings()

#----- import required modules -----

#----- code -----