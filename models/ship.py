"""
Presenting ship object
"""

from common import Cell


class Ship:
    """
    Ship model
    """

    def __init__(self, battle_field, cell_x, cell_y, width, height):
        """
        Args:
            battle_field (list[list[str]]): we will change field by pointer
            cell_x (int): x coordinate
            cell_y (int): y coordinate
            width (int): ship width
            height (int): ship height
        """
        self.x_coord = cell_x
        self.y_coord = cell_y
        self.width = width
        self.height = height
        self._field = battle_field
        for (_x, _y) in self.get_ship_body_gen():
            self._field[_x][_y] = Cell.SHIP
        self._alive_ship_cells = width * height

    @property
    def is_alive(self):
        """ True if ship has live cells """
        return self._alive_ship_cells > 0

    @property
    def x2_coord(self):
        """ x + height """
        return self.x_coord + self.height

    @property
    def y2_coord(self):
        """ y + width """
        return self.y_coord + self.width

    def shot(self, cell_x, cell_y):
        """
        Returns:
            bool: True if ship is still alive
        """
        if self._field[cell_x][cell_y] == Cell.SHIP:
            self._alive_ship_cells -= 1
            self._field[cell_x][cell_y] = Cell.DAMAGED
        return self.is_alive

    def get_ship_body_gen(self):
        """ get all ship cells """
        for _x in range(self.x_coord, self.x2_coord):
            for _y in range(self.y_coord, self.y2_coord):
                yield _x, _y

    def get_ship_area_gen(self):
        """ get all ship cells """
        for _x in range(self.x_coord - 1, self.x2_coord + 1):
            yield _x, self.y_coord - 1
            yield _x, self.y2_coord
        for _y in range(self.y_coord - 1, self.y2_coord + 1):
            yield self.x_coord - 1, _y
            yield self.x2_coord, _y
