from yaml import full_load as load
from random import choice as pick
import pathlib

def fruit(plural: bool):
    with open("utils\data\consumables.yaml") as file:
        fruit = load(file)

        for item, doc in fruit.items():
            return pick(doc['food']['fruits']['singular']) if not plural else pick(doc['food']['fruits']['plural'])