"""Tests for _2024/_16/main.py functions."""

import pytest
from helpers.array_helper import Board
from _2024._16.main import part1


def create_grid_from_string(grid_str: str) -> list[list[str]]:
    """Helper function to create a 2D grid from a string representation."""
    lines = grid_str.strip().split('\n')
    return [list(line) for line in lines if line.strip()]


class TestPart1:
    """Tests for part1 function."""

    def test_first_example(self):
        """Test with the first provided test data."""
        grid_str = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
        
        two_d_array = create_grid_from_string(grid_str)
        board = Board(two_d_array)
        result = part1(board)
        assert result == 7036

    def test_second_example(self):
        """Test with the second provided test data."""
        grid_str = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
        
        two_d_array = create_grid_from_string(grid_str)
        board = Board(two_d_array)
        result = part1(board)
        assert result == 11048

