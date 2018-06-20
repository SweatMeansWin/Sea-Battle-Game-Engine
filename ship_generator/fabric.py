"""
Contains fabric for ship generation engine
"""

from common import ShipGenerationMode

from .manual import ManualShipGenerator
from .random import RandomShipGenerator
from .simple import SimpleShipGenerator
from .probably_best import ProbablyBestShipGenerator


class ShipGeneratorFabric:
    """
    Class implement choosing input engine logic
    """

    @staticmethod
    def get(generator_type, battle_field=None):
        """
        Args:
            generator_type (int): GameMode constant
            battle_field (BattleField|None): field

        Returns:
            ship_generator.BaseShipGenerator: input engine
        """
        engine_type = None
        if generator_type == ShipGenerationMode.MANUAL:
            engine_type = ManualShipGenerator
        elif generator_type == ShipGenerationMode.RANDOM:
            engine_type = RandomShipGenerator
        elif generator_type == ShipGenerationMode.SIMPLE:
            engine_type = SimpleShipGenerator
        elif generator_type == ShipGenerationMode.PROBABLY_BEST:
            engine_type = ProbablyBestShipGenerator
        assert engine_type is not None, "Unknown ship generator type"
        return engine_type(battle_field)
