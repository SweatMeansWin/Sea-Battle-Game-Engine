"""
Module contain input engine implement shooting in line
"""

from .auto_input import AutoInputEngine


class SpiralInputEngine(AutoInputEngine):
    """
    Shoot all cell line by line
    """

    def __init__(self, enemy_battle_field):
        super().__init__(enemy_battle_field)
        self._x = 0
        self._y = 0
        self._w = self._enemy_bf.width - 1
        self._h = self._enemy_bf.height - 1
        self._g = self._next_cell()

    def _get_value(self):
        """
        Main method, result is used as value to game input

        Returns:
            str: field cell in text format
        """
        return next(self._g)

    def _next_cell(self):
        """
        Returns:
            int, int: x, y coordinates
        """
        while True:
            for _y in range(self._y, self._w + 1):
                yield self._x, _y
            self._x += 1
            for _x in range(self._x, self._h + 1):
                yield _x, self._h
            self._w -= 1
            for _y in reversed(range(self._y, self._w + 1)):
                yield self._h, _y
            self._h -= 1
            for _x in reversed(range(self._x, self._h + 1)):
                yield _x, self._y
            self._y += 1
