# python-dev-tools

## purpose:

---

## directory directory:

This is meant to be a simple guide to the directory.

    -----| /project_template/ ; this is a subdirectory dedicated to a "template" for quickly setting up new python projects
    ----------| .env ; this file contains user-specific environment variables like api keys, secrets, etc.
    ----------| main.py ; this file is the  "main" jumping off file for new programs
    ----------| settings.py ; this file helps with importing environment variables into the main file
    -----| /__init__.py ; empty .py file needed to import classes into an outer directory
    -----| /dev.py ; this file contains the class for the various dev functions
    -----| /final.py ; this file contains the class for the various final functions
    -----| /setup_status.json ; this file contains data about whether the project has been set up (meaning checked that all packages have been installed) or not

---

## project_template:



---

## usage:

This section is meant to be a general guide on how to use the various tools of the python-dev-tools toolkit.

In general, tools can be used by instantiating an instance of the tool class and then calling tool methods accordingly.

### dev:

This is really meant as a way to clearly differentiate print statements made for development reasons and those for the final program. This helps reduce clutter and simplify debugging process, especially when new features are being added to a program.

To setup the dev tools:

    from python_dev_tools.dev import devCommands
    
    dev_mode = True #for whether dev_mode should be enabled or not
    dev = devCommands(dev_mode)

To print something only when dev_mode is True (I call this devPrint()):

    dev.devPrint(content)

### final:

Similar to the dev class, this is meant to be a way to more simply make final print statements.

To setup the final tools:

    from python_dev_tools.final import finalCommands

    dev_mode = True #for whether dev_mode should be enabled or not
    final = finalCommands(dev_mode)

#### standard:

These functions are very simple - just do the actions, as requested, no questions asked.

To print something:

    final.finalPrint(content)

To clear the terminal window:

    final.clear()

To write a line inline (i.e. replacing the last line):

    final.inline(content)

#### no-dev:

Only do these functions when not debugging; this is really nice for needing to have different formatting between dev and non-dev modes (e.g. showing extra data readouts per API call so that you know what information is being retrieved).

To print something:

    final.finalNoDevPrint(content)

To clear something:

    final.noDevClear()

Note that there is no no-dev inline() function since inline() is already quite finnicky (not to mention not super useful since clear() exists, albeit runs slightly slower) to begin with and adding the idea that whether things will print depending on dev_mode state will further add confusion and unusability.

### module_setup:

This is perhaps the most useful feature of the entire toolkit. Essentially, it's a nice way to ensure that all external modules (installed from PyPI) are installed wihtout making users run lines from the command line; theoretically this could be solved using fancy AHK scripts, but I think this method is significantly cleaner and "more automatic". 

Using the feature is quite simple. First, you need to create a list of the PyPI modules you want to require. Ensure that the names are as listed in PyPI, not just the ones you use to import them - for example Python Image Library (PIL) is listed in PyPI as "Pillow" instead of "PIL". Because the tool will simply try to install the package using pip (meaning that it won't know that say, PIL is actually named Pillow when installing), this is very important.

Additionally, "python-dotenv" and "regex" must always be required + installed in order for settings<area>.py and user_input<area>.py to work properly.

An example of doing this:

    from python_dev_tools import moduleSetup

    dev_mode = True #for whether dev_mode should be enabled or not
    module_list = [
        "python-dotenv", #remember that this is required for settings.py to work
        "regex", #this is needed for user_input.py to work (theoretically re would work, but unicode support is nice)
        "url-lib3",
        "markupsafe",
        "other PyPI modules"
    ]

From there, simply instantiate an instance of the moduleSetup class with dev_mode and module_list as parameters:

     moduleSetup = moduleSetup(dev_mode)

and you're done. Simple, right? 