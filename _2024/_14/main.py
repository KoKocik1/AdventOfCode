from pathlib import Path
import math
from copy import deepcopy

from helpers import GetFile
from _2024._14.classes import Board, Robot


# Constants
BOARD_WIDTH = 101
BOARD_HEIGHT = 103
PART1_STEPS = 100


def parse_robot_data(line: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Parse robot position and velocity from a line of input."""
    position_str = line[0].split('=')[1]
    velocity_str = line[1].split('=')[1]

    position = tuple(int(x) for x in position_str.split(','))
    velocity = tuple(int(x) for x in velocity_str.split(','))

    return position, velocity


def load_data(file: GetFile, width: int = BOARD_WIDTH, height: int = BOARD_HEIGHT) -> Board:
    """Load robots from file and create a board."""
    board = Board(width, height)
    for line in file.get_row():
        position, velocity = parse_robot_data(line)
        robot = Robot(position, velocity)
        board.add_robot(robot)
    return board


def part1(board: Board, steps: int = PART1_STEPS) -> int:
    """Move robots and return the product of quadrant counts."""
    board.move_robots(steps)
    quadrant_counts = board.count_robots_by_quadrant()
    return math.prod(quadrant_counts)


def part2(board: Board) -> int:
    """Find the first second where all robots are at unique positions."""
    second = 0
    while True:
        second += 1
        board.move_robots(1)
        if board.has_no_overlaps():
            board.print_board()
            return second


def main():
    """Main entry point."""
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')

    board = load_data(file)
    print(part1(board))
    board = load_data(file)
    print(part2(board))


if __name__ == "__main__":
    main()
