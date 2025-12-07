from pathlib import Path

from helpers import GetFile, time_and_print, Board
from _2025._7.classes import SignalSplitter


def part1(board: Board) -> int:
    """Count unique splitters encountered during signal splitting."""
    signal_splitter = SignalSplitter(board)
    return signal_splitter.split_signal()


def part2(board: Board) -> int:
    """Count total signal lines using recursive counting."""
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
