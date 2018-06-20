"""
Contain base class for input
"""


class InputInterrupted(Exception):
    """ stop game """


class BaseInputEngine:
    """
    Base class for input engine
    """

    def __init__(self, enemy_battle_field=None):
        """
        Storing view for checking shots already done

        Args:
            enemy_battle_field (models.BattleField|None): bf view
        """
        self._enemy_bf = enemy_battle_field

    def get_value(self, last_result=None):
        """
        Main method, result is used as value to game input

        Args:
            last_result (int|None): ShotResult of previous choose

        Returns:
            int, int: cell coordinates
        """
        raise NotImplementedError()
