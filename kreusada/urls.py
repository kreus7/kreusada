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