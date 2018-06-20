"""
Module contain input engine implement shooting by diagonal
"""

from .auto_input import AutoInputEngine


class DiagonalInputEngine(AutoInputEngine):
    """
    Shoot all cell by diagonal
    """

    def __init__(self, enemy_battle_field):
        """
        Storing view for checking shots already done

        Args:
            enemy_battle_field (models.BattleField|None): bf view
        """
        super().__init__(enemy_battle_field)
        self._x = 0
        self._w = 0
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
            _x = self._x
            _y = self._w
            while _y >= 0 and _x < self._enemy_bf.height:
                yield _x, _y
                _x += 1
                _y -= 1
            if self._w < self._enemy_bf.width - 1:
                self._w += 1
            else:
                self._x += 1
