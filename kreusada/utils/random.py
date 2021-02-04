from yaml import full_load as load
from random import choice as pick
import pathlib

def fruit(plural: bool):
    with open(pathlib.Path(__file__).resolve(strict=True).parent / "datalists" / "consumables.yaml") as file:
        fruit = load(file)
        for k in fruit.keys():
            if not plural:
                return pick(k['singular'])
            else:
                return pick(k['plural'])