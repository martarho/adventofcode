from lib import *
from loguru import logger
import typing
import os


def find_digits(s: str) -> list:
    all_digits = []
    for d in s:
        if d.isdigit():
            all_digits.append(d)
    return all_digits


def translator(s: str) -> str:
    d = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }

    for k in d.keys():
        s = s.replace(k, str(d[k]))
    return s


def problem1(f: typing.Union[str, os.PathLike]) -> None:
    data = read_files(f)
    total = 0
    for s in data:
        digits = find_digits(s)
        total += int(str(digits[0]) + str(digits[-1]))
    print(total)


def problem2(f: typing.Union[str, os.PathLike]) -> None:
    data = read_files(f)
    total = 0
    for s in data:
        s = translator(s)
        digits = find_digits(s)
        total += int(str(digits[0]) + str(digits[-1]))
    print(total)


logger.debug("--- Problem 1 - test")
problem1("data/d01_test.txt")

logger.debug("--- Problem 1")
problem1("data/d01.txt")

logger.debug("--- Problem 2 - test")
problem2("data/d01_test2.txt")

logger.debug("--- Problem 2")
problem2("data/d01_part2.txt")
