#----- intro -----

"""
This is just meant to be a file that ensures the project is properly set up each time the program is run - this is just done by ensuring pip is setup,
and then installing modules as necessary.

Credit to @ArtOfWarfare on stackOverflow for this solution:
    I've just very lightly modified the functions he's shared here: https://stackoverflow.com/posts/25643988/revisions
"""

#----- check the module_setup.json file to see whether modules even need to be  -----

import json #this is to read the .json file

def setup_modules(module_list):
    with open('./python_dev_tools/setup_status.json') as file:
        data = json.load(file)

    if not data["module_setup_status"]:

        print("Module Installation: This project has not been set up yet. Installing modules now.")

        #----- import baseline library stuff -----

        from subprocess import call #for using python/pip to install pip and other needed modules
        from os import remove, name #for removing the get-pip.py file after having installed pip, name is for ensuring correct pipPath for different OS
        # from urllib import urlretrieve #for getting get-pip.py file from the internet
        from urllib.request import urlretrieve
        from os.path import isfile, join #for dealing with pip's filepath
        from sys import prefix #this gets the filepath prefix for the system, for example C: on windows
        from subprocess import Popen, PIPE #used to get the pip.exe filepath on unix-based systems
        from pkgutil import iter_modules #this is used to check to see if the package is already installed

        #----- ensure correct pip setup -----

        #function that installs pip and cleans up the get-pip.py file afterward
        def installPip(): 

            urlretrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py") #get get-pip.py file from online
            call(["python", "get-pip.py"]) #run the .py file to install pip
            remove("get-pip.py") #remove the file to clean up the mess

        #function that returns the pip executable and installs pip if it cannot find it
        def getPip(): 

            #find the pip.exe filepath, depending on OS type
            if name == "nt": #windows
                pipPath = join(prefix, 'Scripts', 'pip.exe') 
            else: #unix
                finder = Popen(['which', 'pip'], stdout=PIPE, stderr=PIPE)
                pipPath = finder.communicate()[0].strip()

            #check if pip is installed, install it if not
            if not isfile(pipPath):
                installPip()
                if not isfile(pipPath):
                    raise NameError("MODULE INSTALL ERROR: failed to find/install pip, try manually installing pip and trying again, or if that doesn't work manually set pipPath to the pip.exe filepath")

            return pipPath

        #----- function that installs a given necessary module -----

        def installIfNeeded(module_pip_name):
        
            try: #ideally, pip should be able to find the module needed based on the given name, but in some cases the name might be wrong, and that should raise an error
                if module_pip_name not in [tuple_[1] for tuple_ in iter_modules()]:
                    print(f"{module_pip_name} has not been installed. Installing the module now.")
                    call([getPip(), "install", module_pip_name])

                    print(f"{module_pip_name} has been installed.")

            except: #this will raise an error if pip can't install the module for some reason
                raise KeyError(f"MODULE INSTALL ERROR: failed to install module {module_pip_name}. check that the module name is correct and then try again.")
        
        
        #----- running the two functions -----

        getPip()
        for module in module_list:
            installIfNeeded(module)

        #----- update module_list.json -----

        with open('./python_dev_tools/module_list.json', 'r') as file:
            data = json.load(file)
        new_data = {
            "setup_status": True
        }
        with open('./python_dev_tools/module_list.json', 'w') as file:
            data = json.dump(new_data, file)

        print("Module Installation: The project is now set up, you should not need to do this again.")
        