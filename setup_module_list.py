#----- intro -----

"""
This is just meant to be a tool that can easily make the module_list.json file needed for automatic module installation.
"""

#----- import stuff -----

import json #do I even need to write something describing what this does?

#----- code -----

#data to write to JSON
data_dict = {
    "setup_status": False,
    "module_list":[ #write modules' pip names here
        
    ]
}

#writing data to JSON
with open('module_list.json', 'w') as output_file:
    json.dump(data_dict, output_file)
