#----- intro -----

"""
This is really simple, I just want a simple variable I can change so that I can print things specifically for when I want to debug or see more
detailed output for development reasons.
"""

#----- code -----

def devPrint(content, dev_mode=True):
    if dev_mode:    
        print(content)