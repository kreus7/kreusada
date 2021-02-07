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