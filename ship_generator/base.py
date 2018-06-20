"""
Contain base class for ship generation
"""


class BadShipRuleError(Exception):
    """ raise when ships can't be placed according the rules """


class BaseShipGenerator:
    """
    Class declare ship generation methods
    """

    def __init__(self, battle_field):
        """
        Args:
            battle_field (models.BattleField): map generator to battle field
        """
        self._bf = battle_field

    def generate_ships(self, ship_rules):
        """
        Fill battle field with ships according to rules

        Args:
            ship_rules (dict): dict with ship size and count
                {
                    ship_size1[height, width] (int, int) : count1 (int)
                    ship_size2[height, width] (int, int) : count2 (int)
                }
        """
        self._bf.ships.clear()
        self._generate_ships(ship_rules)
        self._bf.alive_ships_count = len(self._bf.ships)

    def _generate_ships(self, ship_rules):
        """ Internal class logic """
        raise NotImplementedError()
