# python-dev-tools

## purpose:

The purpose of this project is to create a simple, easy-to-use set of commonly-used tools for python program development. This includes many features, from differentiating different use-cases of print statements (i.e. ones needed for debugging vs. ones needed in the final program) to automatically installing PyPI modules straight from the internet.

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
    -----| /user_input.py ; this file contains the class for the various functions with getting and simple screening of user input
    -----| /custom_errors.py ; this file contains the class for the various funtions relating to printing standardised error and warning messages
    -----| /threading.py ; this file contains the class for easily creating and monitoring multi-thread programs

---

## project_template:

This is really meant to be a simple way of starting off using the development tools - it includes a basic structure of the files typically needed for a program such as settings and a main file. It also simply incorporates many of the features included in this toolkit, so you don't need to do any of the boring setup :)

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

To create a horizontal rule:

First, you'll need to create a list of strings - this can include just one string or multiple strings (if you're looking to 'rule' over multiple lines like you might for a list of things).

then, simply use:

    final.dashedFormattedLine(string_list_here)

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

### custom_errors

The purpose of this tool is pretty simple: to be able to create customisable errors easily. There are two main functions you need to know about: printError() and printWarning(). Note that since the errorCreator() is still a class, you should still make sure to create an instance of it somewhere in your code like so:

    errorCreator = custom_errors.errorCreator()

#### printError():

This function will print out ('raise') a more severe error, such as a function receiving the wrong kind of parameter. I'll copy the exact parameter requirements/explanations here for reference, though they should also be visible using tooltips in an editor like VS Code or Atom:

    Parameters:
    -----------

        type: str
            string denoting the 'type' of error encountered (e.g. "TypeError")

        source: str
            string denoting the 'source' of the error, or where the error was encountered (e.g. "fooFunction()")
        
        description: str
            string with a description of what the error entails (e.g. "expected parameter of type str, but instead received int")

        final_append: str
            string denoting what to do if encountering the error while dev_mode is disabled

        error_message: str
            string containing the python traceback of the error, if applicable (mostly for try + except statements)
        
        exit (opt): bool
            True if the program should exit upon handling this error, False if not

    Returns:
    --------
        
        None

#### printWarning():

This is meant to be a way to do something similar to printError(), but for cases where slightly less severity of issue is involved. Once again, the parameters/returns for reference:

    Parameters:
    -----------

        source: str
            string denoting the 'source' of the error, or where the error was encountered (e.g. "fooFunction()")
        
        description: str
            string with a description of what the error entails (e.g. "expected parameter of type str, but instead received int")

    Returns:
    --------

        None

### user_input

The purpose of this file is to streamline the process of gathering user input, as well as adding some nice-to-have features. Like the others, make sure to create an instance of queryManager() first!

The tool employs a class called 'userResponse' that contains some data about each response received from the user, as well as what query the user was given that warranted that response.

The tool has a few functions that are useful to know about:

To request some sort of numeric input:

    queryManager.numberRequest(query, lower_bound (opt), upper_bound (opt), ensure_whole (opt), record(opt))

To request some sort of string input:

    queryManager.stringRequest(query, cannot_contain (opt), censor (opt), processing (opt), record (opt))

To request the user pick from a list of options:

    queryManager.optionRequest(query, options_list, clear (opt), add_previous (opt))

It even has a feature to have the user go back to the last option query automatically, just by setting add_previous to True!

To simply request some input with minimal processing on it:

    queryManager.blankRequest(query)

### threading

This file is meant to simply add support for multithreading in your projects. Make sure to create an instance of threader() before using it. 

Each new parallel process can be added like this:

    threader.createThread(function_to_run, *args, **kwargs)

You can check which functions are currently running like this:

    threader.getThreads()

You can even set the whole program to end upon your threads finishing like so:

    threader.exitOnThreadEnd()