"""
Module contain input engine implement random shooting
"""

import random

from .auto_input import AutoInputEngine


class RandomInputEngine(AutoInputEngine):
    """
    Class for choosing cell randomly
    """

    def _get_value(self):
        """
        Main method, result is used as value to game input

        Returns:
            int, int: cell coordinates
        """
        return (
            random.randint(0, self._enemy_bf.height - 1),
            random.randint(0, self._enemy_bf.width - 1),
        )
