"""
Object describe field with ships and player context
"""

from common import Cell, ShotResult, BadInputError
from ship_generator import ShipGeneratorFabric

from .ship import Ship


class BattleField:
    """
    Model of battle field object
    """

    def __init__(self, player_name, height, width, ship_rules, ship_generation_mode):
        """
        Args:
            player_name (str): player name
            height (int): field height
            width (int): field width
            ship_rules (dict): dict with ship size and count
                {
                    ship_size1[height, width] (int, int) : count1 (int)
                    ship_size2[height, width] (int, int) : count2 (int)
                }
            ship_generation_mode (int): ShipGenerationRule constant
        """
        self.height = height
        self.width = width
        self.player_name = player_name
        self.alive_ships_count = 0
        self.cells = []
        self.ships = []
        self.ship_generation_mode = ship_generation_mode

        self._clear_cells()
        self._generate_ships(ship_generation_mode, ship_rules)

    def shoot(self, cell_x, cell_y):
        """
        Make a shot to [x, y]

        Args:
            cell_x (int): number
            cell_y (int): letter

        Returns:
            int: ShotResult state
        """
        target = self.cells[cell_x][cell_y]

        if target == Cell.EMPTY:
            self.cells[cell_x][cell_y] = Cell.SHOT_PLACE

        elif target == Cell.SHIP:
            ship = self._find_ship(cell_x, cell_y)
            shot = ship.shot(cell_x, cell_y)
            if shot:
                return ShotResult.DAMAGED
            self._sink_ship(ship)
            if not self.alive_ships_count:
                return ShotResult.WIN
            return ShotResult.DESTROYED

        return ShotResult.MISSED

    def create_ship(self, cell_x, cell_y, width, height):
        """
        Args:
            cell_x (int): ship x
            cell_y (int): ship y
            width (int): ship width
            height (int): ship height
        """
        self._validate_ship_placement(cell_x, cell_y, width, height)
        self.ships.append(Ship(self.cells, cell_x, cell_y, width, height))

    def _validate_ship_placement(self, cell_x, cell_y, width, height):
        """
        Args:
            cell_x (int): ship x
            cell_y (int): ship y
            width (int): ship width
            height (int): ship height

        Raises:
            IndexError: some problems
        """
        ship_cells = set()
        for sh in self.ships:
            if sh.x_coord <= cell_x + height and sh.y_coord <= cell_y + width:
                ship_cells.update(list(sh.get_ship_body_gen()))
                ship_cells.update(list(sh.get_ship_area_gen()))
        if ship_cells:
            for _x in range(cell_x, cell_x + height):
                for _y in range(cell_y, cell_y + width):
                    if (_x, _y) in ship_cells:
                        raise BadInputError("Interception with ships")

    def _generate_ships(self, ship_generation_type, ship_rules):
        """
        Generate ship on the field

        Args:
            ship_generation_type (int): ShipGenerationRule constant
            ship_rules (dict): dict with ship size and count
                {
                    ship_size1[height, width] (int, int) : count1 (int)
                    ship_size2[height, width] (int, int) : count2 (int)
                }

        Raises:
            BadShipRuleError: if set ships by rules is impossible
        """
        generator = ShipGeneratorFabric.get(ship_generation_type, self)
        generator.generate_ships(ship_rules)

    def _find_ship(self, cell_x, cell_y):
        """
        Find ship by his coordinates

        Returns:
            Ship: ship object
        """
        for ship in self.ships:
            if ship.x_coord <= cell_x < ship.x2_coord and ship.y_coord <= cell_y < ship.y2_coord:
                return ship
        raise EnvironmentError("Hi! You caught impossible error")

    def _sink_ship(self, ship):
        """
        Mark all cells around ship as shot

        Args:
            ship (Ship): ship instance
        """
        for _x, _y in ship.get_ship_area_gen():
            if (0 <= _y < self.width) and (0 <= _x < self.height):
                self.cells[_x][_y] = Cell.SHOT_PLACE
        self.alive_ships_count -= 1

    def _clear_cells(self):
        """ Set all cells as Cell.EMPTY """
        self.cells = [[Cell.EMPTY] * self.width for _ in range(self.height)]
