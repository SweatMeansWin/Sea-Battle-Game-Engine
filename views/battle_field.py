"""
Classes which know how to represent battle field models to UI
"""

from common import FIRST_CHAR_CODE, Cell

from drawing import Drawable


class BattleFieldView(Drawable):
    """
    Class that return console table view for player field
    """

    def __init__(self, battle_field):
        """
        Args:
            battle_field (models.BattleField): map view to battle field
        """
        self._bf = battle_field

    @property
    def battle_field(self):
        """
        Returns:
            models.BattleField: connected battle field instance
        """
        return self._bf

    def draw(self):
        """ draw field """
        self.draw_line(self.get_headers())
        for row_idx in range(self._bf.height):
            self.draw_line(' ' * self.OFFSET + ' '.join('-' * (self._bf.width + 1)))
            self.draw_line(self.get_row(row_idx))
        self.draw_line('\n')

    def get_headers(self):
        """ return field header """
        return '{player} |{chars}'.format(
            player=self._bf.player_name.ljust(self.OFFSET, ' '),
            chars='|'.join(
                [chr(x) for x in range(
                    FIRST_CHAR_CODE,
                    FIRST_CHAR_CODE + self._bf.width
                )]
            )
        )

    def get_row(self, idx):
        """ return idx field row """
        return '{offset}{idx}|{field}'.format(
            offset=' ' * (self.OFFSET - 1),
            idx=str(idx + 1).rjust(2, ' '),
            field=self._get_field_row(idx),
        )

    def _get_field_row(self, idx):
        """ return field row cells info """
        return '|'.join(self._bf.cells[idx])


class BattleFieldEnemyView(BattleFieldView):
    """
    Derived class which hide ships position
    """

    def _get_field_row(self, idx):
        """ return row cells with replaced ships """
        return '|'.join(self._bf.cells[idx]).replace(Cell.SHIP, Cell.EMPTY)
