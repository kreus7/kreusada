from yaml import full_load as load
from random import choice as pick
import pathlib

def fruit(plural: bool):
    with open(pathlib.Path(__file__).resolve(strict=True).parent / "datalists" / "consumables.yaml") as file:
        fruit = load(file)
        for item, doc in fruit.items():
            if not plural:
                return pick(item['fruits']['singular'])
            else:
                return pick(item['fruits']['plural'])