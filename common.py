"""
Common constants and declarations
"""

import re

FIRST_CHAR = 'A'
FIRST_CHAR_CODE = ord(FIRST_CHAR)


class GameMode:
    """
    Constants for game modes
    """
    PLAYER = 0
    # Others are auto
    RANDOM = 1
    SPIRAL = 2
    LINE = 3
    DIAGONAL = 4
    STATIC = 5


class ShipGenerationMode:
    """
    Constants for ship generation
    """
    MANUAL = 0
    RANDOM = 1
    SIMPLE = 2
    PROBABLY_BEST = 3


class Cell:
    """
    Constants for drawing battlefield cell
    """
    EMPTY = ' '
    SHIP = 'H'
    SHOT_PLACE = 'o'
    DAMAGED = 'x'


class ShotResult:
    """
    Constants for shoot result
    """
    MISSED = 1
    DAMAGED = 2
    DESTROYED = 3
    WIN = 4


class BadInputError(Exception):
    """ raise if user enter bad value """


INPUT_PATTERN = re.compile(r'([a-zA-Z]+)(\d+)')


def parse_text_cell(input_text, height, width):
    """
    Validate and parse input

    Args:
        input_text (str): input in {LETTER}{NUMBER} format
        height (int): field height
        width (int): field width

    Returns:
        int, int: coordinates

    Raises:
        BadInputError: when input is wrong
    """
    if not input_text:
        raise BadInputError("Empty input")
    try:
        groups = INPUT_PATTERN.findall(input_text)[0]
        cell_y = ord(groups[0].upper()) - FIRST_CHAR_CODE  # letter (column)
        cell_x = int(groups[1]) - 1  # number (row)
        assert 0 <= cell_x < height, 'No such number'
        assert 0 <= cell_y < width, 'No such letter'
    except IndexError:
        raise BadInputError('Input format "A1"')
    except AssertionError as exc:
        raise BadInputError(str(exc))
    return cell_x, cell_y
