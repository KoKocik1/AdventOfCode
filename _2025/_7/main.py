from pathlib import Path

from helpers import GetFile, time_and_print, Board
from classes import SignalSplitter


def part1(board: Board) -> tuple[int, int]:
    signal_splitter = SignalSplitter(board)
    splitters = signal_splitter.split_signal()
    return splitters


def part2(board: Board) -> int:
    signal_splitter = SignalSplitter(board)
    return signal_splitter.count_signal_lines()


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter='')
    array = file.get_2d_array()
    board = Board(array)
    result1 = time_and_print("Part 1", part1, board)
    result2 = time_and_print("Part 2", part2, board)


if __name__ == "__main__":
    main()
