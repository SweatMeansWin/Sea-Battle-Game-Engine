"""
Module contain input engine implement random shooting
"""

from .auto_input import AutoInputEngine


class StaticInputEngine(AutoInputEngine):
    """
    Class for choosing constant cell (For testing)
    """

    def get_value(self, last_result=None):
        """
        Main method, result is used as value to game input

        Args:
            last_result (int|None): ShotResult of previous choose

        Returns:
            int, int: cell coordinates
        """
        return 0, 0

    def _get_value(self):
        """
        The one cell to rule them all
        """
        pass
