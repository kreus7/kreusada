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