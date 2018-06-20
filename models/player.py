"""
Contains player object realization
"""

from input_logic import GameInputsFabric


class Player:
    """
    Struct represent player object
    """

    def __init__(self, idx, game_mode, battle_field, game_views):
        """
        Args:
            idx (int): number
            game_mode (int): GameMode constant, choosing game logic
            battle_field (models.BattleField): battle field instance
            game_views (tuple[views.BattleFieldView]): views for UI
        """
        self.number = idx
        self.battle_field = battle_field
        self.player_name = battle_field.player_name
        self.game_mode = game_mode
        self.views = game_views
        self.input_engine = GameInputsFabric.get(game_mode, game_views[1].battle_field)
        self.last_result = None
