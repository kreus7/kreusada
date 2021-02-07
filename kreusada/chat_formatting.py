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