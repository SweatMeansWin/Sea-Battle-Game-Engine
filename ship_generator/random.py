"""

"""

import random

from common import BadInputError

from .base import BaseShipGenerator


class RandomShipGenerator(BaseShipGenerator):
    """

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
        for (ship_height, ship_width), ship_count in ship_rules.items():
            for _ in range(ship_count):
                while True:
                    if random.randint(0, 1) == 1:
                        cell_x = random.randint(0, self._bf.height - ship_height)
                        cell_y = random.randint(0, self._bf.width - ship_width)
                        w, h = ship_width, ship_height
                    else:
                        cell_x = random.randint(0, self._bf.width - ship_width)
                        cell_y = random.randint(0, self._bf.height - ship_height)
                        w, h = ship_height, ship_width

                    try:
                        self._bf.create_ship(
                            cell_x,
                            cell_y,
                            w,
                            h,
                        )
                    except (IndexError, BadInputError) as exc:
                        continue
                    break
