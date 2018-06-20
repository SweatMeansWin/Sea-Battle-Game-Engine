"""
Contains class for manual ship insertion
"""

from common import parse_text_cell, BadInputError
from views.battle_field import BattleFieldView

from .base import BaseShipGenerator


class ManualShipGenerator(BaseShipGenerator):
    """
    Insert ships from console
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
        view = BattleFieldView(self._bf)
        view.draw()
        for ship_size, ship_count in ship_rules.items():
            for _ in range(ship_count):
                while True:
                    view.draw_line("Place [{},{}] ship.".format(ship_size[0], ship_size[1]))
                    # Get ship coordinates from console
                    input_text = input("Enter ship coordinates in format [A1,A4]: ")
                    try:
                        # Parse cell pairs
                        (from_x, from_y), (to_x, to_y) = list(map(
                            lambda x: parse_text_cell(x, self._bf.height, self._bf.width),
                            input_text.split(',')
                        ))
                    except ValueError:
                        continue
                    except BadInputError as exc:
                        view.draw_line(str(exc))
                        continue

                    # Get entered ship size and check
                    in_width = abs(to_y - from_y) + 1
                    in_height = abs(to_x - from_x) + 1
                    if ship_size not in ((in_width, in_height), (in_height, in_width)):
                        continue
                    try:
                        # Try to create ship with entered coordinates
                        self._bf.create_ship(
                            from_x,
                            from_y,
                            1 if to_y == from_y else abs(to_y - from_y) + 1,
                            1 if to_x == from_x else abs(to_x - from_x) + 1,
                        )
                    except IndexError:
                        view.draw_line("Bad values")
                        continue
                    except BadInputError as exc:
                        view.draw_line(str(exc))
                        continue
                    # Update what we draw
                    view.draw()
                    break
