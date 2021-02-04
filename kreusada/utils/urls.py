GIST = "https://gist.github.com"
GIT = "https://github.com"
LMGTFY="https://lmgtfy.app"
GOOGLE="https://www.google.co.uk/search?source=hp&ei=z07WX6SiGrXVgwfdpa3wAQ&q="

def gist(text: str):
    """Gets a gist URL from a string."""
    return "[{}]({})".format(text, GIST)

def github(text: str, git_slug: str = ''):
    """Gets a github URL from a string."""
    return "[{}]({}/{})".format(text, GIT, git_slug)

def lmgtfy(text: str):
    """Gets a LMGTFY URL from a string."""
    return "{}/?q={}".format(LMGTFY, text)

def google(text: str):
    """Gets a google URL from a string."""
    return "{}{}".format(GOOGLE, text)
