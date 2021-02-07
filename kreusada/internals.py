import os
import psutil
import inspect
import platform

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