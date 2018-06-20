"""
Containt fabric class for input engines
"""

from common import GameMode

from input_logic import UserInputEngine
from input_logic import StaticInputEngine, RandomInputEngine
from input_logic import LineInputEngine, SpiralInputEngine, DiagonalInputEngine


class GameInputsFabric:
    """
    Class implement choosing input engine logic
    """

    @staticmethod
    def get(game_mode, battle_field=None):
        """
        Args:
            game_mode (int): GameMode constant
            battle_field (BattleField|None): field

        Returns:
            BaseInputEngine: input engine
        """
        engine_type = None
        if game_mode == GameMode.PLAYER:
            engine_type = UserInputEngine
        elif game_mode == GameMode.RANDOM:
            engine_type = RandomInputEngine
        elif game_mode == GameMode.LINE:
            engine_type = LineInputEngine
        elif game_mode == GameMode.STATIC:
            engine_type = StaticInputEngine
        elif game_mode == GameMode.SPIRAL:
            engine_type = SpiralInputEngine
        elif game_mode == GameMode.DIAGONAL:
            engine_type = DiagonalInputEngine
        assert engine_type is not None, "Unknown game mode"
        return engine_type(battle_field)
