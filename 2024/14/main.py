from pathlib import Path
import math

from helpers import GetFile
from classes import Board, Robot


def load_data(file: GetFile) -> Board:
    board = Board(101, 103)
    for line in file.get_row():
        position = [int(x) for x in line[0].split('=')[1].split(',')]
        velocity = [int(x) for x in line[1].split('=')[1].split(',')]
        robot = Robot(position, velocity)
        board.add_robot(robot)
    return board


def part1(board: Board) -> int:
    board.move_robots(100)
    return math.prod(board.count_robots())


def part2(board: Board) -> int:
    second = 0
    while True:
        second += 1
        board.move_robots(1)
        if board.no_repeats():
            board.print_board()
            return second


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')
    board = load_data(file)
    print(part1(board))
    print(part2(board))


if __name__ == "__main__":
    main()
