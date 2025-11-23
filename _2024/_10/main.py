from pathlib import Path

from helpers import GetFile, Board
from classes import Climber


def _process_trailheads(array: list[list[str]], score_method: str) -> int:
    """Process all trailheads and accumulate scores using the specified method."""
    board = Board(array)
    trailheads = board.find_all_character_positions('0')
    total_score = 0

    for trailhead in trailheads:
        climber = Climber(board)
        climber.find_trail(trailhead)
        if score_method == 'positions':
            total_score += climber.get_score()
        elif score_method == 'ways':
            total_score += climber.get_score_ways()

    return total_score


def part1(array: list[list[str]]) -> int:
    return _process_trailheads(array, 'positions')


def part2(array: list[list[str]]) -> int:
    return _process_trailheads(array, 'ways')


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
