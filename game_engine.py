"""
Game starter, controller
"""

from random import randint

from common import GameMode, ShotResult
from models.battle_field import BattleField
from models.player import Player
from views.battle_field import BattleFieldView, BattleFieldEnemyView
from views.game_view import SeaBattleGameView, SeaBattleResultGameView


class SeaBattleEngine:
    """
    Game engine, control fields and returning
    """

    PLAYERS = ('me', 'enemy')

    def __init__(self, settings):
        """
        Args:
            settings (dict):
                {
                    width (int): field width
                    height (int): field height
                    game_modes (tuple[int]): GameMode constants,
                    ship_generation (dict): dict with ship size and count
                        {
                            'ships' (dict): {
                                ship_size1[height, width] (int, int) : count1 (int)
                                ship_size2[height, width] (int, int) : count2 (int)
                            },
                            'first' (int): ShipGeneratorRules,
                            'second' (int): ShipGeneratorRules,
                        }
                    start_player_idx (int|None): index of starting player
                }
        """
        self._game_view = None
        self._round = 0
        self._start_player_idx = 0
        self._current_player_idx = 0
        self._settings = settings
        self._prepare()

    @property
    def size(self):
        """
        Returns:
            int, int: field width and height
        """
        return self._settings['width'], self._settings['height']

    @property
    def current_player(self):
        """
        Returns:
            Player: current player
        """
        return self._players[self._current_player_idx]

    def start(self):
        """ begin our journey """
        game_view = self._get_view()
        game_view.introduce()
        game_view.enter_loop()

    def shoot(self, cell_x, cell_y):
        """
        Trying killing someone

        Args:
            cell_x (int): number
            cell_y (int): letter

        Returns:
            int: ShotResult constant
        """
        shot_result = self._players[1 - self._current_player_idx].battle_field.shoot(cell_x, cell_y)
        self.current_player.last_result = shot_result
        return shot_result

    def update(self, shot):
        """
        Process round result

        Args:
            shot (int): ShotResult constant
        """
        self._round += 1
        if shot == ShotResult.MISSED:
            self._current_player_idx = 1 - self._current_player_idx
        elif shot == ShotResult.WIN:
            self._game_view.finish(self._round)

    def refresh(self):
        """
        Begin our journey
        """
        self._prepare()
        self._game_view = None

    def get_result(self):
        """
        Returns:
            dict: game info
            {
                round (int): round count
                mode (int): game mode
                width (int): field width
                height (int): field height
                first_player_won: (bool) player made first step won
            }
        """
        return {
            'settings': self._settings,
            'round': self._round,
            'game_mode_won': self.current_player.game_mode,
            'ship_generation_mode_won': self.current_player.battle_field.ship_generation_mode,
            'start_player_won': self._current_player_idx == self._start_player_idx,
        }

    def _prepare(self):
        """
        Init attributes
        """
        # Create battlefields
        battle_fields = (
            BattleField(
                'player1',
                self._settings['width'],
                self._settings['height'],
                self._settings['ship_generation']['ships'],
                self._settings['ship_generation']['first'],
            ),
            BattleField(
                'player2',
                self._settings['width'],
                self._settings['height'],
                self._settings['ship_generation']['ships'],
                self._settings['ship_generation']['second'],
            ),
        )
        # Init player attributes
        self._round = 0
        self._start_player_idx = self._settings.get('start_player_idx', randint(0, 1))
        self._current_player_idx = self._start_player_idx
        self._players = [
            Player(
                idx=idx,
                game_mode=self._settings['game_modes'][idx],
                battle_field=battle_fields[idx],
                game_views=(
                    BattleFieldView(battle_fields[idx]),
                    BattleFieldEnemyView(battle_fields[1 - idx])
                )
            ) for idx in range(2)
        ]

    def _get_view(self):
        """
        Get view for UI

        Returns:
            SeaBattleGameView: instance of view
        """
        if not self._game_view:
            if not self._settings.get('hide_ui') or GameMode.PLAYER in self._settings['game_modes']:
                self._game_view = SeaBattleGameView(self)
            else:
                self._game_view = SeaBattleResultGameView(self)
        return self._game_view
