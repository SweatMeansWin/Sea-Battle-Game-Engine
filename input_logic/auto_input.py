"""
Contain class for automated
"""

from common import ShotResult, Cell

from .base import BaseInputEngine


class AutoInputEngine(BaseInputEngine):
    """
    Class for choosing cell randomly
    """

    def __init__(self, enemy_battle_field=None):
        """
        Storing view for checking shots already done

        Args:
            enemy_battle_field (models.BattleField|None): bf view
        """
        super().__init__(enemy_battle_field)
        self._previous_cell = None
        self._previous_stack = []
        self._direction_cycle = (
            lambda cell: (cell[0], cell[1] + 1),
            lambda cell: (cell[0], cell[1] - 1),
            lambda cell: (cell[0] + 1, cell[1]),
            lambda cell: (cell[0] - 1, cell[1]),
        )

    def get_value(self, last_result=None):
        """
        Main method, result is used as value to game input

        Args:
            last_result (int|None): ShotResult of previous choose

        Returns:
            int, int: cell coordinates
        """
        if last_result == ShotResult.DESTROYED:
            # If ship destroyed, clear context and use internal logic
            self._previous_stack.clear()
        elif last_result == ShotResult.DAMAGED:
            # If we damaged ship we should find others cells
            # Remember the one we hit, because now we have 4 possible directions
            _cell = self._check_possible_cell(self._previous_cell)
            if _cell:
                self._previous_stack.append(self._previous_cell)
                self._previous_cell = _cell
                return _cell
            if not _cell:
                self._previous_cell = self._previous_stack.pop()
                return self.get_value(last_result)

        elif last_result == ShotResult.MISSED:
            # If stack has elements that we hit ago and moved to wrong direction
            if self._previous_stack:
                self._previous_cell = self._previous_stack[-1]
                _cell = self._check_possible_cell(self._previous_cell)
                if _cell:
                    self._previous_cell = _cell
                    return _cell
                if not _cell:
                    self._previous_cell = self._previous_stack.pop()
                    return self.get_value(last_result)

        # Internal logic in child classes
        while True:
            # We skip already cells already hit
            next_cell = self._get_value()
            if self._enemy_bf.cells[next_cell[0]][next_cell[1]] not in (Cell.SHOT_PLACE, Cell.DAMAGED):
                break
        self._previous_cell = next_cell
        return self._previous_cell

    def _check_possible_cell(self, cell):
        """
        Args:
            cell (tuple[int]): x, y - possible cell coordinates

        Returns:
            tuple[int]|None: good cell coordinates
        """
        for direction_func in self._direction_cycle:
            _cell = direction_func(cell)
            if (
                0 <= _cell[0] < self._enemy_bf.height
                and 0 <= _cell[1] < self._enemy_bf.width
                and self._enemy_bf.cells[_cell[0]][_cell[1]] not in (Cell.SHOT_PLACE, Cell.DAMAGED)
            ):
                return _cell
            else:
                continue
        return None

    def _get_value(self):
        """
        Implement bot internal logic

        Returns:
            int, int: cell coordinates
        """
        raise NotImplementedError()
