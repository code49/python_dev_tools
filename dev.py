# ----- intro -----

"""
This is really simple, I just want a simple variable I can change so that I can print things specifically for when I want to debug or see more
detailed output for development reasons.
"""

# ----- code -----


class devCommands():

    def __init__(self, dev_mode):
        self.dev_mode = dev_mode

    def devPrint(self, content):
        if self.dev_mode:
            print(content)
