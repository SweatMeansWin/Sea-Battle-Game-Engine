"""
Contains class for manual ship insertion
"""

from .base import BaseShipGenerator, BadShipRuleError


class SimpleShipGenerator(BaseShipGenerator):
    """
    Fill ship positions
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
        x_cell = 0
        y_cell = 0
        for (ship_height, ship_width), ship_count in ship_rules.items():
            for _ in range(ship_count):
                while True:
                    if (
                            x_cell + ship_height < self._bf.height
                            and y_cell + ship_width < self._bf.width
                    ):
                        self._bf.create_ship(x_cell, y_cell, ship_width, ship_height)
                        break
                    else:
                        x_cell = 0
                        y_cell += max([s.width for s in self._bf.ships]) + 1
                        if y_cell >= self._bf.width:
                            raise BadShipRuleError("Not enough space for ships")
                x_cell += ship_height + 1
