"""
Here we start
"""

from pprint import pprint
from time import time

from common import GameMode, ShipGenerationMode
from game_engine import SeaBattleEngine

RULES = {
    (4, 1): 1,
    (3, 1): 2,
    (2, 1): 3,
    (1, 1): 4,
}
W, H = 10, 10


def get_statistic(game_count, settings):
    """
    Get average statistic

    Args:
        game_count (int): amount games to play
        settings (dict): GameMode constants

    Returns:
        dict: statistic game info
    """
    result = {
        'game_count': game_count,
        'count_start_player_won': 0,
        'max_round': None,
        'min_round': None,
        'avg_round': None,
        'settings': settings,
        'game_mode_wins': {k: 0 for k in settings['game_modes']},
        'ship_generation_mode_wins': {
            settings['ship_generation']['first']: 0,
            settings['ship_generation']['second']: 0,
        },
    }
    settings['hide_ui'] = True
    rounds = []
    engine = SeaBattleEngine(settings)
    for idx in range(game_count):
        engine.start()
        # Parse results
        _result = engine.get_result()
        rounds.append(_result['round'])
        result['count_start_player_won'] += int(_result['start_player_won'])
        result['game_mode_wins'][_result['game_mode_won']] += 1
        result['ship_generation_mode_wins'][_result['ship_generation_mode_won']] += 1
        # Refresh battle fields
        engine.refresh()

    result['max_round'] = max(rounds)
    result['min_round'] = min(rounds)
    result['avg_round'] = sum(rounds) // game_count
    return result


def play_game(game_settings):
    """
    Args:
        game_settings (dict): game settings
    """
    engine = SeaBattleEngine(game_settings)
    engine.start()
    pprint(engine.get_result())


if __name__ == '__main__':

    _settings = {
        'width': W,
        'height': H,
        'game_modes': (GameMode.RANDOM, GameMode.RANDOM),
        'ship_generation': {
            'ships': RULES,
            'first': ShipGenerationMode.RANDOM,
            'second': ShipGenerationMode.PROBABLY_BEST,
        },
        'hide_ui': False,
    }

    play_game(_settings)

    GAME_COUNT = 10000
    pprint(get_statistic(
        GAME_COUNT,
        _settings,
    ))
