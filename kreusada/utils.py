import os
import sys
import yaml
import random
import psutil
import discord
import pathlib
import inspect
import platform

class internals:
    """
    Get information about your client's internals.
    """
    
    def platform():
        """
        Retrieves your client's platform.
        """
        return platform.platform()
    
    def ram():
        """
        Gets your client's ram usage.
        """
        return psutil.virtual_memory()[2]
    
    def os():
        """
        Get your operating system's name.
        """
        return os.name
    
    def get_module(func):
        """
        Attempts to get the module from the function.
        """
        try:
            return inspect.getmodule(func)
        except:
            return False
    
class numerics:
    """
    Functions with math.
    """

    def isodd(number: int):
        """
        Returns True if the `number` is odd.

        Parameters
        ----------
        number: int
            The number to return the boolean on.

        Returns
        -------
        bool
            True if odd, else False.
        """
        return False if number % 2 == 0 else True

    def iseven(number: int):
        """
        Returns True if the `number` is even.

        Parameters
        ----------
        number: int
            The number to return the boolean on.

        Returns
        -------
        bool
            True if even, else False.
        """
        return True if number % 2 == 0 else False

class embed:
    """
    Functions for discord embeds.
    """

    def randcolor():
        """
        Generates a random embed colour.

        Returns
        -------
        int
            The randomly generated hex code.

        Aliases
        -------
        randcolour()
        """
        return "%06x" % random.randint(0, 0xFFFFFF)

    def randcolour():
        """
        Generates a random embed colour.

        Returns
        -------
        int
            The randomly generated hex code.

        Aliases
        -------
        randcolor()
        """
        return "%06x" % random.randint(0, 0xFFFFFF)

class random:
    """
    Functions for returning with the random module.
    """

    def boolean():
        """
        Generates a random boolean.

        Returns
        -------
        bool
            The random boolean.
        """
        return random.getrandbits(1)

    def percentage():
        """
        Generates a random percentage.

        Returns
        -------
        str
            The random percentage.
        """
        return f"{random.randint(1, 100)}%"

class box:
    """
    Get text wrapped in code-blocks.
    """

    def full(text: str, lang: str):
        """
        Returns a string in a full code-block.
        
        Parameters
        ----------
        text: str
            The text to add the codeblock to.
        lang: str
            The programming language for this code-block.
            
        Returns
        -------
        str
            The code-block.
        """
        return "```{}\n{}\n```".format(lang, text)

    def small(text: str):
        """
        Returns a string in a small code-block.
        
        Parameters
        ----------
        text: str
            The text to add the codeblock to.
            
        Returns
        -------
        str
            The code-block.
        """
        return "`{}`".format(text)

class chat_formatting:
    """
    Formatting utility for Discord.
    """

    def bold(text: str):
        """
        Returns a string with boldened characters.
        
        Parameters
        ----------
        text: str
            The text to bolden.
            
        Returns
        -------
        str
            The boldened string.
        """
        return "**{}**".format(text)


    def italic(text: str):
        """
        Returns a string with italicized characters.
        
        Parameters
        ----------
        text: str
            The text to italicize.
            
        Returns
        -------
        str
            The italicized string.
        """
        return "*{}*".format(text)


    def strike(text: str):
        """
        Returns a string with striked characters.
        
        Parameters
        ----------
        text: str
            The text to strike.
            
        Returns
        -------
        str
            The striked string.
        """
        return "~~{}~~".format(text)


    def spoiler(text: str):
        """
        Returns a string in a spoiler.
        
        Parameters
        ----------
        text: str
            The text to add the spoiler to.
            
        Returns
        -------
        str
            The spoiler string.
        """
        return "||{}||".format(text)


    def quote(text: str):
        """
        Returns a string as a quote.
        
        Parameters
        ----------
        text: str
            The text to quote.
            
        Returns
        -------
        str
            The quoted string.
        """
        return ">>> {}".format(text)

    def snake(text: str):
        """
        Returns a string with underscore spaces.
        
        Parameters
        ----------
        text: str
            The text to modify.
            
        Returns
        -------
        str
            The new string.
        """
        return text.replace(' ', '_')


    def reverse(text: str):
        """
        Returns a string reversed.
        
        Parameters
        ----------
        text: str
            The text to reverse.
            
        Returns
        -------
        str
            The reversed string.
        """
        return text[::-1]

class urls:
    """
    Functions used to embed strings into urls with markdown.
    """
    GIST = "https://gist.github.com"
    GIT = "https://github.com"
    LMGTFY="https://lmgtfy.app"
    GOOGLE="https://www.google.co.uk/search?source=hp&ei=z07WX6SiGrXVgwfdpa3wAQ&q="

    def gist(text: str):
        """
        Creates an embedded gist url on a string.
        
        Parameters
        ----------
        text: str
            The text to add the link to.
            
        Returns
        -------
        str
            The hyperlinked string.
        """
        return "[{}]({})".format(text, GIST)

    def github(text: str, git_slug: str = ''):
        """
        Creates an embedded github url on a string.
        
        Parameters
        ----------
        text: str
            The text to add the link to.
        git_slig: str
            The git slug for the link. Defaults to none.
            
        Returns
        -------
        str
            The hyperlinked string.
        """
        return "[{}]({}/{})".format(text, GIT, git_slug)

    def lmgtfy(text: str):
        """
        Creates an embedded LMGTFY url on a string.
        
        Parameters
        ----------
        text: str
            The text to add the link to.
            
        Returns
        -------
        str
            The hyperlinked string.
        """
        return "{}/?q={}".format(LMGTFY, text)

    def google(text: str):
        """
        Creates an embedded google url on a string.
        
        Parameters
        ----------
        text: str
            The text to add the link to.
            
        Returns
        -------
        str
            The hyperlinked string.
        """
        return "{}{}".format(GOOGLE, text)
