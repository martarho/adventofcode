from lib import *
import typing
import os
import re
from collections import defaultdict
import math


def sets2dict(l: list) -> tuple:
    d = defaultdict(list)
    gameID = int(l[0].split(" ")[1])
    for m in l[1:]:
        tup = m.split(" ")
        d[tup[1]].append(int(tup[0]))
    return (gameID, d)


def problem(f: typing.Union[str, os.PathLike]) -> None:
    # -- Set up problem
    pattern = r"(Game \d+|\d+ \w+)"
    bag_content = {"red": 12, "green": 13, "blue": 14}
    data = read_files(f)
    game_ids = []
    powers = []
    # --- Iterate games
    for game in data:
        gameID, sets = sets2dict(re.findall(pattern, game))
        is_valid = True
        max_values = {}
        for c in sets.keys():
            if len([*filter(lambda x: bag_content[c] < x, sets[c])]) > 0:
                is_valid = False
            if c not in max_values:
                max_values[c] = max(sets[c])
            elif any(num > max_values[c] for num in sets[c]):
                max_values[c] = max(sets[c])

        if is_valid:
            game_ids.append(gameID)

        powers.append(math.prod(max_values.values()))
    logger.debug("--- Part 1")
    print(sum(game_ids))
    logger.debug("--- Part 2")
    print(sum(powers))


logger.debug("Problem 1+2 - test data")
problem("d02_test.txt")
logger.debug("Part 1+2 - real data")
problem("d02.txt")
