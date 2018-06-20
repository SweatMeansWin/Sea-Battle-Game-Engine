"""
Module contain input engine implement shooting in line
"""

from .auto_input import AutoInputEngine


class LineInputEngine(AutoInputEngine):
    """
    Shoot all cell line by line
    """

    def __init__(self, enemy_battle_field):
        super().__init__(enemy_battle_field)
        self._x = 0
        self._y = 0
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
        for _h in range(self._enemy_bf.height):
            for _w in range(self._enemy_bf.width):
                yield _h, _w
