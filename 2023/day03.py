from lib import *
import re
import typing
from collections import defaultdict
from itertools import product


def find_elements(s: str, r: dict, pattern=re.compile(r"(\d+|\D)")) -> tuple:
    """
    Finds all numerical and character elements and returns an object with their data
    Return:
       ( ELEMENT,
         {
            row: INT, row_value,
            start: INT, start_value,
            end: INT, end_value,
            is_digit: BOOL, is a digit?
         }

       )
    """
    for m in pattern.finditer(s):
        if m.group() != ".":
            yield (
                m.group(),
                {
                    "row": int(r),
                    "start": m.start(),
                    "end": m.start() + len(m.group()) - 1,
                    "is_digit": m.group().isdigit(),
                },
            )


def generate_adjacents(r: int, s: int, e: int) -> list:
    """
    Takes in a coordinate and generates all adjacent coordinates within the matrix.
    Returns a list of unique adjacent coordinates
    """
    # Generate all coordinates of the numeric value
    coordinates_value = [x for x in product(list(range(s, e + 1)), [r])]
    offsets = [-1, 0, 1]
    adjacents = []

    for c in coordinates_value:
        adjacents.extend(
            [
                i
                for i in list(product(*(range(n - 1, n + 2) for n in c)))
                if (i[0] > -1 and i[1] > -1 and (i not in coordinates_value))  #
            ]
        )
    # (y,x)
    return list(set(adjacents))


def check_adjacents(adj: list, chars: list) -> list:
    """
    Takes in a list of chars and an adjacency list and finds its intersection
    Yields all character objects overlapping with an adjacent position
    """
    for a in adj:
        for f in chars:
            if (f[1]["start"] == a[0]) and (f[1]["row"] == a[1]):
                yield f


def problems(f: typing.Union[str, os.PathLike]) -> None:
    """
    Solves both problems by using 2D coordinates to generate adjacent positions to numbers
    and then find the overlaps with the positions of the characters of interest
    """
    data = read_files(f)
    numeric_values = []
    special_chars = []
    total = 0
    gears = defaultdict(list)
    for r, row in enumerate(data):
        for f in find_elements(row, r):
            if f[1]["is_digit"]:
                numeric_values.append(f)
            else:
                special_chars.append(f)
    # generate adjacent positions and intersect with characters found
    for num, coords in numeric_values:
        adjacents = generate_adjacents(
            r=coords["row"], s=coords["start"], e=coords["end"]
        )
        any_adjacent_chars = [a for a in check_adjacents(adjacents, special_chars)]
        # Compute total for problem 1
        if len(any_adjacent_chars) > 0:
            total += int(num)
        # Store possible gears for problem 2
        for gear, gear_coords in any_adjacent_chars:
            if gear == "*":
                gear_id = str(gear_coords["row"]) + "-" + str(gear_coords["start"])
                gears[gear_id].append(num)
    # Results
    total_gears = 0
    for g in gears.keys():
        if len(gears[g]) == 2:
            total_gears += int(gears[g][0]) * int(gears[g][1])
    logger.debug("Task 1")
    logger.debug(total)
    logger.debug("Task 2")
    logger.debug(total_gears)


logger.debug("TEST")
problems("d03_test.txt")
logger.debug("PROBLEM")
problems("d03.txt")
