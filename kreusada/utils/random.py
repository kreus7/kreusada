import yaml
import random
import pathlib

def boolean():
    """
    Returns a random boolean.
    """
    return random.getrandbits(1)

def percentage():
    """
    Returns a percentage from 1 to 100.
    """
    return f"{random.randint(1, 100)}%"

#def fruit(plural: bool):
#    with open(pathlib.Path(__file__).resolve(strict=True).parent / "datalists" / "consumables.yaml") as file:
#        fruit = yaml.full_load(file)
#        for k in fruit.keys():
#            if not plural:
#                return random.choice(k['singular'])
#            else:
#                return random.choice(k['plural'])