# ----- intro -----

"""
This file is meant to add functions for requesting and getting user input, all formatted in an
easy to use manner. Additionally, it will allow for integrated input processing just to ensure that
malicious input cannot be used to break programs.
"""

# ----- import other modules -----

import time
import regex as re

# ----- import other dev tools -----

from dev import devCommands
from final import finalCommands
from user_input import errorCreator

# ----- code -----


class userResponse():

    def __init__(self, value, value_raw, query, dev_mode):
        self.value = value
        self.type = type(value)
        self.value_raw = value_raw
        self.query = query

        self.dev_mode = dev_mode

        self.devCommands = devCommands(dev_mode)
        self.finalCommands = finalCommands(dev_mode)


class queryManager():

    """
    This is meant to be a class for managing user queries, including
    fancy features like easy implementation of previous buttons.
    """

    def __init__(self, dev_mode):
        self.history_list = list()
        self.dev_mode = dev_mode

        self.devCommands = devCommands(dev_mode)
        self.finalCommands = finalCommands(dev_mode)
        self.errorCreator = errorCreator(dev_mode)

    def __indexer__(self, find=None, index=None) -> dict:
        """
        This is just a local method needed to assist with the indexing/querying of query entries in the history_list.
        I suppose you could use it to say, find out how many queries you've made, but I think that need will be reasonably rare.

        Parameters:
        -----------

        find (opt): int
            integer representing the index of the history_list that is being searched for; default None if not needed

        index (opt): dict
            history_list dictionary entry to create an index for; None if not needed

        Returns:
        --------

        response: dict
            dictionary representing either the dictionary needed or a new dictionary with the correct index, depending on whether find or index was given
        """

        # requested mode is 'find'
        if find != None:

            # check that both find and index haven't been given; throw error if so
            if index == None:
                self.errorCreator.printError("ParameterError", "queryManager:__indexer__()",
                                             "expected find or index, but got neither.", "something went wrong with response queries.", "", True)

            # check that find is an integer; throw error if not
            if type(find) != int:
                find_type = type(find)
                self.errorCreator.printError("TypeError", "queryManager:__indexer__()",
                                             "expected find to be of type int, instead received {find_type}.", "something went wrong with reqponse queries.", "", True)

            # return the dictionary of the requested history_list entry
            try:
                return self.history_list[find]
            except Exception as e:
                self.errorCreator.printError(
                    "Exception", "queryManager:__indexer__()", "unknown", e, True)

        # requested mode is 'index'
        else:

            # check that index is a dictionary; throw error if not
            if type(index) != dict:
                index_type = type(index)
                self.errorCreator.printError("TypeError", "queryManager:__indexer__()",
                                             "expected index to be of type dict, instead received {index_type}.", "something went wrong with reqponse queries.", "", True)

            # give the dictionary an index according to history_list
            try:
                int_index = self.history_list[-1]["index"] + 1
            except IndexError:
                int_index = -1
            index["index"] = int_index + 1

            return index

    def baseRequest(self, query) -> str:
        """
        Just some basic processing of user input to prevent erroring/malicious input.

        Parameters:
        -----------

        query: str
            string representing the question the user is choosing options to respond to

        Returns:
        --------

        user_response: str
            string of the user's input
        """

        user_response = input(query)

        # check if the input is empty
        if user_response == None or user_response == "":

            self.errorCreator.printWarning(
                "queryManager:baseRequest()", "got null user input, please write something and try again")

            # let the user try again
            user_response = self.baseRequest(query)
            return user_response

        # input is fine, pass it along
        return user_response

    def numberRequest(self, query, lower_bound=None, upper_bound=None, ensure_whole=False, record=False) -> userResponse:
        """
        Gets and validates numeric input.

        Parameters:
        -----------

        query: str
            string representing the question the user is choosing options to respond to

        lower_bound (opt): int
            integer representing the lowest value the user can input - None if not needed; defaults to None

        upper_bound (opt): int
            integer representing the highest value the user can input - None if not needed; defaults to None

        ensure_whole (opt): bool
            boolean representing whether user input must be a whole number or not; defaults to False

        record (opt): bool
            boolean representing whether a userResponse class instance should be generated and saved to the history_list.
            also controls whether the raw value is returned instead of an instance of userResponse; defaults to False

        Returns:
        --------

        response: userResponse
            instance of class userResponse according to the input given; will not generate if record is False

        value: int
            value the user inputs; only generates if record is False
        """

        try:
            user_response = float(self.baseRequest(query))
        except TypeError:
            self.errorCreator.printWarning(
                "queryManager:numberRequest()", "input requires a number, but did not receive one")

            # let the user try again
            user_response = self.numberRequest(
                query, lower_bound=lower_bound, upper_bound=upper_bound, ensure_whole=ensure_whole, record=False)

            # create a userRequest or simple return depending on what is requested
            if record:
                response = userResponse(
                    user_response, user_response, query, self.dev_mode)
                self.history_list[-1]["response"] = response
                return response
            else:
                return user_response

        # check to ensure that the given number is round
        if ensure_whole and user_response % 1 != 0:

            self.errorCreator.printWarning(
                "queryManager:numberRequest()", "input requires a whole number, but did not receive one")

            time.sleep(2)

            # let the user try again
            user_response = self.numberRequest(
                query, lower_bound=lower_bound, upper_bound=upper_bound, ensure_whole=ensure_whole, record=False)

            # create a userRequest or simple return depending on what is requested
            if record:
                response = userResponse(
                    user_response, user_response, query, self.dev_mode)
                self.history_list[-1]["response"] = response
                return response
            else:
                return user_response

        # check to ensure that the number given is greater than or equal to the lower bound
        str_user_response = str(user_response)
        if user_response <= lower_bound:

            str_lower_bound = str(lower_bound)
            self.errorCreator.printWarning(
                "queryManager:numberRequest()", "need a numeric input greater than or equal to {str_lower_bound}, but instead got {str_user_response}, which is too low")

            time.sleep(2)

            # let the user try again
            user_response = self.numberRequest(
                query, lower_bound=lower_bound, upper_bound=upper_bound, ensure_whole=ensure_whole, record=False)

            # create a userRequest or simple return depending on what is requested
            if record:
                response = userResponse(
                    user_response, user_response, query, self.dev_mode)
                self.history_list[-1]["response"] = response
                return response
            else:
                return user_response

        elif user_response >= upper_bound:

            str_upper_bound = str(upper_bound)
            self.errorCreator.printWarning(
                "queryManager:numberRequest", "need a numeric input less than or equal to {str_upper_bound}, but instead got {str_user_response}, which is too high")

            time.sleep(2)

            # create a userRequest or simple return depending on what is requested
            if record:
                response = userResponse(
                    user_response, user_response, query, self.dev_mode)
                self.history_list[-1]["response"] = response
                return response
            else:
                return user_response

        # input is fine, return the data as requested (userRequest or simple return)
        if record:
            response = userResponse(
                user_response, user_response, query, self.dev_mode)
            self.history_list[-1]["response"] = response
            return response
        else:
            return user_response

    def stringRequest(self, query, cannot_contain=[], censor=False, processing=[], record=False) -> userResponse:
        """
        Gets and processes user string input.

        Parameters:
        -----------

        query: str
            string representing the question the user is choosing options to respond to

        cannot_contain (opt): list
            regexes for things that aren't allowed to be in the given input
            (neat tip, use regex101.com to test various patterns); defaults to []

        censor (opt): bool
            boolean representing whether new input should be gathered when words on the cannot contain list, 
            or whether the strings should simply be censored; defaults to False

        processing (opt): list
            list containing any one of the following: "lower", "upper"; defaults to []

        record (opt): bool
            boolean representing whether a userResponse class instance should be generated and saved to the history_list.
            also controls whether the raw value is returned instead of an instance of userResponse; defaults to False

        Returns:
        --------

        response: userResponse
            instance of class userResponse according to the input given; will not generate if record is False

        value: str
            value the user inputs; only generates if record is False
        """

        user_response = self.baseRequest(query)

        # setup regex to check cannot_contain properly
        final_regex_string = ""
        for regex in cannot_contain:
            final_regex_string += regex + "|"
        final_regex = re.compile(final_regex_string)

        # check for matches and censor/ask for new input as requrested
        matches = re.finditer(final_regex)
        if len(matches) != 0:
            if censor:
                user_response = re.sub(final_regex, "", user_response)
            else:
                self.errorCreator.printWarning(
                    "queryManager:stringRequest()", "the string you inputted contains 'banned' content, please try again")
                user_response = self.stringRequest(
                    query, cannot_contain=cannot_contain, censor=censor, processing=processing, record=False)

        # process the input according to the given processing markers
        if len(processing) != 0:
            if "upper" in processing:
                user_response = user_response.upper()
            elif "lower" in processing:
                user_response = user_response.lower()

        # input is now processed, return the data as requested (userRequest or simple return)
        if record:
            response = userResponse(
                user_response, user_response, query, self.dev_mode)
            self.history_list[-1]["response"] = response
            return response
        else:
            return user_response

    def optionRequest(self, query, options_list, clear=True, add_previous=False) -> userResponse:
        """
        Gets the user's choice among a group of options.

        Parameters:
        -----------

        query: str
            string representing the question the user is choosing options to respond to

        options_list: list
            list of strings to print as options to the user

        clear (opt): bool
            whether the terminal window should be cleared or not, True by default

        add_previous (opt): bool
            True if the previous answer set should be included as an option for the query, False if not; False by default

        Returns:
        --------

        user_response: userResponse
            instance of class userResponse according to the data given by options_list/functions_list
        """

        # ----- pre-user-request -----

        # check that there has been at least 1 query made if add_previous is True; throw an error if not
        if len(self.history_list) < 1 and add_previous:
            self.errorCreator.printError("ParameterError", "queryManager:optionRequest()",
                                         "tried to add 'back button' functionality without a previous query", "something went wrong with getting your input.", "", True)

        # format options_list and functions_list according to the given parameters
        if add_previous:
            options_list.append("previous")

        # generate a listing for the query in history_list
        self.history_list.append(self.__indexer__(index={
            "options_list": options_list,
        }))

        # ----- handling the user request -----

        # if requested, clear the terminal window
        if clear:
            self.finalCommands.clear()

        # show the options list strings
        self.finalCommands.blankLine()
        print("Options: ")
        for i in range(0, len(options_list)):
            print(f"[{i}] - {options_list[i]}")
        self.finalCommands.blankLine()

        # get the user's response and create an instance of userResponse accordingly
        user_response = self.numberRequest(
            query, 0, len(options_list) + 1, True, False)

        # input is fine, create a userResponse instance accordingly
        response = userResponse(
            options_list[user_response], user_response, self.dev_mode)

        return self.history_list[-1]["response"]

    def blankRequest(self, query="") -> None:
        """
        A function for getting 'enter' button input from the user, regardless of what's been typed.

        Parameters:
        -----------

        query (opt): str
            string representing what the user is reacting to

        Returns:
        --------

        None
        """

        self.finalCommands.blankLine()
        answer = input(query")
        self.finalCommands.blankLine()

        return None
