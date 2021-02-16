import random

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
