from pathlib import Path

from helpers import GetFile, Board
from classes import Climber


def part1(array: list[list[str]]) -> int:
    board = Board(array)
    count = 0
    trailheads = board.find_all_character_positions('0')
    for trailhead in trailheads:
        climber = Climber(board)
        climber.find_trail(trailhead)
        count += climber.get_score()
    return count


def part2(array: list[list[str]]) -> int:
    board = Board(array)
    count = 0
    trailheads = board.find_all_character_positions('0')
    for trailhead in trailheads:
        climber = Climber(board)
        climber.find_trail(trailhead)
        count += climber.get_score_ways()
    return count


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    print(part1(array))
    print(part2(array))


if __name__ == "__main__":
    main()
