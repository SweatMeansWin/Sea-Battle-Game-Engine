"""
Contain class for user console input
"""

from common import parse_text_cell
from common import BadInputError

from .base import BaseInputEngine, InputInterrupted


class UserInputEngine(BaseInputEngine):
    """
    Class for getting cell from console
    """

    def get_value(self, last_result=None):
        """
        Main method, result is used as value to game input

        Args:
            last_result (int|None): ShotResult of previous choose

        Returns:
            str: field cell in text format

        Raises:
            InputInterrupted: when user want to stop
        """
        while True:
            try:
                input_text = input('Your move: ')
            except EOFError:
                raise InputInterrupted("EOF")
            try:
                return parse_text_cell(
                    input_text,
                    self._enemy_bf.height,
                    self._enemy_bf.width
                )
            except BadInputError:
                continue
