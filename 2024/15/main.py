from pathlib import Path

from helpers import GetFile
from helpers.array_helper import Board
from classes import CleanBoard


def part1(board: Board, moves: list[str]) -> int:
    clean_board = CleanBoard(board, moves)
    clean_board.clean_board()
    print(board)
    positions = board.find_all_character_positions('O')
    score = 0
    for position in positions:
        row = position.row
        col = position.col
        score += 100*row+col
    return score


def part2(array: list[list[int]]) -> int:
    return 0


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    data_file1 = Path(__file__).parent / 'data/data_moves.txt'
    file = GetFile(str(data_file), delimiter='')
    board = Board(file.get_2d_array())
    file1 = GetFile(str(data_file1), delimiter='')
    moves = []
    for line in file1.get_row():
        moves.extend(list(line))
    print(part1(board, moves))
    # print(part2(board, moves))


if __name__ == "__main__":
    main()
