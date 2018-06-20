"""
General GUI for engine
"""

from common import ShotResult
from drawing import Drawable
from input_logic.base import InputInterrupted


class SeaBattleGameView(Drawable):
    """
    General UI
    """

    DELIMITER = '\t' * 5

    def __init__(self, game_engine):
        """
        Args:
            game_engine (game_engine.SeaBattleEngine): game instance
        """
        self._engine = game_engine
        self._playing = True

    def introduce(self):
        """
        Hi!
        """
        self.draw_line("Hello!\nSea Battle game\n")
        self._draw_current_user_fields()

    def enter_loop(self):
        """
        Enter the game loop UI interaction
        """
        while self._playing:
            try:
                cell_x, cell_y = self._engine.current_player.input_engine.get_value(
                    self._engine.current_player.last_result
                )
            except InputInterrupted:
                return
            shoot_result = self._engine.shoot(cell_x, cell_y)
            self._engine.update(shoot_result)
            self.update(shoot_result)

    def update(self, shot_result):
        """
        Update UI: show shoot result and redraw field

        Args:
            shot_result (int): ShotResult constant
        """
        if shot_result == ShotResult.WIN:
            return
        elif shot_result == ShotResult.DAMAGED:
            self.draw_line("You damaged enemy's ship")
        elif shot_result == ShotResult.DESTROYED:
            self.draw_line("Enemy's ship is destroyed. Lucky you!")
        elif shot_result == ShotResult.MISSED:
            self.draw_line("Better next luck")
        self._draw_current_user_fields()

    def finish(self, round_num):
        """
        Show finish words

        Args:
            round_num (int): round count
        """
        self._playing = False
        self._draw_current_user_fields()
        self.draw_line("Thank you very much\nOur winner is '{}'. Win in {} round".format(
            self._engine.current_player.player_name,
            round_num,
        ))

    def _draw_current_user_fields(self):
        """ draw user and enemy fields """
        _views = self._engine.current_player.views
        self.draw_line(
            self.DELIMITER.join([cell_x.get_headers() for cell_x in _views])
        )
        (cell_x, cell_y) = self._engine.size
        for row_idx in range(cell_x):
            self.draw_line(
                self.DELIMITER.join(
                    [' ' * self.OFFSET + ' '.join('-' * (cell_y + 1))] * len(_views)
                )
            )
            self.draw_line(
                self.DELIMITER.join([cell_x.get_row(row_idx) for cell_x in _views])
            )
        self.draw_line('\n')


class SeaBattleResultGameView(SeaBattleGameView):
    """
    Representing view for bots playing without showing results
    """

    def introduce(self):
        """
        No introducing
        """
        pass

    def update(self, shot_result):
        """
        Update UI: show nothing there
        """
        pass

    def finish(self, round_num):
        """
        Finish in silence
        """
        self._playing = False
