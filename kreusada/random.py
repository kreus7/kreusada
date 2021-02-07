import random

def boolean():
    """
    Generates a random boolean.

    Returns
    -------
    bool
        The random boolean.
    """
    return random.choice([True, False])

def percentage():
    """
    Generates a random percentage.

    Returns
    -------
    str
        The random percentage.
    """
    return f"{random.randint(1, 100)}%"