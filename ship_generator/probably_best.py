"""
Contains class for static ship insertion
"""

from .base import BaseShipGenerator


class ProbablyBestShipGenerator(BaseShipGenerator):
    """
    Manual static ships for 10x10 fields
    """

    def _generate_ships(self, ship_rules):
        """
        Fill battle field with ships according to rules

        Args:
            ship_rules (dict): dict with ship size and count
                {
                    ship_size1[height, width] (int, int) : count1 (int)
                    ship_size2[height, width] (int, int) : count2 (int)
                }
        """
        # 4
        self._bf.create_ship(0, 0, 4, 1)
        # 3
        self._bf.create_ship(0, 6, 3, 1)
        self._bf.create_ship(2, 0, 1, 3)
        # 2
        self._bf.create_ship(2, self._bf.width - 1, 1, 2)
        self._bf.create_ship(5, self._bf.width - 1, 1, 2)
        self._bf.create_ship(6, 0, 1, 2)
        # 1
        self._bf.create_ship(4, 4, 1, 1)
        self._bf.create_ship(6, 6, 1, 1)
        self._bf.create_ship(7, 3, 1, 1)
        self._bf.create_ship(9, 6, 1, 1)
