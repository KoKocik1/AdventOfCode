from pathlib import Path

from helpers import GetFile
from helpers.array_helper import Board
from _2024._16.classes import MazeSolver

def part1(board: Board) -> int:
    solver = MazeSolver(board)
    solver.solve()
    print(board)
    return min(solver.scores)


def part2(board: Board) -> int:
    solver = MazeSolver(board)
    solver.solve()
    solver.mark_path(min(solver.scores))
    print(board)
    return board.count_characters('O')


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    board = Board(array)
    #print(part1(board))
    print(part2(board))


if __name__ == "__main__":
    main()
